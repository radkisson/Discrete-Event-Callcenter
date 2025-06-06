# Helper functions to select specialized and helper agents

"""Utility helpers for filtering and ordering worker lists."""

from typing import List, Protocol


class WorkerProtocol(Protocol):
    def skill_for(self, number: int) -> int: ...

    def work_time(self) -> int: ...


def workers_by_skill(worker_list: List[WorkerProtocol], number: int) -> List[WorkerProtocol]:
    """Return workers sorted by skill for the given department."""
    return sorted(worker_list, key=lambda x: x.skill_for(number), reverse=True)


def first_level(worker_list: List[WorkerProtocol], department: int) -> List[WorkerProtocol]:
    """Return specialized agents for a given call type."""
    ordered = workers_by_skill(worker_list, department)
    ordered.reverse()
    length = len(ordered)
    count = 0
    for i in range(length):
        if ordered[i].skill_for(department) == 8:  # Skill matrix value 8
            count += 1
    for _ in range(length - count):
        ordered.pop(0)
    ordered.reverse()
    return ordered


def second_level(worker_list: List[WorkerProtocol], department: int) -> List[WorkerProtocol]:
    """Return helper agents for a given call type."""
    ordered = workers_by_skill(worker_list, department)
    count = 0
    for i in range(len(ordered)):
        skill = ordered[i].skill_for(department)
        if skill < 5 or skill > 7:
            count += 1  # Count but do nothing yet
    while count != 0:
        for i in range(len(ordered)):
            skill = ordered[i].skill_for(department)
            if skill < 5 or skill > 7:  # Skill between 5 and 7
                ordered.pop(i)
                count -= 1
                break
    return ordered


def sort_by_work_time(worker_list: List[WorkerProtocol]) -> List[WorkerProtocol]:
    """Return workers sorted by amount of work done."""
    ordered = sorted(worker_list, key=lambda x: x.work_time(), reverse=True)
    ordered.reverse()
    return ordered
