import os
import random


def get_system_value():
    # Real bug: production logic depends on unseeded randomness.
    value = random.randint(1, 10)

    # Demo mode can make the behavior reproducible later.
    seed = os.getenv("FLAKE_DEMO_SEED")
    if seed is not None:
        random.seed(int(seed))
        value = random.randint(1, 10)

    return value


def is_valid_value():
    return get_system_value() >= 5