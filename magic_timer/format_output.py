"""
Format time into a (more) readable string,
by using an appropriate unit, and rounding to 2 significant figures.

Note that 3 digits are still rounded to 2 significant figures, 
e.g. 340 might result from 331.

"""
import math

UNIT_NAME = ["days", "hours", "minutes", "seconds", "milliseconds", "microseconds"]
SECS_IN_UNIT = [24*60*60, 60*60, 60, 1, 1./1000, 1./1000000]


def format_output(delta: float) -> str:
    """
    delta: time in seconds
    return: time in an appropriate unit, rounded to 2 sig figs
    """

    for unit_name, secs_in_unit in zip(UNIT_NAME, SECS_IN_UNIT):
        
        t = delta / secs_in_unit  # t = time in {unit_name}
        
        if int(t) > 0:
            num_whole_digits = len(str(int(t)))  # num digits to left of decimal point

            if num_whole_digits == 1:
                # round up to a single decimal place
                t = math.ceil(10 * t) / 10  
                return "{:.1f} {}".format(t, unit_name)

            elif num_whole_digits == 2:
                # round up to whole numbers
                t = math.ceil(t)
                return "{:.0f} {}".format(t, unit_name)
            
            elif num_whole_digits == 3:
                # round up the 3rd digit
                # (not sure whether to do this, or just leave as 3 sig figures..)
                t = math.ceil(t / 10) * 10
                return "{} {}".format(t, unit_name)

            else:
                assert False, 'error, should not have more than 3 digits to left of decimal point'

    return "t < 0.05 {}".format(UNIT_NAME[-1])


if __name__ == "__main__":
    # Checking the outputs:

    print(format_output(365*24*60*60))
    print(format_output(2*24*60*60))
    print(format_output(4.2*60*60))
    print(format_output(3.11*60))
    print(format_output(45.38))
    print(format_output(.334))
    print(format_output(.00008422))
    print(format_output(.0))
