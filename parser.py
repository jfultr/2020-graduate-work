import requests
import threading
import time


url = 'http://169.254.45.12/html/cam_pic.php'


def catch_path_exception(write_funck):
    def decorated_function(path, content):
        try:
            write_funck(path, content)
        except OSError:
            print('catched!!')
    return decorated_function


@catch_path_exception
def write_img(file_path, content):
    with open(file_path, "wb") as out:
        out.write(content.content)
        out.close()


def main_loop():
    while True:
        start = time.time()
        # time.sleep(0.1)
        p = requests.get(url)
        file_path = 'img.jpg'
        write_img(file_path, p)
        print(start - time.time())


if __name__ == '__main__':
    thread = threading.Thread(target=main_loop).start()
