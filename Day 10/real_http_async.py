import asyncio
import time
import httpx

URLS = [
    "https://api.github.com",
    "https://api.github.com",
    "https://api.github.com",
]

async def fetch(client, url):
    """One real request. `await` pauses HERE while the network is busy."""
    print(f"  start  {url}")
    response = await client.get(url)      # non-blocking network wait
    response.raise_for_status()
    print(f"  done   {url}  ({response.status_code})")
    return response.status_code


async def fetch_sequentially(client):
    """await each request, then the next -> waits add up (~3s)."""
    print("Sequential (await one at a time):")
    start = time.perf_counter()
    for url in URLS:
        await fetch(client, url)
    print(f"  -> took {time.perf_counter() - start:.2f}s\n")


async def fetch_concurrently(client):
    """gather starts all requests, then waits once -> ~1s (the slowest one)."""
    print("Concurrent (asyncio.gather):")
    start = time.perf_counter()
    await asyncio.gather(*(fetch(client, url) for url in URLS))   # * unpacks the list
    print(f"  -> took {time.perf_counter() - start:.2f}s\n")


async def main():
    # One client, reused for every request (opens/reuses connections efficiently).
    async with httpx.AsyncClient(timeout=20) as client:
        await fetch_sequentially(client)
        await fetch_concurrently(client)
    print("Real network calls -- same overlap trick as the fake ones.")


asyncio.run(main())


