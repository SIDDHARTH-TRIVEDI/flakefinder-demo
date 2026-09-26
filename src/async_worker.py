import asyncio
import os
import random


def get_demo_delay():
    seed = os.getenv("FLAKE_DEMO_SEED")

    if seed is not None:
        rng = random.Random(int(seed))
        return rng.uniform(0.0, 0.02)

    return random.uniform(0.0, 0.02)


async def background_update(result):
    delay = get_demo_delay()

    await asyncio.sleep(delay)
    result["ready"] = True


async def process_request():
    result = {"ready": False}

    # BUG: background task is started but not awaited.
    asyncio.create_task(background_update(result))

    # Race window.
    await asyncio.sleep(get_demo_delay())

    return result