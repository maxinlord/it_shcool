import aiohttp
import asyncio

async def fetch(session, url):
    """Отправляет запрос по указанному URL и возвращает статус ответа."""
    async with session.get(url) as response:
        return response.status

async def bound_fetch(semaphore, session, url):
    """Оборачивает запрос в семафор для ограничения одновременных запросов."""
    async with semaphore:
        status = await fetch(session, url)
        print(f"Status: {status} from {url}")
        return status

async def run_requests(url, max_requests):
    semaphore = asyncio.Semaphore(max_requests)
    
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(20):
            task = asyncio.create_task(bound_fetch(semaphore, session, url))
            tasks.append(task)
        
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    url = "http://google.com"
    max_requests = 10  # Ограничение на 10 запросов одновременно
    asyncio.run(run_requests(url, max_requests))
