from magic_timer import MagicTimer
import time


def my_slow_function(t):
    time.sleep(t)


def test_MagicTimer():

    timer = MagicTimer()
    my_slow_function(2)
    assert str(timer)[:-3] == "0:00:00:02:"

    timer = MagicTimer()
    my_slow_function(.5)
    assert str(timer)[:-2] == "0:00:00:00:5"
