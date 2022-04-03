from functools import wraps
import time
from typing import Callable, Union, List

from magic_timer.format_seconds import format_seconds


class MagicTimer:
    """Time things.

    ```python
    t = MagicTimer()
    do_stuff()
    print(t)
    1.4 seconds
    ```
    """

    def __init__(self, history: bool = False) -> None:
        self.start_time_seconds: float = _get_time()  # when the timer was started
        self.stop_time_seconds: float = None  # when the timer was stopped
        self.stopped_delta_seconds: float = 0  # how long the timer has been stopped
        self.str_history: Union[List[float], None] = [] if history else None

    def time_elapsed(self) -> float:
        "Return time_elapsed since timer started, in seconds."
        if self.stop_time_seconds:
            return (
                self.stop_time_seconds
                - self.start_time_seconds
                - self.stopped_delta_seconds
            )
        else:
            return _get_time() - self.start_time_seconds - self.stopped_delta_seconds

    def stop(self) -> None:
        """Stop the timer."""
        self.stop_time_seconds = _get_time()

    def start(self) -> None:
        """Restart a stopped timer."""
        if self.stop_time_seconds:
            self.stopped_delta_seconds += _get_time() - self.stop_time_seconds
            self.stop_time_seconds = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.stop()

    def __str__(self) -> str:
        t = self.time_elapsed()
        if not self.str_history is None:
            self.str_history.append(t)
        return format_seconds(t)

    def __repr__(self) -> str:
        return f"{__class__.__name__}(t_zero={self.start_time_seconds})"


def ftimer(func: Callable) -> Callable:
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


def _get_time() -> float:
    return time.monotonic()
