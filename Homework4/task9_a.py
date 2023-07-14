import asyncio
import aiohttp
import aiofiles
import time
import sys


async def save_img(url: str):
    start_download = time.time()
    file_name = url[url.rfind("/") + 1:]
    file_path = f'parsed/async/{file_name}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                f = await aiofiles.open(file_path, mode='wb')
                await f.write(await response.read())
                await f.close()

    print(F'file_name: {file_name}, Download complete: {time.time() - start_download:.2f}')


async def main(urls: list):
    tasks = []
    start_time = time.time()
    for url in urls:
        task = asyncio.ensure_future(save_img(url, ))
        tasks.append(task)
    await asyncio.gather(*tasks)
    print(f'Finished! Time: {time.time() - start_time:.2f} seconds')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        url_img = sys.argv[1:]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(url_img))
    else:
        my_urls = ['https://img.mvideo.ru/Big/30067507bb.jpg',
                   'https://traveltimes.ru/wp-content/uploads/2021/06/8804_ho_00_p_2048x1536.jpg',
                   'http://klublady.ru/uploads/posts/2022-02/1644974969_12-klublady-ru-p-tortikov-foto-12.jpg',
                   'https://proprikol.ru/wp-content/uploads/2020/12/snezhnye-barsy-krasivye-kartinki-56.jpeg',
                   'https://phonoteka.org/uploads/posts/2021-07/1625711813_12-phonoteka-org-p-krasivie-arti-kosmosa-krasivo-12.jpg',
                   ]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(my_urls))


