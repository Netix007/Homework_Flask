import threading
import requests
import time


urls = []
for i in range(100):
    text = f'https://hh.ru/vacancy/82850{i+817}'
    urls.append(text)


def parse_url(url: str):
    response = requests.get(url, headers={'User-Agent': 'test'})
    file_name = f'parsed/threading/parse_{url[8:].replace("/", "_")}.html'
    with open(file_name, "w", encoding="utf-8") as f_out:
        f_out.write(response.text)


def main():
    threads = []
    start_time = time.time()
    for url in urls:
        thread = threading.Thread(target=parse_url, args=(url, ))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

    print(f'Finished! Time: {time.time() - start_time:.2f} seconds')


if __name__ == '__main__':
    main()
