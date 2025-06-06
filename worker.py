"""Worker definitions and helpers used by the simulation."""

import itertools  # Helper for constructing the worker matrices
from data import team_size as default_team_size, A, B, C, tSLA  # Matrices generated in data.py

# Define the worker objects

class WorkerType:
    """Model a call-centre agent and their skill set.

    Parameters
    ----------
    department : int
        Department identifier this worker belongs to.
    number : int
        Unique number for the worker inside the department.
    sales, logistics, programming, maintenance : int
        Skill levels for the four departments.  ``8`` represents a specialist
        while lower values denote diminishing ability.
    sla : float
        Service level agreement for this worker's main department.
    """

    def __init__(self, department, number, sales, logistics, programming, maintenance, sla):
        # Basic worker data
        self.department = department  # Department this worker belongs to
        self.number = number  # Worker identifier
        self.schedule = []  # List of handled calls
        self.sales = sales  # Skills per department
        self.logistics = logistics
        self.programming = programming
        self.maintenance = maintenance
        self.sla = sla  # SLA for the department
        self.tracer = "Kaixo"
    
    def __repr__(self):
        """Return a readable representation of the worker."""
        return 'WorkerType: Department {} Number {}'.format(
            self.department, self.number
        )
        
    def next_available(self):  # When will this worker be free?
        """Return the minute when this worker becomes free."""

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
        """Return ``True`` if ``call_obj`` can be handled upon arrival."""

        # A worker with an empty schedule is immediately free
        if self.next_available() == 0:
            return True

        # Otherwise they are free if the last scheduled call finishes before the
        # new call arrives
        if self.next_available() < call_obj.time:
            return True

        return False
        
    def work_time(self):  # Total time this worker has been busy
        """Return total minutes this worker has spent on calls."""

        time = 0
        for i in range(len(self.schedule)):
            time = time + self.schedule[i].duration
        return time
    
    def skill_for(self, number):  # Return the skill value for the given department
        """Return skill level for department ``number`` (1 to 4)."""

        if number == 1:
            return self.sales
        if number == 2:
            return self.logistics
        if number == 3:
            return self.programming
        if number == 4:
            return self.maintenance


def build_worker_list(skill_matrix, team_size=None):
    """Return a list of :class:`WorkerType` built from ``skill_matrix``.

    Parameters
    ----------
    skill_matrix : array-like
        Matrix describing the main and secondary skill of every worker.
    team_size : Sequence[int], optional
        Number of workers per department. When ``None`` the values from
        :data:`data.team_size` are used.

    The matrix encodes the primary and secondary skill for each worker.  This
    helper creates the required :class:`WorkerType` objects and assigns the
    corresponding skill values.
    """

    if team_size is None:
        team_size = default_team_size

    # Create workers for each department according to ``team_size``
    workers: list[WorkerType] = []
    dept = 0
    for size in team_size:
        for number in range(size):
            worker = WorkerType(dept, number, 2, 2, 2, 2, 0)
            if dept < len(tSLA):
                worker.sla = tSLA[dept]
            else:
                worker.sla = 0
            workers.append(worker)
        dept += 1

    # Assign skills using the provided matrix
    for idx, worker in enumerate(workers):
        if skill_matrix[idx, 0] == 1:
            worker.sales = 8
        if skill_matrix[idx, 0] == 2:
            worker.logistics = 8
        if skill_matrix[idx, 0] == 3:
            worker.programming = 8
        if skill_matrix[idx, 0] == 4:
            worker.maintenance = 8

        if skill_matrix[idx, 1] == 1:
            worker.sales = 5
        if skill_matrix[idx, 1] == 2:
            worker.logistics = 5
        if skill_matrix[idx, 1] == 3:
            worker.programming = 5
        if skill_matrix[idx, 1] == 4:
            worker.maintenance = 5

    return workers


# Worker matrices used during the simulation
workers = build_worker_list(A)
workers2 = build_worker_list(B)
workers3 = build_worker_list(C)
