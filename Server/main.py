import threading
from absl import app
from Server.processing import Camera


def main(_argv):
    camera = Camera()
    thread = threading.Thread(target=camera.open_view_window())
    thread.start()


if __name__ == '__main__':
    app.run(main)
