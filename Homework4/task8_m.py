import multiprocessing
import requests
import time

urls = []
for i in range(100):
    text = f'https://hh.ru/vacancy/82850{i+817}'
    urls.append(text)


def parse_url(url: str):
    response = requests.get(url, headers={'User-Agent': 'test'})
    file_name = f'parsed/multiprocessing/parse_{url[8:].replace("/", "_")}.html'
    with open(file_name, "w", encoding="utf-8") as f_out:
        f_out.write(response.text)


def main():
    processes = []
    start_time = time.time()
    for url in urls:
        process = multiprocessing.Process(target=parse_url, args=(url, ))
        process.start()
        processes.append(process)
    for process in processes:
        process.join()

    print(f'Finished! Time: {time.time() - start_time:.2f} seconds')


if __name__ == '__main__':
    main()
