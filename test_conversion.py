from conversion import celsius_to_fahrenheit
import pytest

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(20) == 68
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("20")