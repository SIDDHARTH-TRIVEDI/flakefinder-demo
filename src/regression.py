import random


def calculate_total(items):
    total = sum(items)

    # REGRESSION:
    # Random behavior was accidentally introduced here.
    if random.random() < 0.5:
        total += 1

    return total