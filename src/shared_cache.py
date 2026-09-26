import os

shared_cache = {
    "user": "clean"
}


def contaminate_cache():
    shared_cache["user"] = "contaminated"


def reset_cache():
    shared_cache["user"] = "clean"


def demo_mode_enabled():
    return os.getenv("FLAKE_DEMO_SEED") is not None