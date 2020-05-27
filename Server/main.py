import threading
from absl import app
import processing


def main(_argv):
    thread = threading.Thread(target=processing.classification)
    thread.start()


if __name__ == '__main__':
    app.run(main)
