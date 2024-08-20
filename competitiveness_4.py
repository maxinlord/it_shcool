import aiohttp
import asyncio

async def fetch(session, url):
    """Отправляет GET-запрос по указанному URL и возвращает статус ответа."""
    async with session.get(url) as response:
        return response.status

async def bound_fetch(semaphore, session, url):
    """Оборачивает запрос в семафор для ограничения одновременных запросов."""
    async with semaphore:
        status = await fetch(session, url)
        return status

async def run_requests(url, total_requests, max_concurrent_requests):
    """Запускает асинхронные запросы и записывает результаты в файл."""
    semaphore = asyncio.Semaphore(max_concurrent_requests)
    statuses = []

    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(total_requests):
            task = asyncio.create_task(bound_fetch(semaphore, session, url))
            tasks.append(task)
        
        # Сбор всех результатов
        for task in asyncio.as_completed(tasks):
            status = await task
            statuses.append(status)

    # Запись статусов в файл
    with open('statuses.txt', 'w') as f:
        for status in statuses:
            f.write(f"Status: {status}\n")

    # Проверка на количество запросов
    assert len(statuses) == total_requests, "Количество полученных статусов не соответствует количеству запросов."

if __name__ == "__main__":
    url = "https://example.com/"
    total_requests = 50
    max_concurrent_requests = 10

    asyncio.run(run_requests(url, total_requests, max_concurrent_requests))
    print("Все запросы завершены и результаты записаны в файл")

