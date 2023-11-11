import pytest
from src.ej2_3_3 import contador

@pytest.mark.parametrize(
    "input_num, expected",
    [
        (3, "3,2,1,0"),
        (1, "1,0"),
        (2, "2,1,0")
    ]
)
def test_dividir_params(input_num, expected):
    assert contador(input_num) == expected


def test_contador_valueError():
    with pytest.raises(ValueError):
        contador(-3)