"""Test MagicTimer and ftimer.

(At least for times in the order of 1 second.)
"""
import time
from magic_timer import MagicTimer, ftimer


@ftimer
def sleep(t):
    time.sleep(t)


def test_context_manager():
    with MagicTimer() as timer:
        sleep(1.92)
    assert str(timer) == "2.0 seconds", "timing error"


def test_MagicTimer():
    timer = MagicTimer()
    sleep(1.92)
    assert str(timer) == "2.0 seconds", "timing error"

    timer = MagicTimer()
    sleep(1.03)
    assert str(timer) == "1.1 seconds", "timing error"


def test_MagicTimer_stop():
    timer = MagicTimer()
    sleep(0.01)
    timer.stop()
    t0 = timer.time_elapsed()
    sleep(0.01)
    t1 = timer.time_elapsed()
    assert t0 == t1, "Timer failed to stop"


def test_MagicTimer_stop_start():
    timer = MagicTimer()
    sleep(0.01)
    timer.stop()
    t0 = timer.time_elapsed()
    sleep(0.01)
    t1 = timer.time_elapsed()
    timer.start()
    sleep(0.01)
    t2 = timer.time_elapsed()
    assert t0 == t1, "Timer failed to stop"
    assert t2 > t1, "Time failed to restart"


def test_MagicTimer_history():
    timer = MagicTimer(history=True)
    for _ in range(3):
        sleep(0.01)
        print(timer)
    assert len(timer.str_history) == 3, "Incorrect number of times"
    assert timer.str_history[0] < timer.str_history[1], "Value error"
    assert timer.str_history[1] < timer.str_history[2], "Value error"


def test_ftime(capsys):
    sleep(1.95)
    captured = capsys.readouterr()
    result = captured.out.strip() == f"`sleep` ran in 2.0 seconds."
    assert result, f"Output does not match {captured.out}."

    sleep(1.41)
    captured = capsys.readouterr()
    result = captured.out.strip() == f"`sleep` ran in 1.5 seconds."
    assert result, f"Output does not match {captured.out}."


def test_ftime_return():
    @ftimer
    def sqr(x):
        return x * x

    assert sqr(5) == 25, "Decorated function did not return the correct value."
