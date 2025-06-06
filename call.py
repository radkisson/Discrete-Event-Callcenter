"""Create :class:`Call` instances from generated input data.

The data module produces :data:`call_input_list` which contains the arrival
time, duration, department and SLA for every incoming call.  This module wraps
those records into :class:`Call` objects and exposes them as :data:`calls`.
"""

from data import call_input_list

class Call:
    """Representation of a single call arriving to the centre.

    Parameters
    ----------
    time : float
        Minute when the call enters the system.
    duration : float
        Expected handling time in minutes.
    department : int
        Identifier of the department that should serve the call.
    sla : float
        Service Level Agreement (maximum waiting time allowed).
    """

    def __init__(self, time, duration, department, sla):
        # minute when the call arrives
        self.time = time
        # duration of the call in minutes
        self.duration = duration
        # department that should handle the call
        self.department = department
        # service level agreement for the call
        self.sla = sla
        # minute when the call is actually handled
        self.handle_time = 0

    def wait_time(self):
        """Return the time this call waited in queue.

        Returns
        -------
        float
            Minutes between arrival and being handled.
        """
        return self.handle_time - self.time

    def delta_t(self):
        """Return the waiting time before this call was handled.

        Returns
        -------
        float
            Alias for :meth:`wait_time` used by legacy code.
        """
        return self.wait_time()

# Build the list of calls using the generated input matrix
calls = [
    Call(call_input_list[i][0][0], call_input_list[i][0][1],
         call_input_list[i][0][2], call_input_list[i][0][3])
    for i in range(len(call_input_list))
]
