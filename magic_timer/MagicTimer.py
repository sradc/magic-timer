import time
from magic_timer.format_output import format_output


SECS_IN_DAY = 24 * 60 * 60
SECS_IN_HOUR = 60 * 60
SECS_IN_MIN = 60

GET_TIME = time.monotonic  # func returns time in secs

class MagicTimer:

    def __init__(self, t_zero=None):
        
        if t_zero:
            self.t_zero = t_zero
        else:
            self.t_zero = GET_TIME()

    def delta(self):
        "Return time elapsed in seconds"
        return GET_TIME() - self.t_zero

    def __str__(self):
        "Format self.delta into an appropriately readable string."
        return format_output(delta=self.delta())

    def __repr__(self):
        return "{}(t_zero={})".format(__class__.__name__, self.t_zero)
    
    def time_elapsed(self):
        """
        Return elapsed time in -
        days, hours, minutes, seconds, milliseconds, microseconds
        """
        delta = self.delta()

        days = int(delta / SECS_IN_DAY)
        remainder = delta - days * SECS_IN_DAY

        hours = int(remainder / SECS_IN_HOUR)
        remainder -= hours * SECS_IN_HOUR

        minutes = int(remainder / SECS_IN_MIN)
        remainder -= minutes * SECS_IN_MIN

        seconds = int(remainder)
        remainder -= seconds

        milliseconds = int(remainder * 1000)
        remainder -= milliseconds / 1000

        microseconds = int(remainder * 1000_000)

        return days, hours, minutes, seconds, milliseconds, microseconds


if __name__ == "__main__":
    t = MagicTimer()
    print(t)
