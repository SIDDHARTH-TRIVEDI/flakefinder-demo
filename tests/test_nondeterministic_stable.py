from src.nondeterministic import get_system_value, is_valid_value


def test_system_value_is_integer():
    value = get_system_value()
    assert isinstance(value, int)


def test_system_value_is_in_expected_range():
    value = get_system_value()
    assert 1 <= value <= 10


def test_valid_value_returns_boolean():
    result = is_valid_value()
    assert isinstance(result, bool)


def test_seeded_value_is_reproducible():
    import os

    old_seed = os.environ.get("FLAKE_DEMO_SEED")

    try:
        os.environ["FLAKE_DEMO_SEED"] = "5"

        first = get_system_value()
        second = get_system_value()

        assert first == second
    finally:
        if old_seed is None:
            os.environ.pop("FLAKE_DEMO_SEED", None)
        else:
            os.environ["FLAKE_DEMO_SEED"] = old_seed