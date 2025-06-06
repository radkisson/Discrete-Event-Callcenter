# Helper functions to select specialized and helper agents
from worker import workers, workers2, workers3  # Import worker lists

def workers_by_skill(number):
    """Return workers sorted by skill for the given department."""
    return sorted(workers, key=lambda x: x.skill_for(number), reverse=True)

def workers_by_skill2(number):
    return sorted(workers2, key=lambda x: x.skill_for(number), reverse=True)

def workers_by_skill3(number):
    return sorted(workers3, key=lambda x: x.skill_for(number), reverse=True)

def first_level(department):
    """Return specialized agents for a given call type."""
    worker_list = workers_by_skill(department)
    worker_list.reverse()
    length = len(worker_list)
    count = 0
    for i in range(length):
        if worker_list[i].skill_for(department) == 8:  # Skill matrix value 8
            count = count + 1
    for j in range(length - count):
        worker_list.pop(0)
    worker_list.reverse()
    return worker_list

def first_level2(department):
    worker_list = workers_by_skill2(department)
    worker_list.reverse()
    length = len(worker_list)
    count = 0
    for i in range(length):
        if worker_list[i].skill_for(department) == 8:  # Skill matrix value 8
            count = count + 1
    for j in range(length - count):
        worker_list.pop(0)
    worker_list.reverse()
    return worker_list

def first_level3(department):
    worker_list = workers_by_skill3(department)
    worker_list.reverse()
    length = len(worker_list)
    count = 0
    for i in range(length):
        if worker_list[i].skill_for(department) == 8:  # Skill matrix value 8
            count = count + 1
    for j in range(length - count):
        worker_list.pop(0)
    worker_list.reverse()
    return worker_list

def second_level(department):
    """Return helper agents for a given call type."""
    worker_list = workers_by_skill(department)
    count = 0
    for i in range(len(worker_list)):
            skill = worker_list[i].skill_for(department)
            if skill < 5 or skill > 7:
                count = count + 1  # Count but do nothing yet
    while count != 0:
        for i in range(len(worker_list)):
            skill = worker_list[i].skill_for(department)
            if skill < 5 or skill > 7:  # Skill between 5 and 7
                worker_list.pop(i)
                count = count - 1
                break
    return worker_list

def second_level2(department):
    worker_list = workers_by_skill2(department)
    count = 0
    for i in range(len(worker_list)):
            skill = worker_list[i].skill_for(department)
            if skill < 5 or skill > 7:
                count = count + 1  # Count but do nothing yet
    while count != 0:
        for i in range(len(worker_list)):
            skill = worker_list[i].skill_for(department)
            if skill < 5 or skill > 7:  # Skill between 5 and 7
                worker_list.pop(i)
                count = count - 1
                break
    return worker_list

def second_level3(department):
    worker_list = workers_by_skill3(department)
    count = 0
    for i in range(len(worker_list)):
            skill = worker_list[i].skill_for(department)
            if skill < 5 or skill > 7:
                count = count + 1  # Count but do nothing yet
    while count != 0:
        for i in range(len(worker_list)):
            skill = worker_list[i].skill_for(department)
            if skill < 5 or skill > 7:  # Skill between 5 and 7
                worker_list.pop(i)
                count = count - 1
                break
    return worker_list

def sort_by_work_time(worker_list):
    """Return workers sorted by amount of work done."""
    ordered = sorted(worker_list, key=lambda x: x.work_time(), reverse=True)
    ordered.reverse()
    return ordered

def sort_by_work_time2(worker_list):
    ordered = sorted(worker_list, key=lambda x: x.work_time(), reverse=True)
    ordered.reverse()
    return ordered

def sort_by_work_time3(worker_list):
    ordered = sorted(worker_list, key=lambda x: x.work_time(), reverse=True)
    ordered.reverse()
    return ordered
