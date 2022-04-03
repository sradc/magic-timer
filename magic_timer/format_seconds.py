"""Turn time in seconds into a readable string.
"""
import math
from typing import Union, Tuple

TIME_UNITS = (  # Order matters
    ("days", 24 * 60 * 60),
    ("hours", 60 * 60),
    ("minutes", 60),
    ("seconds", 1),
    ("milliseconds", 1 / 1000),
    ("microseconds", 1 / 1000_000),
)


def format_seconds(seconds: float) -> str:
    """Convert `seconds` into readable string.

    E.g. format_seconds(45.38) -> '46 seconds'
         format_seconds(434) -> '7.3 minutes'
    """
    try:
        value, unit = _convert_to_appropriate_unit(seconds)
    except ValueError:
        return f"t < 1 {TIME_UNITS[-1][0]}"
    value = _round_appropriately(value, unit)
    return f"{value} {unit}"


def _convert_to_appropriate_unit(value_in_seconds: float) -> Tuple[float, str]:
    """Convert `value_in_seconds` into an appropriate unit from TIME_UNITS."""
    for unit, seconds_in_unit in TIME_UNITS:
        if value_in_seconds >= seconds_in_unit:
            value = value_in_seconds / seconds_in_unit
            return value, unit
    raise ValueError("`value_in_seconds` is smaller than the smallest time unit.")


def _round_appropriately(value: float, unit: str) -> Union[int, float]:
    """Round *up* to 2 significant figures
    (except for unit="days", and value>=100, which is just rounded
    to the nearest whole number).

    Round up because it's better to overestimate than underestimate 
    time taken.
    """
    num_integer_digits = len(str(int(value)))
    if num_integer_digits <= 1:
        return math.ceil(value * 10) / 10
    elif num_integer_digits == 2:
        return math.ceil(value)
    elif num_integer_digits == 3:
        if unit == "days":
            return math.ceil(value)
        return math.ceil(value / 10) * 10
    else:
        if unit == "days":
            return math.ceil(value)
        raise ValueError("Should not have more than 3 digits.")
