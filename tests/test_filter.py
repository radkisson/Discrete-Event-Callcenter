import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest

from filter import workers_by_skill, first_level, second_level, sort_by_work_time
from department import Department


class DummyCall:
    def __init__(self, duration):
        self.duration = duration


class DummyWorker:
    def __init__(self, skills, work=None):
        self.skills = skills
        self.schedule = [DummyCall(d) for d in (work or [])]

    def skill_for(self, number):
        return self.skills.get(number, 0)

    def work_time(self):
        return sum(call.duration for call in self.schedule)


workers = [
    DummyWorker({Department.PROGRAMMING.value + 1: 5}, [10, 5]),
    DummyWorker({Department.PROGRAMMING.value + 1: 7}, [3]),
    DummyWorker({Department.PROGRAMMING.value + 1: 8}, [20]),
]

workers2 = [
    DummyWorker({Department.SALES.value + 1: 5}),
    DummyWorker({Department.SALES.value + 1: 7}),
    DummyWorker({Department.SALES.value + 1: 8}),
]

workers3 = [
    DummyWorker({Department.LOGISTICS.value + 1: 8}),
    DummyWorker({Department.LOGISTICS.value + 1: 7}),
    DummyWorker({Department.LOGISTICS.value + 1: 8}),
]


def old_first_level(worker_list, department):
    lst = sorted(worker_list, key=lambda x: x.skill_for(department), reverse=True)
    lst.reverse()
    length = len(lst)
    count = 0
    for i in range(length):
        if lst[i].skill_for(department) == 8:
            count += 1
    for _ in range(length - count):
        lst.pop(0)
    lst.reverse()
    return lst


def old_second_level(worker_list, department):
    lst = sorted(worker_list, key=lambda x: x.skill_for(department), reverse=True)
    count = 0
    for i in range(len(lst)):
        skill = lst[i].skill_for(department)
        if skill < 5 or skill > 7:
            count += 1
    while count != 0:
        for i in range(len(lst)):
            skill = lst[i].skill_for(department)
            if skill < 5 or skill > 7:
                lst.pop(i)
                count -= 1
                break
    return lst


class FilterHelperTests(unittest.TestCase):
    def test_workers_by_skill(self):
        dept = Department.SALES.value + 1
        expected = sorted(workers2, key=lambda x: x.skill_for(dept), reverse=True)
        self.assertEqual(workers_by_skill(workers2, dept), expected)

    def test_first_level(self):
        dept = Department.LOGISTICS.value + 1
        self.assertEqual(first_level(list(workers3), dept), old_first_level(list(workers3), dept))

    def test_second_level(self):
        dept = Department.PROGRAMMING.value + 1
        self.assertEqual(second_level(list(workers), dept), old_second_level(list(workers), dept))

    def test_sort_by_work_time(self):
        expected = sorted(workers, key=lambda x: x.work_time(), reverse=True)
        expected.reverse()
        self.assertEqual(sort_by_work_time(list(workers)), expected)


if __name__ == '__main__':
    unittest.main()
