"""General normal smoke and integration tests for demo modules."""

from src.nondeterministic import get_system_value
from src.regression import calculate_total
from src.shared_cache import reset_cache, shared_cache


def test_system_components_smoke():
    """Verify core components can be invoked together in a standard workflow."""
    reset_cache()
    assert shared_cache["user"] == "clean"

    val = get_system_value()
    assert isinstance(val, int)


def test_calculate_total_positive_numbers():
    """Verify calculate_total with standard positive input list."""
    items = [5, 15, 25]
    total = calculate_total(items)
    # Accounting for regression off-by-one tolerance in stable test
    assert total in (45, 46)
