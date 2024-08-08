from project import choose_apple_colour
from project import choose_snake_colour
from project import choose_height_and_weight
import pytest
def test_choose_apple_colour():
    with pytest.raises(TypeError):
        choose_apple_colour("pink")

def test_choose_snake_colour():
    with pytest.raises(TypeError):
        choose_snake_colour("xD")

def test_choose_height_and_weight():
    with pytest.raises(ValueError):
        choose_height_and_weight("i")