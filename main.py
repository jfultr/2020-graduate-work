import cv2
import threading
from absl import app, flags
from absl.flags import FLAGS
import tensorflow as tf

from yolov3_tf2.models import (
    YoloV3, YoloV3Tiny
)

flags.DEFINE_integer('num_classes', 80, 'number of classes in the model')
flags.DEFINE_string('classes', './data/coco.names', 'path to classes file')
flags.DEFINE_string('weights', './checkpoints/yolov3.tf',
                    'path to weights file')
flags.DEFINE_integer('size', 416, 'resize images to')

from yolov3_tf2.dataset import transform_images, load_tfrecord_dataset
from yolov3_tf2.utils import draw_outputs


def main(_argv):
    thread = threading.Thread(target=classification)
    thread.start()


def classification():
    yolo = YoloV3(classes=FLAGS.num_classes)

    yolo.load_weights(FLAGS.weights).expect_partial()
    print('weights loaded')

    class_names = [c.strip() for c in open(FLAGS.classes).readlines()]
    print('classes loaded')

    cap = cv2.VideoCapture('http://169.254.104.205:8080/?action=stream')



    while True:
        ret, img_raw = cap.read()
        frame = tf.expand_dims(img_raw, 0)
        frame = transform_images(frame, FLAGS.size)
        boxes, scores, classes, nums = yolo(frame)

        frame = cv2.cvtColor(img_raw, cv2.COLOR_BGR2GRAY)
        frame = draw_outputs(frame, (boxes, scores, classes, nums), class_names)

        cv2.imshow('gray', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def lol_loop():
    while True:
        print('lol')


if __name__ == '__main__':
    app.run(main)
