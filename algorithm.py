"""Core logic for simulating a discrete-event call centre.

This module contains helper functions to compute key metrics and the
``run_simulation`` function which orchestrates the event loop.  Only the
Python standard library and NumPy are used so that the scheduling
mechanics remain easy to follow.
"""

from __future__ import annotations

from typing import Iterable, List, Optional, Sequence, Tuple

from department import Department

from filter import first_level, second_level, sort_by_work_time


def _service_level(calls: Sequence, *, threshold: int = 5) -> float:
    """Return service level for ``calls``.

    Parameters
    ----------
    calls : Sequence
        Iterable of call objects implementing ``wait_time``.
    threshold : int, optional
        Maximum waiting time considered acceptable. Defaults to ``5`` minutes.

    Returns
    -------
    float
        Fraction of calls answered before ``threshold`` minutes.
    """

    count = sum(1 for call_obj in calls if call_obj.wait_time() < threshold)
    return count / len(calls) if calls else 0.0

def _sla_compliance(calls: Sequence, sla: Sequence[float]) -> float:
    """Return share of ``calls`` solved within their SLA.

    Parameters
    ----------
    calls : Sequence
        Iterable of call objects.
    sla : Sequence[float]
        SLA thresholds for each department.

    Returns
    -------
    float
        Ratio of calls completed before exceeding their SLA.
    """

    count = sum(
        1
        for call_obj in calls
        if call_obj.handle_time + call_obj.duration - call_obj.time
        < sla[int(call_obj.department)]
    )
    return count / len(calls) if calls else 0.0



def _queue_fraction(calls: Sequence) -> float:
    """Return fraction of ``calls`` that had to wait in queue.

    Parameters
    ----------
    calls : Sequence
        Iterable of call objects.

    Returns
    -------
    float
        Proportion of calls with non-zero waiting time.
    """

    count = sum(1 for call_obj in calls if call_obj.wait_time() > 0)
    return count / len(calls) if calls else 0.0


def _average_utilisation(agents: Sequence) -> float:
    """Return average agent utilisation.

    Parameters
    ----------
    agents : Sequence
        Iterable of agent objects implementing ``work_time``.

    Returns
    -------
    float
        Ratio of minutes spent on calls relative to an 8 hour shift.
    """

    total_work = sum(agent.work_time() for agent in agents)
    return total_work / (len(agents) * 8 * 60) if agents else 0.0


def run_simulation(
    calls: Optional[Iterable] = None,
    agents: Optional[Iterable] = None,
    sla: Optional[Sequence[float]] = None,
) -> Tuple[int, int, int, float, float, float, float]:
    """Run the call center simulation and return summary metrics.

    Parameters
    ----------
    calls : Iterable, optional
        Sequence of :class:`call.Call` objects.  When ``None`` a new dataset is
        generated.
    agents : Iterable, optional
        Sequence of :class:`worker.Agent` instances.  When ``None`` new
        agents are built using the generated skill matrices.
    sla : Sequence[float], optional
        SLA thresholds for each department.

    Returns
    -------
    tuple
        ``(professionals, helpers, waiting, service_level, sla_compliance,
        queue_fraction, average_utilisation)`` where each value corresponds to
        one of the metrics computed during the simulation.

    Notes
    -----
    When ``calls`` or ``agents`` are omitted the required modules are
    reloaded so that every run uses fresh random input data.
    """

    if calls is None or agents is None or sla is None:
        # Deferred imports to avoid heavy module loading unless necessary
        import importlib
        import data as data_mod
        import worker as worker_mod
        import call as call_mod

        data_mod = importlib.reload(data_mod)
        worker_mod = importlib.reload(worker_mod)
        call_mod = importlib.reload(call_mod)

        if calls is None:
            calls = call_mod.calls
        if agents is None:
            agents = worker_mod.agents
        if sla is None:
            sla = data_mod.sla_targets

    # Convert to lists for multiple iterations and because filter helpers expect
    # list objects.
    calls = list(calls)
    agents = list(agents)

    professionals = 0
    helpers = 0
    waiting = 0

    for call_item in calls:
        call_type = int(call_item.department) + 1  # departments are 1-indexed
        primary_workers = sort_by_work_time(first_level(agents, call_type))
        secondary_workers = sort_by_work_time(second_level(agents, call_type))

        attended = False
        for worker in primary_workers:
            if worker.is_free(call_item):
                worker.schedule.append(call_item)
                worker.schedule[-1].handle_time = call_item.time
                professionals += 1
                attended = True
                break

        if not attended:
            for worker in secondary_workers:
                if worker.is_free(call_item):
                    worker.schedule.append(call_item)
                    worker.schedule[-1].handle_time = call_item.time
                    helpers += 1
                    attended = True
                    break

        if not attended:
            concat = sort_by_work_time(primary_workers + secondary_workers)
            waiting += 1
            call_item.handle_time = concat[0].next_available()
            concat[0].schedule.append(call_item)

    return (
        professionals,
        helpers,
        waiting,
        _service_level(calls),
        _sla_compliance(calls, sla),
        _queue_fraction(calls),
        _average_utilisation(agents),
    )


def run_simulation_detailed(
    calls: Optional[Iterable] = None,
    agents: Optional[Iterable] = None,
    sla: Optional[Sequence[float]] = None,
) -> Tuple[int, int, int, float, float, float, float, float, float]:
    """Run the simulation and compute additional skill metrics.

    The first seven elements of the returned tuple match
    :func:`run_simulation`.  Two extra values provide the average waiting
    time for calls handled by specialists and helpers respectively.  A
    specialist is a worker whose skill is ``8`` for the department of the
    call.  Helpers have a skill between ``5`` and ``7``.
    """

    # keep references so we can inspect the schedules after running
    if calls is None or agents is None or sla is None:
        import importlib
        import data as data_mod
        import worker as worker_mod
        import call as call_mod

        data_mod = importlib.reload(data_mod)
        worker_mod = importlib.reload(worker_mod)
        call_mod = importlib.reload(call_mod)

        if calls is None:
            calls = call_mod.calls
        if agents is None:
            agents = worker_mod.agents
        if sla is None:
            sla = data_mod.sla_targets

    calls = list(calls)
    agents = list(agents)

    result = run_simulation(calls, agents, sla)

    specialist_wait = []
    helper_wait = []
    for agent in agents:
        for call_obj in agent.schedule:
            skill = agent.skill_for(int(call_obj.department) + 1)
            if skill >= 8:
                specialist_wait.append(call_obj.wait_time())
            elif 5 <= skill <= 7:
                helper_wait.append(call_obj.wait_time())

    avg_spec = sum(specialist_wait) / len(specialist_wait) if specialist_wait else 0.0
    avg_help = sum(helper_wait) / len(helper_wait) if helper_wait else 0.0

    return result + (avg_spec, avg_help)


if __name__ == "__main__":
    for value in run_simulation():
        print(value)

