from data import team_size, A, B, C, DEPARTMENT_SLA  # Matrices generated in data.py

# Define the worker objects

class WorkerType:

    def __init__(self, department, number, sales, logistics, programming, maintenance, sla):
        """Create a new worker.

        Parameters
        ----------
        department : int
            Department this worker belongs to.
        number : int
            Worker identifier.
        sales, logistics, programming, maintenance : int
            Skill level for each department.
        sla : float
            SLA goal in minutes for this worker's department.
        """
        # Basic worker data
        self.department = department  # Department this worker belongs to
        self.number = number  # Worker identifier
        self.schedule = []  # List of handled calls
        self.sales = sales  # Skills per department
        self.logistics = logistics
        self.programming = programming
        self.maintenance = maintenance
        # service level agreement for the worker's department
        self.sla = sla
        self.tracer = "Kaixo"
    
    def __repr__(self):
        """Return a readable representation of the worker."""
        return 'WorkerType: Department {} Number {}'.format(
            self.department, self.number
        )
        
    def next_available(self):  # When will this worker be free?
        if len(self.schedule) == 0:
            return 0
        else:
            available = (
                self.schedule[-1].time
                + self.schedule[-1].duration
                + self.schedule[-1].delta_t()
            )
            return available
    
    def is_free(self, call_obj):  # Check if the worker can take the call
        if self.next_available() == 0:
            return 1
        if self.next_available() < call_obj.time:
            return 1
        else:
            return 0
        
    def work_time(self):  # Total time this worker has been busy
        time = 0
        for i in range(len(self.schedule)):
            time = time + self.schedule[i].duration
        return time
    
    def skill_for(self, number):  # Return the skill value for the given department
        if number == 1:
            return self.sales
        if number == 2:
            return self.logistics
        if number == 3:
            return self.programming
        if number == 4:
            return self.maintenance

dept = 0
workers = []  # Initial empty list of workers
for i in team_size:  # Build the first worker list
    for j in range(i):
        workers.append(WorkerType(dept, j, 0, 0, 0, 0, 0))
        workers[-1].sla = DEPARTMENT_SLA[dept]
    dept = dept + 1

for i in range(len(workers)):
    workers[i].sales = 2
    workers[i].logistics = 2
    workers[i].programming = 2
    workers[i].maintenance = 2

for i in range(len(workers)):
    if A[i,0] == 1:
        workers[i].sales = 8
    if A[i,0] == 2:
        workers[i].logistics = 8
    if A[i,0] == 3:
        workers[i].programming = 8
    if A[i,0] == 4:
        workers[i].maintenance = 8
    if A[i,1] == 1:
        workers[i].sales = 5
    if A[i,1] == 2:
        workers[i].logistics = 5
    if A[i,1] == 3:
        workers[i].programming = 5
    if A[i,1] == 4:
        workers[i].maintenance = 5

dept = 0
workers2 = []  # Second worker matrix
for i in team_size:  # Build the second worker list
    for j in range(i):
        workers2.append(WorkerType(dept, j, 0, 0, 0, 0, 0))
        workers2[-1].sla = DEPARTMENT_SLA[dept]
    dept = dept + 1

for i in range(len(workers2)):
    workers2[i].sales = 2
    workers2[i].logistics = 2
    workers2[i].programming = 2
    workers2[i].maintenance = 2

for i in range(len(workers2)):
    if B[i,0] == 1:
        workers2[i].sales = 8
    if B[i,0] == 2:
        workers2[i].logistics = 8
    if B[i,0] == 3:
        workers2[i].programming = 8
    if B[i,0] == 4:
        workers2[i].maintenance = 8
    if B[i,1] == 1:
        workers2[i].sales = 5
    if B[i,1] == 2:
        workers2[i].logistics = 5
    if B[i,1] == 3:
        workers2[i].programming = 5
    if B[i,1] == 4:
        workers2[i].maintenance = 5
    
dept = 0
workers3 = []  # Third worker matrix
for i in team_size:  # Build the third worker list
    for j in range(i):
        workers3.append(WorkerType(dept, j, 0, 0, 0, 0, 0))
        workers3[-1].sla = DEPARTMENT_SLA[dept]
    dept = dept + 1

for i in range(len(workers3)):
    workers3[i].sales = 2
    workers3[i].logistics = 2
    workers3[i].programming = 2
    workers3[i].maintenance = 2

for i in range(len(workers3)):
    if C[i,0] == 1:
        workers3[i].sales = 8
    if C[i,0] == 2:
        workers3[i].logistics = 8
    if C[i,0] == 3:
        workers3[i].programming = 8
    if C[i,0] == 4:
        workers3[i].maintenance = 8
    if C[i,1] == 1:
        workers3[i].sales = 5
    if C[i,1] == 2:
        workers3[i].logistics = 5
    if C[i,1] == 3:
        workers3[i].programming = 5
    if C[i,1] == 4:
        workers3[i].maintenance = 5
