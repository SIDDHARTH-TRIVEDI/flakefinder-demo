import asyncio
import os
import random


async def background_update(result):
    delay = random.uniform(0.0, 0.02)

    seed = os.getenv("FLAKE_DEMO_SEED")
    if seed is not None:
        random.seed(int(seed))
        delay = random.uniform(0.0, 0.02)

    await asyncio.sleep(delay)
    result["ready"] = True


async def process_request():
    result = {"ready": False}

    # BUG: the background task is started but never awaited.
    asyncio.create_task(background_update(result))

    # The function returns before the background task is guaranteed
    # to complete.
    await asyncio.sleep(random.uniform(0.0, 0.02))

    return result