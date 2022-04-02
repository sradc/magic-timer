"""Test MagicTimer and ftimer.

(At least for times in the order of 1 second.)
"""
import time
from magic_timer import MagicTimer, ftimer


@ftimer
def sleep(t):
    time.sleep(t)


def test_MagicTimer():
    timer = MagicTimer()
    sleep(1.92)
    assert str(timer) == "2.0 seconds", "timing error"

    timer = MagicTimer()
    sleep(1.03)
    assert str(timer) == "1.1 seconds", "timing error"


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
