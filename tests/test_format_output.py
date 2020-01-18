from magic_timer import format_output

def test_format_output():
    assert format_output(365*24*60*60) == "370 days"
    format_output(2*24*60*60) == "2.0 days"
    format_output(4.2*60*60) == "4.2 hours"
    format_output(3.11*60) == "3.2 minutes"
    format_output(45.38) == "46 seconds"
    format_output(.334) == "340 milliseconds"
    format_output(.00008422) == "85 microseconds"
    format_output(.0) == "t < 0.05 microseconds"
    
