import math

from algorithm import run_simulation

class DummyCall:
    def __init__(self, time, duration, department, sla):
        self.time = time
        self.duration = duration
        self.department = department
        self.sla = sla
        self.handle_time = 0

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


def test_single_call():
    calls = [DummyCall(0, 5, 0, 10)]
    workers = [DummyWorker(0, 8)]
    sla = [10]

    result = run_simulation(calls, workers, sla)

    expected = (
        1,        # professionals
        0,        # helpers
        0,        # waiting
        1.0,      # service level
        1.0,      # SLA compliance
        0.0,      # queue share
        5 / (8 * 60),  # average utilisation
    )

    assert len(result) == len(expected)
    for r, e in zip(result, expected):
        assert math.isclose(r, e, rel_tol=1e-9)
