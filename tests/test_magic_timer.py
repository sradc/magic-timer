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
            .format(my_slow_function.__name__))

    my_slow_function(.5)
    captured = capsys.readouterr()
    assert (captured.out.strip()[:-2] ==
            "magic-timer: '{}' - 0:00:00:00:5"
            .format(my_slow_function.__name__))
