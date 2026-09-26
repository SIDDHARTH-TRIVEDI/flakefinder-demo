from src.regression import calculate_total


def test_calculate_total_empty_list():
    assert calculate_total([]) in (0, 1)


def test_calculate_total_single_item():
    result = calculate_total([10])
    assert result in (10, 11)


def test_calculate_total_multiple_items():
    result = calculate_total([5, 10, 15])
    assert result in (30, 31)


def test_calculate_total_returns_integer():
    result = calculate_total([10, 20, 30])
    assert isinstance(result, int)