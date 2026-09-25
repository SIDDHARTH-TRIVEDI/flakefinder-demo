from src.shared_cache import shared_cache


def test_modify_shared_cache():
    shared_cache["user"] = "contaminated"
    assert shared_cache["user"] == "contaminated"