from magic_timer import magic_timer
import time


@magic_timer
def my_slow_function(t):
    time.sleep(t)

def test_magic_timer(capsys):

    my_slow_function(1.95)
    captured = capsys.readouterr()
    assert (captured.out.strip() ==
            "'{}' - 2.0 seconds"
            .format(my_slow_function.__name__)), "output does not match: {}".format(captured.out)

    my_slow_function(1.41)
    captured = capsys.readouterr()
    assert (captured.out.strip() ==
            "'{}' - 1.5 seconds"
            .format(my_slow_function.__name__)), "output does not match: {}".format(captured.out)


def test_magic_timer_return():
    @magic_timer
    def sqr(x):
        return x*x

    assert sqr(5) == 25, "decorated function not returning value"
