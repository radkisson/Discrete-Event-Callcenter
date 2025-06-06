import os
import sys
import types

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# create dummy data module to satisfy imports
class DummyMatrix:
    def __getitem__(self, idx):
        return 0

sys.modules['data'] = types.SimpleNamespace(
    team_size=[],
    A=DummyMatrix(),
    B=DummyMatrix(),
    C=DummyMatrix(),
    DEPARTMENT_SLA=[],
    tSLA=[],  # backward compatibility
    call_input_list=[],
)

from call import Call
from worker import WorkerType


def test_next_available_single_call():
    worker = WorkerType(0, 0, 0, 0, 0, 0, 0)
    call = Call(0, 5, 0, 10)
    call.handle_time = 3
    worker.schedule.append(call)
    assert worker.next_available() == 8


def test_constructor_stores_sla():
    worker = WorkerType(0, 0, 0, 0, 0, 0, 15)
    assert worker.sla == 15
