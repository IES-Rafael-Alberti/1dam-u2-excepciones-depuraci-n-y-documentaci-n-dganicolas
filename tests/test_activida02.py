import pytest
from src.ej2_3_2 import parimpar

@pytest.mark.parametrize(
    "input_num, expected",
    [
        (5, "1,3,5"),
        (1, "1"),
        (2, "1")
    ]
)
def test_parimpar_params(input_num, expected):
    assert parimpar(input_num) == expected


def test_parimpar_valueError():
    with pytest.raises(ValueError):
        parimpar(-3)