from magic_timer import magic_timer
import time


@magic_timer
def my_slow_function(t):
    time.sleep(t)

def test_magic_timer(capsys):

    my_slow_function(2)
    captured = capsys.readouterr()
    assert (captured.out.strip()[:-3] ==
            "magic-timer: '{}' - 0:00:00:02:"
            .format(my_slow_function.__name__)), "timing error"

    my_slow_function(.5)
    captured = capsys.readouterr()
    assert (captured.out.strip()[:-2] ==
            "magic-timer: '{}' - 0:00:00:00:5"
            .format(my_slow_function.__name__)), "timing error"


@magic_timer
def sqr(x):
    return x*x


def test_magic_timer_return():
    assert sqr(5) == 25, "decorated function return error"

