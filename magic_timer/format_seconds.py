'''Turn time in seconds into a readable string.
'''
import math

TIME_UNITS = (  # Ordered from large to small.
    ('days', 24*60*60),
    ('hours', 60*60),
    ('minutes', 60),
    ('seconds', 1),
    ('milliseconds', 1/1000),
    ('microseconds', 1/1000_000),
)


def format_seconds(seconds):
    '''Convert `seconds` into readable string.

    E.g. format_seconds(45.38) -> '46 seconds'
    '''
    try:
        value, unit = _convert_to_appropriate_unit(seconds)
    except ValueError:
        return f't < 1 {TIME_UNITS[-1][0]}'
    value = _round_appropriately(value)
    return f'{value} {unit}'


def _convert_to_appropriate_unit(seconds):
    '''Convert seconds into an appropriate unit from TIME_UNITS.'''
    for unit, seconds_in_unit in TIME_UNITS:
        if seconds >= seconds_in_unit:
            value = seconds / seconds_in_unit
            return value, unit
    raise ValueError('`seconds` is smaller than the smallest time unit.')


def _round_appropriately(value):
    '''Round to at most 1 decimal place.

    Round with math.ceil, since generally better to overestimate the time taken.
    '''
    num_integer_digits = len(str(int(value)))
    if num_integer_digits <= 1:
        return math.ceil(value * 10) / 10
    else:
        return math.ceil(value)


if __name__ == "__main__":
    # Testing the outputs:
    print(format_seconds(84654*24*60*60))
    print(format_seconds(365*24*60*60))
    print(format_seconds(2*24*60*60))
    print(format_seconds(4.2*60*60))
    print(format_seconds(3.11*60))
    print(format_seconds(45.38))
    print(format_seconds(4.58))
    print(format_seconds(.334))
    print(format_seconds(.00008422))
    print(format_seconds(.00000645))
    print(format_seconds(.00000109))
    print(format_seconds(.000001))
    print(format_seconds(.00000064))
    print(format_seconds(.0))
    print(format_seconds(0))
    print(_round_appropriately(0))
