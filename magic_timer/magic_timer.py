import time
from functools import wraps
from magic_timer.format_seconds import format_seconds


class MagicTimer:
    """Time things.

    >>> t = MagicTimer()
    >>> do_stuff()
    >>> print(t)
    1.4 seconds
    """

    def __init__(self, t_zero=None):
        self.t_zero: float = t_zero if t_zero else _get_time()
        self.t_stopped: float = None

    def time_elapsed(self):
        if self.t_stopped:
            return self.t_stopped - self.t_zero
        else:
            return _get_time() - self.t_zero

    def stop(self):
        """Stop the timer."""
        self.t_stopped = _get_time()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

    def __str__(self):
        return format_seconds(self.time_elapsed())

    def __repr__(self):
        return f"{__class__.__name__}(t_zero={self.t_zero})"


def ftimer(func):
    """Use to time a function.

    @ftimer
    def myfunc():
        ...

    >>> myfunc()

    `myfunc` ran in 4.6 seconds.
    """

    @wraps(func)
    def wrapped_function(*args, **kwargs):
        timer = MagicTimer()
        y = func(*args, **kwargs)
        print(f"`{func.__name__}` ran in {timer}.")
        return y

    return wrapped_function


def _get_time():
    return time.monotonic()
