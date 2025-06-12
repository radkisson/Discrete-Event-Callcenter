# Helper functions to select specialized and helper agents

"""Utility helpers for filtering and ordering worker lists.

The functions in this module act on sequences of workers and are used by
the simulation engine to select the best agent for a given call.  Only two
basic pieces of information are required from a worker: its skill level for
a department and the amount of work already assigned.
"""

from typing import List, Protocol


class WorkerProtocol(Protocol):
    def skill_for(self, number: int) -> int: ...

    def work_time(self) -> int: ...


def workers_by_skill(worker_list: List[WorkerProtocol], number: int) -> List[WorkerProtocol]:
    """Return ``worker_list`` ordered by skill for ``number``.

    Parameters
    ----------
    worker_list : List[WorkerProtocol]
        Sequence of workers to sort.
    number : int
        Department identifier to look the skill up for.

    Returns
    -------
    List[WorkerProtocol]
        New list sorted from highest to lowest skill level.
    """
    return sorted(worker_list, key=lambda x: x.skill_for(number), reverse=True)


def first_level(worker_list: List[WorkerProtocol], department: int) -> List[WorkerProtocol]:
    """Return specialists for ``department``.

    Parameters
    ----------
    worker_list : List[WorkerProtocol]
        Workers to filter.
    department : int
        Department number using one-based indexing.

    Returns
    -------
    List[WorkerProtocol]
        Only those workers whose skill is ``8`` for the requested department,
        sorted from most to least busy.
    """
    ordered = workers_by_skill(worker_list, department)
    return [worker for worker in ordered if worker.skill_for(department) == 8]


def second_level(worker_list: List[WorkerProtocol], department: int) -> List[WorkerProtocol]:
    """Return helper agents for ``department``.

    Parameters
    ----------
    worker_list : List[WorkerProtocol]
        Worker population to search.
    department : int
        Department identifier using one-based indexing.

    Returns
    -------
    List[WorkerProtocol]
        Workers with intermediate skill (between 5 and 7) for the given
        department sorted from most to least busy.
    """
    ordered = workers_by_skill(worker_list, department)
    return [worker for worker in ordered if 5 <= worker.skill_for(department) <= 7]


def sort_by_work_time(worker_list: List[WorkerProtocol]) -> List[WorkerProtocol]:
    """Return ``worker_list`` ordered by current workload.

    Parameters
    ----------
    worker_list : List[WorkerProtocol]
        Workers to sort by utilisation.

    Returns
    -------
    List[WorkerProtocol]
        New list sorted from least to most busy.
    """
    ordered = sorted(worker_list, key=lambda x: x.work_time(), reverse=True)
    ordered.reverse()
    return ordered
