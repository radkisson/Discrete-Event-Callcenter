from call import calls
from filter import (
    first_level,
    second_level,
    sort_by_work_time,
    first_level2,
    second_level2,
    sort_by_work_time2,
    first_level3,
    second_level3,
    sort_by_work_time3,
)
from worker import workers, workers2, workers3
from data import tSLA, team_size  # Imported data

professionals = 0
helpers = 0
waiting = 0  # Counters to track call handling statistics

for k in range(len(calls)):
    call_item = calls[k]
    call_type = call_item.department + 1  # departments are 1-indexed
    primary_workers = first_level(call_type)  # specialized agents
    primary_workers = sort_by_work_time(primary_workers)
    secondary_workers = second_level(call_type)  # helper agents
    secondary_workers = sort_by_work_time(secondary_workers)
    attended = 0
    for i in range(len(primary_workers)):
        if primary_workers[i].is_free(call_item) == 1:
            primary_workers[i].schedule.append(call_item)
            primary_workers[i].schedule[-1].handle_time = call_item.time
            attended = 1
            professionals = professionals + 1
            break  # Stop until next call arrives
        else:  # No specialized agent is free
            continue
    if attended == 0:
        for i in range(len(secondary_workers)):
            if secondary_workers[i].is_free(call_item) == 1:
                secondary_workers[i].schedule.append(call_item)
                secondary_workers[i].schedule[-1].handle_time = call_item.time
                attended = 1
                helpers = helpers + 1
                break  # Stop until next call arrives
            else:  # No agent is free so the call waits in queue
                continue
    if attended == 1:
        continue
    if attended == 0:  # Call waits in the queue
        concat = []
        for i in range(len(primary_workers)):
            concat.append(primary_workers[i])
        for j in range(len(secondary_workers)):
            concat.append(secondary_workers[j])
        concat = sort_by_work_time(concat)
        waiting = waiting + 1
        call_item.handle_time = concat[0].next_available()
        concat[0].schedule.append(call_item)
        
print(professionals)
print(helpers)
print(waiting)

def SL():  # Percentage of calls that waited less than 5 minutes in queue
    count = 0
    for i in range(len(calls)):
        if calls[i].wait_time() < 5:
            count = count + 1
    return count / len(calls)

def ASA():  # Share of calls solved within the SLA once answered
    count = 0
    for i in range(len(calls)):
        j = int(calls[i].department)
        if calls[i].handle_time + calls[i].duration - calls[i].time < tSLA[j]:
            count = count + 1
    return count / len(calls)

def INVASA():
    return 1 - ASA()

def p_wait_queue():  # Fraction of calls that had to wait in queue
    count = 0
    for i in range(len(calls)):
        if calls[i].wait_time() > 0:
            count = count + 1
    return count / len(calls)

def average_work_time():  # Average worker utilisation
    total_work = 0
    for idx in range(len(workers)):
        total_work = total_work + workers[idx].work_time()
    total_work = total_work / (len(workers) * 8 * 60)
    return total_work

print('{}'.format(SL()))
print('{}'.format(ASA()))
print('{}'.format(p_wait_queue()))
print('{}'.format(average_work_time()))
