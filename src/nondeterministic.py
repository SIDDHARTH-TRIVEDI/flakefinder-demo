import os
import random


def get_system_value():
    seed = os.getenv("FLAKE_DEMO_SEED")

    if seed is not None:
        rng = random.Random(int(seed))
        return rng.randint(1, 10)

    # Real nondeterministic behavior.
    return random.randint(1, 10)


def is_valid_value():
    return get_system_value() >= 5