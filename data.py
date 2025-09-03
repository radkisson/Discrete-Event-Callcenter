
"""Generate the random input matrices used by the simulator.

This module constructs the synthetic call-arrival and worker-skill data used
throughout the project.  NumPy is employed to draw samples from exponential
distributions so that each run produces a slightly different workload.  The
output consists of a matrix of incoming calls (:data:`call_input_list`) as well
as several worker skill matrices (:data:`skill_matrix_a`, :data:`skill_matrix_b`,
:data:`skill_matrix_c`).  These
variables are imported by :mod:`call` and :mod:`worker` when building their
respective objects.  Constants defined here are treated as the default inputs
for the simulation engine.
"""

import numpy as np
import numpy.random as rnd  # used to generate random numbers
import helpers


team_size = np.array([5, 3, 4, 3])  # Number of workers per department
work_hours = 8  # Working hours per day
total_minutes = work_hours * 60  # Total work time in minutes
department_ratio = np.array([.35, .18, .25, .22])  # Department workload proportions
max_calls = [200, 180, 270, 110]  # Maximum calls per department
sla_targets = np.array([18.0, 12.0, 10.0, 25.0])  # SLA target per department
incoming_calls = np.array([180, 160, 250, 95])  # Incoming calls per department

skill_matrix_a = np.hstack(
    [
        np.array([
            1,
            2,
            1,
            3,
            1,
            0,
            1,
            0,
            1,
            0,
            2,
            4,
            2,
            1,
            2,
            0,
            3,
            1,
            3,
            4,
            3,
            0,
            3,
            0,
            4,
            3,
            4,
            2,
            4,
            0,
        ]).reshape(15, 2),
        np.zeros([15, 2]),
    ]
)
skill_matrix_b = np.hstack(
    [
        np.array([
            1,
            0,
            1,
            0,
            1,
            0,
            1,
            0,
            1,
            0,
            2,
            0,
            2,
            0,
            2,
            0,
            3,
            0,
            3,
            0,
            3,
            0,
            3,
            0,
            4,
            0,
            4,
            0,
            4,
            0,
        ]).reshape(15, 2),
        np.zeros([15, 2]),
    ]
)
skill_matrix_c = np.hstack(
    [
        np.array([
            1,
            2,
            1,
            3,
            1,
            0,
            1,
            0,
            1,
            0,
            2,
            4,
            2,
            1,
            2,
            0,
            3,
            1,
            3,
            4,
            3,
            0,
            3,
            0,
            4,
            3,
            4,
            2,
            4,
            0,
        ]).reshape(15, 2),
        np.zeros([15, 2]),
    ]
)


total_workers = team_size.sum()  # Total number of workers
work_minutes_department = total_minutes * team_size  # Work minutes per department
total_work_minutes = work_minutes_department.sum()  # Total amount of work in minutes
minutes_per_dept = department_ratio * total_work_minutes  # Minutes assigned to each department
average_call_time = [minutes_per_dept[i] * pow(max_calls[i], -1) for i in range(4)]  # Average handling time per call
arrival_rate = incoming_calls / total_minutes  # Arrival rate per minute

arrivals = np.array([
    rnd.exponential(1 / arrival_rate[i], incoming_calls[i]) for i in range(4)
], dtype=object)  # Call arrival times
arrival_times = np.array([
    np.array([arrivals[j][0:i].sum() for i in range(max_calls[j])])
    for j in range(4)
], dtype=object)  # Cumulated arrival times
call_durations = np.array([
    rnd.exponential(average_call_time[i], incoming_calls[i]) for i in range(4)
], dtype=object)  # Call durations
call_durations_cum = np.array([
    np.array([call_durations[j][0:i].sum() for i in range(max_calls[j])])
    for j in range(4)
], dtype=object)

# Matrix of incoming calls per department (time, duration, type, SLA)

all_calls = np.array(
    [
        np.array(
            [
                np.array([
                    arrival_times[i][j],
                    call_durations[i][j],
                    i,
                    sla_targets[i],
                ])
                for j in range(incoming_calls[i])
            ]
        )
        for i in range(4)
    ],
    dtype=object,
)

# Proportion of calls that will miss the SLA even if answered immediately

overSLA = np.zeros(4)  # Initialize result list

for group in range(4):
    over_sla_count = 0
    for call_idx in range(incoming_calls[group]):
        if all_calls[group][call_idx][1] > all_calls[group][call_idx][3]:
            over_sla_count = over_sla_count + 1
    overSLA[group] = over_sla_count / max_calls[group]  # Ratio of calls that exceed the SLA


call_matrix = np.concatenate((all_calls[0], all_calls[1], all_calls[2], all_calls[3]), axis=0)  # Join all departments

call_input_list = np.sort(
    call_matrix.view("float,float,float,float"), order=["f0"], axis=0
)  # Sorted call matrix by arrival time
