import pytest
from src.ej2_3_1 import edades

@pytest.mark.parametrize(
    "input_num, expected",
    [
        (3, "has cumplido 1 años.\nhas cumplido 2 años.\nhas cumplido 3 años."),
        (1, "has cumplido 1 años."),
        (2, "has cumplido 1 años.\nhas cumplido 2 años.")
    ]
)
def test_dividir_params(input_num, expected):
    assert edades(input_num) == expected


def test_edades_valueError():
    with pytest.raises(ValueError):
        edades(-3)