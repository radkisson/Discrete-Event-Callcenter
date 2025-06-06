from data import call_input_list

class Call:
    """Simple representation of an incoming call."""

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
        """Return the time this call waited in queue."""
        return self.handle_time - self.time

# Build the list of calls using the generated input matrix
calls = [
    Call(call_input_list[i][0][0], call_input_list[i][0][1],
         call_input_list[i][0][2], call_input_list[i][0][3])
    for i in range(len(call_input_list))
]
