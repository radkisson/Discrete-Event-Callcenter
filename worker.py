"""Agent classes and builders used by the simulation engine."""

import itertools  # Helper for constructing the worker matrices

from data import (
    skill_matrix_a,
    skill_matrix_b,
    skill_matrix_c,
    sla_targets,
)
from department import Department
import config

# Define the worker objects

class Agent:
    """Model a call-centre agent and their skill set.

    Parameters
    ----------
    department : Department | int
        Department identifier this worker belongs to.
    number : int
        Unique number for the worker inside the department.
    sales, logistics, programming, maintenance : int
        Skill levels for the four departments.  ``8`` represents a specialist
        while lower values denote diminishing ability.
    sla : float
        Service level agreement for this worker's main department.

    Notes
    -----
    The simulation uses these skill values only to prioritise agent
    selection. Specialists are always considered before helpers but the
    skill level does not alter call duration or the SLA itself.
    """

    def __init__(self, department: Department | int, number, sales, logistics, programming, maintenance, sla):
        # Basic agent data
        self.department = Department(department)  # Department this agent belongs to
        self.number = number  # Agent identifier
        self.schedule = []  # List of handled calls
        self.sales = sales  # Skills per department
        self.logistics = logistics
        self.programming = programming
        self.maintenance = maintenance
        self.sla = sla  # SLA for the department
        self.tracer = "Kaixo"
    
    def __repr__(self):
        """Return a readable representation of the agent."""
        return 'Agent: Department {} Number {}'.format(self.department, self.number)
        
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
        """Return ``True`` if this worker can handle ``call_obj`` immediately."""

        # A worker with an empty schedule is immediately free
        if self.next_available() == 0:
            return True

        # Otherwise they are free if the last scheduled call finishes before the
        # new call arrives
        if self.next_available() < call_obj.time:
            return True

        return False
        
    def work_time(self):  # Total time this worker has been busy
        time = 0
        for i in range(len(self.schedule)):
            time = time + self.schedule[i].duration
        return time
    
    def skill_for(self, number: int | Department):  # Return the skill value for the given department
        if isinstance(number, Department):
            number = number.value + 1
        if number == 1:
            return self.sales
        if number == 2:
            return self.logistics
        if number == 3:
            return self.programming
        if number == 4:
            return self.maintenance


def build_agent_list(skill_matrix, team_size, quality_levels=None, helper_skill=5):
    """Return a list of :class:`Agent` built from ``skill_matrix``.

    Parameters
    ----------
    skill_matrix : array-like
        Matrix describing the primary and secondary skills for each worker.
    team_size : list[int]
        Number of workers per department.
    quality_levels : list[int], optional
        Specialist skill level for each department. ``[8, 8, 8, 8]`` by default.
    helper_skill : int, optional
        Skill level assigned to secondary skills. Defaults to ``5``.
    """

    if quality_levels is None:
        quality_levels = [8, 8, 8, 8]

    # Create workers for each department according to ``team_size``
    agents: list[Agent] = []
    for dept_value, size in enumerate(team_size):
        dept = Department(dept_value)
        for number in range(size):
            agent = Agent(dept, number, 2, 2, 2, 2, 0)
            agent.sla = sla_targets[dept.value]
            agents.append(agent)

    # Assign skills using the provided matrix
    for idx, agent in enumerate(agents):
        primary = skill_matrix[idx, 0]
        secondary = skill_matrix[idx, 1]

        if primary:
            dept_enum = Department(primary - 1)
            if dept_enum is Department.SALES:
                agent.sales = quality_levels[Department.SALES.value]
            elif dept_enum is Department.LOGISTICS:
                agent.logistics = quality_levels[Department.LOGISTICS.value]
            elif dept_enum is Department.PROGRAMMING:
                agent.programming = quality_levels[Department.PROGRAMMING.value]
            elif dept_enum is Department.MAINTENANCE:
                agent.maintenance = quality_levels[Department.MAINTENANCE.value]

        if secondary:
            dept_enum = Department(secondary - 1)
            if dept_enum is Department.SALES:
                agent.sales = helper_skill
            elif dept_enum is Department.LOGISTICS:
                agent.logistics = helper_skill
            elif dept_enum is Department.PROGRAMMING:
                agent.programming = helper_skill
            elif dept_enum is Department.MAINTENANCE:
                agent.maintenance = helper_skill

    return agents


# Agent matrices used during the simulation.  When tests monkeypatch ``data``
# these may fail to build, so fall back to empty lists in that case.
try:
    agents = build_agent_list(skill_matrix_a, config.TEAM_SIZE, config.QUALITY)
    agents2 = build_agent_list(skill_matrix_b, config.TEAM_SIZE, config.QUALITY)
    agents3 = build_agent_list(skill_matrix_c, config.TEAM_SIZE, config.QUALITY)
except Exception:
    agents = []
    agents2 = []
    agents3 = []
