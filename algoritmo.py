"""Core logic for simulating a discrete-event call centre.

This module contains helper functions to compute key metrics and the
``run_simulation`` function which orchestrates the event loop.  Only the
Python standard library and NumPy are used so that the scheduling
mechanics remain easy to follow.
"""

from __future__ import annotations

from typing import Iterable, List, Optional, Sequence, Tuple

from filter import first_level, second_level, sort_by_work_time


def _sl(calls: Sequence, *, threshold: int = 5) -> float:
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

    count = 0
    for c in calls:
        if c.wait_time() < threshold:
            count += 1
    return count / len(calls) if calls else 0.0


def _asa(calls: Sequence, sla: Sequence[float]) -> float:
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

    count = 0
    for c in calls:
        j = int(c.department)
        if c.handle_time + c.duration - c.time < sla[j]:
            count += 1
    return count / len(calls) if calls else 0.0


def _p_wait_queue(calls: Sequence) -> float:
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

    count = 0
    for c in calls:
        if c.wait_time() > 0:
            count += 1
    return count / len(calls) if calls else 0.0


def _average_work_time(workers: Sequence) -> float:
    """Return average worker utilisation.

    Parameters
    ----------
    workers : Sequence
        Iterable of worker objects implementing ``work_time``.

    Returns
    -------
    float
        Ratio of minutes spent on calls relative to an 8 hour shift.
    """

    total_work = 0
    for w in workers:
        total_work += w.work_time()
    return total_work / (len(workers) * 8 * 60) if workers else 0.0


def run_simulation(
    calls: Optional[Iterable] = None,
    workers: Optional[Iterable] = None,
    sla: Optional[Sequence[float]] = None,
) -> Tuple[int, int, int, float, float, float, float]:
    """Run the call center simulation and return summary metrics.

    Parameters
    ----------
    calls : Iterable, optional
        Sequence of :class:`call.Call` objects.  When ``None`` a new dataset is
        generated.
    workers : Iterable, optional
        Sequence of :class:`worker.WorkerType` instances.  When ``None`` new
        workers are built using the generated skill matrices.
    sla : Sequence[float], optional
        SLA thresholds for each department.

    Returns
    -------
    tuple
        ``(professionals, helpers, waiting, SL, ASA, p_wait, work_time)`` where
        each value corresponds to one of the metrics computed during the
        simulation.

    Notes
    -----
    When ``calls`` or ``workers`` are omitted the required modules are
    reloaded so that every run uses fresh random input data.
    """

    if calls is None or workers is None or sla is None:
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
        if workers is None:
            workers = worker_mod.workers
        if sla is None:
            sla = data_mod.tSLA

    # Convert to lists for multiple iterations and because filter helpers expect
    # list objects.
    calls = list(calls)
    workers = list(workers)

    professionals = 0
    helpers = 0
    waiting = 0

    for call_item in calls:
        call_type = call_item.department + 1  # departments are 1-indexed
        primary_workers = sort_by_work_time(first_level(workers, call_type))
        secondary_workers = sort_by_work_time(second_level(workers, call_type))

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
        _sl(calls),
        _asa(calls, sla),
        _p_wait_queue(calls),
        _average_work_time(workers),
    )


if __name__ == "__main__":
    for value in run_simulation():
        print(value)

