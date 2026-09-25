import asyncio

from src.async_worker import process_request


def test_background_update_completes():
    result = asyncio.run(process_request())

    assert result["ready"] is True