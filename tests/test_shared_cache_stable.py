from src.shared_cache import shared_cache, contaminate_cache, reset_cache


def test_cache_initial_value():
    reset_cache()
    assert shared_cache["user"] == "clean"


def test_cache_can_be_contaminated():
    reset_cache()
    contaminate_cache()
    assert shared_cache["user"] == "contaminated"


def test_cache_can_be_reset():
    contaminate_cache()
    reset_cache()
    assert shared_cache["user"] == "clean"


def test_cache_contains_user_key():
    reset_cache()
    assert "user" in shared_cache