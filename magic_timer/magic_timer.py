from functools import wraps
from magic_timer.MagicTimer import MagicTimer


def magic_timer(func):

    @wraps(func)
    def wrapped_function(*args, **kwargs):
        timer = MagicTimer()

        func(*args, **kwargs)

        s = "magic-timer: '{}' -".format(func.__name__)
        print(s, timer)

    return wrapped_function
