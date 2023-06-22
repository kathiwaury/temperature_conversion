from conversion import celsius_to_fahrenheit

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(20) == 68
    assert celsius_to_fahrenheit("20") is None