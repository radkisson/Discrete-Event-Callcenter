
import numpy as np
import numpy.random as rnd  # used to generate random numbers
import helpers

# Example matrices of worker skills

# k1 = [8, 6, 2, 1]
# k2 = [8, 2, 6, 2]
# k3 = [8, 2, 1, 1]
# k4 = [8, 2, 1, 1]
# k5 = [8, 1, 2, 2]
# l1 = [2, 8, 2, 6]
# l2 = [6, 8, 1, 2]
# l3 = [1, 8, 1, 1]
# I1 = [6, 1, 8, 2]
# I2 = [1, 2, 8, 6]
# I3 = [2, 2, 8, 1]
# I4 = [1, 2, 8, 1]
# m1 = [2, 2, 6, 8]
# m2 = [2, 6, 2, 8]
# m3 = [1, 2, 2, 8]

# k11 = [8, 2, 2, 1]
# k21 = [8, 2, 1, 2]
# k31 = [8, 2, 1, 1]
# k41 = [8, 2, 1, 1]
# k51 = [8, 1, 2, 2]
# l11 = [2, 8, 2, 2]
# l21 = [1, 8, 1, 2]
# l31 = [1, 8, 1, 1]
# I11 = [1, 1, 8, 2]
# I21 = [1, 2, 8, 1]
# I31 = [2, 2, 8, 1]
# I41 = [1, 2, 8, 1]
# m11 = [2, 2, 1, 8]
# m21 = [2, 1, 2, 8]
# m31 = [1, 2, 2, 8]

# k12 = [8, 2, 6, 1]
# k22 = [8, 3, 1, 6]
# k32 = [8, 6, 1, 1]
# k42 = [8, 2, 1, 1]
# k52 = [8, 1, 2, 2]
# l12 = [2, 8, 2, 6]
# l22 = [5, 8, 1, 2]
# l32 = [1, 8, 6, 1]
# I12 = [1, 6, 8, 2]
# I22 = [6, 2, 8, 1]
# I32 = [2, 2, 8, 6]
# I42 = [1, 2, 8, 1]
# m12 = [2, 2, 6, 8]
# m22 = [5, 1, 2, 8]
# m32 = [1, 6, 2, 8]


team_size = np.array([5, 3, 4, 3])  # Number of workers per department
work_hours = 8  # Working hours per day
total_minutes = work_hours * 60  # Total work time in minutes
department_ratio = np.array([.35, .18, .25, .22])  # Department workload proportions
max_calls = [200, 180, 270, 110]  # Maximum calls per department

# Target resolution time (in minutes) for each department.
# Calls should be solved within this timeframe once answered.
DEPARTMENT_SLA = np.array([18.0, 12.0, 10.0, 25.0])

# Alias kept for backward compatibility with existing imports.
tSLA = DEPARTMENT_SLA
incoming_calls = np.array([180, 160, 250, 95])  # Incoming calls per department

A = np.hstack([np.array([1,2,1,3,1,0,1,0,1,0,2,4,2,1,2,0,3,1,3,4,3,0,3,0,4,3,4,2,4,0]).reshape(15,2),np.zeros([15,2])])
B = np.hstack([np.array([1,0,1,0,1,0,1,0,1,0,2,0,2,0,2,0,3,0,3,0,3,0,3,0,4,0,4,0,4,0]).reshape(15,2),np.zeros([15,2])])
C =  np.hstack([np.array([1,2,1,3,1,0,1,0,1,0,2,4,2,1,2,0,3,1,3,4,3,0,3,0,4,3,4,2,4,0]).reshape(15,2),np.zeros([15,2])])

total_workers = team_size.sum()  # Total number of workers
work_minutes_department = total_minutes * team_size  # Work minutes per department
total_work_minutes = work_minutes_department.sum()  # Total amount of work in minutes
minutes_per_dept = department_ratio * total_work_minutes  # Minutes assigned to each department
average_call_time = [minutes_per_dept[i] * pow(max_calls[i], -1) for i in range(4)]  # Average handling time per call
arrival_rate = incoming_calls / total_minutes  # Arrival rate per minute

arrivals = np.array([rnd.exponential(1 / arrival_rate[i], incoming_calls[i]) for i in range(4)])  # Call arrival times
arrival_times = np.array([np.array([arrivals[j][0:i].sum() for i in range(max_calls[j])]) for j in range(4)])  # Cumulated arrival times
call_durations = np.array([rnd.exponential(average_call_time[i], incoming_calls[i]) for i in range(4)])  # Call durations
call_durations_cum  = np.array([ np.array([call_durations[j][0:i].sum() for i in range(max_calls[j])]) for j in range(4)])

# Matrix of incoming calls per department (time, duration, type, SLA)

all_calls  = np.array(
    [
        np.array([
            np.array([arrival_times[i][j], call_durations[i][j], i, DEPARTMENT_SLA[i]])
            for j in range(incoming_calls[i])
        ])
        for i in range(4)
    ]
)
)

# Proportion of calls that would exceed the SLA even if answered immediately.
# Index corresponds to the department.
overSLA = np.zeros(4)

for group in range(4):
    over_sla_count = 0
    for call_idx in range(incoming_calls[group]):
        if all_calls[group][call_idx][1] > all_calls[group][call_idx][3]:
            over_sla_count = over_sla_count + 1
    overSLA[group] = over_sla_count / max_calls[group]  # Fraction exceeding the SLA


call_matrix = np.concatenate((all_calls[0], all_calls[1], all_calls[2], all_calls[3]), axis=0)  # Join all departments

call_input_list = np.sort(
    call_matrix.view("float,float,float,float"), order=["f0"], axis=0
)  # Sorted call matrix by arrival time
