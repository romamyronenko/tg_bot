import pytest

from bull_and_cows import get_bulls_and_cows


@pytest.mark.parametrize(
    "secret, guess, expected_result",
    [
        ('3333', '3333', {'bulls': 4, 'cows': 0}),
        ('1234', '9294', {'bulls': 2, 'cows': 0}),
        ('1234', '9876', {'bulls': 0, 'cows': 0}),
        ('1234', '4321', {'bulls': 0, 'cows': 4}),
        ('1231', '9199', {'bulls': 0, 'cows': 1}),
        ('9199', '1231', {'bulls': 0, 'cows': 1}),
        ('9999', '1111', {'bulls': 0, 'cows': 0}),
    ]
)
def test_get_bulls_and_cows(secret, guess, expected_result):
    res = get_bulls_and_cows(secret, guess)

    assert res == expected_result, res
