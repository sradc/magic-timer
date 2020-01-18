from functools import wraps
from magic_timer.MagicTimer import MagicTimer


def magic_timer(func):
    """
    Use this decorator to turn a function into a timed function.
    When the decorated function has finished running,
    its runtime will be printed.
    """

    @wraps(func)
    def wrapped_function(*args, **kwargs):
        
        timer = MagicTimer()

        y = func(*args, **kwargs)

        s = "'{}' -".format(func.__name__)
        print(s, timer)

        return y

    return wrapped_function
