import asyncio
import os
import random


_demo_rng = None


def get_demo_delay():
    global _demo_rng
    seed = os.getenv("FLAKE_DEMO_SEED")

    if seed is not None:
        if _demo_rng is None:
            _demo_rng = random.Random(int(seed))
        return _demo_rng.uniform(0.0, 0.02)

    _demo_rng = None
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