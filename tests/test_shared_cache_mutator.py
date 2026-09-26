from src.shared_cache import contaminate_cache, shared_cache


def test_contaminate_shared_cache():
    """Mutates the module-level shared cache and leaves it contaminated."""
    contaminate_cache()
    assert shared_cache["user"] == "contaminated"
