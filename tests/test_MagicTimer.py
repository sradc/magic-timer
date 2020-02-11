from magic_timer import MagicTimer
import time


def my_slow_function(t):
    time.sleep(t)


def test_MagicTimer():

    timer = MagicTimer()
    my_slow_function(1.95)
    assert str(timer) == "2.0 seconds", "timing error"

    timer = MagicTimer()
    my_slow_function(1.03)
    assert str(timer) == "1.1 seconds", "timing error"
