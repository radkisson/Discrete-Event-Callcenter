import math

from algorithm import (
    _service_level,
    _sla_compliance,
    _queue_fraction,
    _average_utilisation,
    run_simulation_detailed,
)


class DummyCall:
    def __init__(self, time, duration, department, sla, handle_time=None):
        self.time = time
        self.duration = duration
        self.department = department
        self.sla = sla
        self.handle_time = handle_time if handle_time is not None else time

    def wait_time(self):
        return self.handle_time - self.time

    def delta_t(self):
        return self.wait_time()


class DummyWorker:
    def __init__(self, department, skill):
        self.department = department
        self.number = 0
        self.schedule = []
        self.skill = skill

    def skill_for(self, number):
        return self.skill if number - 1 == self.department else 0

    def work_time(self):
        return sum(c.duration for c in self.schedule)

    def next_available(self):
        if not self.schedule:
            return 0
        c = self.schedule[-1]
        return c.time + c.duration + c.delta_t()

    def is_free(self, call):
        return self.next_available() <= call.time


def test_service_level_threshold():
    calls = [
        DummyCall(0, 1, 0, 10, 0),
        DummyCall(0, 1, 0, 10, 6),
        DummyCall(0, 1, 0, 10, 4),
    ]
    result = _service_level(calls, threshold=5)
    assert math.isclose(result, 2 / 3)


def test_sla_compliance():
    calls = [
        DummyCall(0, 5, 0, 10, 0),
        DummyCall(0, 8, 0, 10, 4),
    ]
    sla = [10]
    result = _sla_compliance(calls, sla)
    assert math.isclose(result, 0.5)


def test_queue_fraction():
    calls = [
        DummyCall(0, 1, 0, 10, 0),
        DummyCall(0, 1, 0, 10, 1),
        DummyCall(0, 1, 0, 10, 2),
    ]
    result = _queue_fraction(calls)
    assert math.isclose(result, 2 / 3)


def test_average_utilisation():
    class Worker:
        def __init__(self, work):
            self.work = work

        def work_time(self):
            return self.work

    workers = [Worker(60), Worker(30)]
    result = _average_utilisation(workers)
    expected = (60 + 30) / (2 * 8 * 60)
    assert math.isclose(result, expected)


def test_run_simulation_detailed_waits():
    calls = [
        DummyCall(0, 5, 0, 10),
        DummyCall(1, 3, 0, 10),
        DummyCall(2, 4, 0, 10),
    ]
    workers = [DummyWorker(0, 8), DummyWorker(0, 6)]
    sla = [10]

    result = run_simulation_detailed(calls, workers, sla)
    expected = (
        1,  # professionals
        1,  # helpers
        1,  # waiting
        1.0,  # service level
        1.0,  # SLA compliance
        1 / 3,  # queue share
        12 / (2 * 8 * 60),  # average utilisation
        0.0,  # specialist wait
        1.0,  # helper wait
    )
    assert len(result) == len(expected)
    for r, e in zip(result, expected):
        assert math.isclose(r, e, rel_tol=1e-9)
