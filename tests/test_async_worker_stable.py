import asyncio

from src.async_worker import background_update, get_demo_delay


def test_background_update_sets_ready():
    result = {"ready": False}

    async def run():
        await background_update(result)

    asyncio.run(run())

    assert result["ready"] is True


def test_background_update_changes_only_ready():
    result = {"ready": False, "extra": "keep"}

    async def run():
        await background_update(result)

    asyncio.run(run())

    assert result["ready"] is True
    assert result["extra"] == "keep"


def test_demo_delay_is_non_negative():
    delay = get_demo_delay()
    assert delay >= 0


def test_demo_delay_is_below_limit():
    delay = get_demo_delay()
    assert delay < 0.02
