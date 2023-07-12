import asyncio
import aiohttp
import time

urls = []
for i in range(100):
    text = f'https://hh.ru/vacancy/82850{i+817}'
    urls.append(text)


async def parse_url(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text_link = await response.text()
    file_name = f'parsed/async/parse_{url[8:].replace("/", "_")}.html'
    with open(file_name, "w", encoding="utf-8") as f_out:
        f_out.write(text_link)


async def main():
    tasks = []
    start_time = time.time()
    for url in urls:
        task = asyncio.ensure_future(parse_url(url,))
        tasks.append(task)
    await asyncio.gather(*tasks)
    print(f'Finished! Time: {time.time() - start_time:.2f} seconds')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
