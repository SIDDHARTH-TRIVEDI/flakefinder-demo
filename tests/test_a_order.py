from src.shared_cache import shared_cache


def test_cache_starts_clean():
    assert shared_cache["user"] == "clean"