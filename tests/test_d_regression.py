from src.regression import calculate_total


def test_calculate_total():
    items = [10, 20, 30]
    assert calculate_total(items) == 60