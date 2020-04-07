from magic_timer import format_output

def test_format_output():
    assert format_output(365*24*60*60) == "370 days"
    assert format_output(2*24*60*60) == "2.0 days"
    assert format_output(4.2*60*60) == "4.2 hours"
    assert format_output(3.11*60) == "3.2 minutes"
    assert format_output(45.38) == "46 seconds"
    assert format_output(.334) == "340 milliseconds"
    assert format_output(.00008422) == "85 microseconds"
    assert format_output(.0) == "t < 0.05 microseconds"
    
