from magic_timer import format_seconds


def test_format_seconds():
    assert format_seconds(365*24*60*60) == "365 days"
    assert format_seconds(2*24*60*60) == "2.0 days"
    assert format_seconds(4.2*60*60) == "4.2 hours"
    assert format_seconds(3.11*60) == "3.2 minutes"
    assert format_seconds(45.38) == "46 seconds"
    assert format_seconds(.334) == "334 milliseconds"
    assert format_seconds(.00008422) == "85 microseconds"
    assert format_seconds(.000001) == "1.0 microseconds"
    assert format_seconds(.0) == "t < 1 microseconds"
