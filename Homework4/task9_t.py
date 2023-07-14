import threading
import requests
import time
import sys


def save_img(url: str):
    start_download = time.time()
    response = requests.get(url)
    file_name = url[url.rfind("/") + 1:]
    file_path = f'parsed/threading/{file_name}'
    with open(file_path, "wb") as f_out:
        f_out.write(response.content)
    print(F'file_name: {file_name}, Download complete: {time.time() - start_download:.2f}')


def main(urls: list):
    threads = []
    start_time = time.time()
    for url in urls:
        thread = threading.Thread(target=save_img, args=(url, ))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

    print(f'Finished! Time: {time.time() - start_time:.2f} seconds')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        url_img = sys.argv[1:]
        main(url_img)
    else:
        my_urls = ['https://img.mvideo.ru/Big/30067507bb.jpg',
                   'https://traveltimes.ru/wp-content/uploads/2021/06/8804_ho_00_p_2048x1536.jpg',
                   'http://klublady.ru/uploads/posts/2022-02/1644974969_12-klublady-ru-p-tortikov-foto-12.jpg',
                   'https://proprikol.ru/wp-content/uploads/2020/12/snezhnye-barsy-krasivye-kartinki-56.jpeg',
                   'https://phonoteka.org/uploads/posts/2021-07/1625711813_12-phonoteka-org-p-krasivie-arti-kosmosa-krasivo-12.jpg',
                   ]
        main(my_urls)
