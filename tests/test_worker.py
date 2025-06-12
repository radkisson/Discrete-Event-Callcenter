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
    skill_matrix_a=DummyMatrix(),
    skill_matrix_b=DummyMatrix(),
    skill_matrix_c=DummyMatrix(),
    sla_targets=[],
    call_input_list=[],
)

from call import Call
from worker import Agent
from department import Department


def test_next_available_single_call():
    worker = Agent(Department.SALES, 0, 0, 0, 0, 0, 0)
    call = Call(0, 5, Department.SALES, 10)
    call.handle_time = 3
    worker.schedule.append(call)
    assert worker.next_available() == 8
