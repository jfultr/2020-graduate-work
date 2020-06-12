import cv2
from absl import flags
from absl.flags import FLAGS
import tensorflow as tf
import time
import numpy as np
import Server.client as client

from yolov3_tf2.models import (
    YoloV3, YoloV3Tiny
)

from yolov3_tf2.dataset import transform_images, load_tfrecord_dataset
from yolov3_tf2.utils import draw_outputs

flags.DEFINE_integer('num_classes', 80, 'number of classes in the model')
flags.DEFINE_string('classes', './data/coco.names', 'path to classes file')
flags.DEFINE_string('weights', './checkpoints/yolov3.tf',
                    'path to weights file')
flags.DEFINE_integer('size', 416, 'resize images to')
flags.DEFINE_string('url', 'http://169.254.49.227:8080/?action=snapshot', 'url to stream')


class Camera(object):
    def __init__(self):
        self.yolo = YoloV3(classes=FLAGS.num_classes)
        self.yolo.load_weights(FLAGS.weights).expect_partial()
        print('weights loaded')
        self.class_names = [c.strip() for c in open(FLAGS.classes).readlines()]
        print('classes loaded')
        self.cap = cv2.VideoCapture()
        self.angles_changed = False

    def open_view_window(self):
        prev_angles = 0
        while True:
            start = time.time()
            ret, img_raw = self.get_img_from_url()
            if ret:
                frame, boxes, scores, classes, nums = self.classification()
                if np.any(classes == 41):
                    angles = '0,0,0,0,600,600'
                else:
                    angles = '0,0,0,0,200,200'

                if angles != prev_angles:
                    self.angles_changed = True
                    print('lol')

                if self.angles_changed:
                    self.angles_changed = False
                    print(angles)
                    client.set_angles(angles)

                prev_angles = angles
                cv2.imshow('gray', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            print(time.time() - start)

        self.cap.release()
        cv2.destroyAllWindows()

    def classification(self):
        _, img_raw = self.get_img_from_url()
        frame = tf.expand_dims(img_raw, 0)
        frame = transform_images(frame, FLAGS.size)
        boxes, scores, classes, nums = self.yolo(frame)

        frame = cv2.cvtColor(img_raw, cv2.COLOR_BGR2GRAY)
        frame = draw_outputs(frame, (boxes, scores, classes, nums), self.class_names)
        return frame, boxes, scores, classes, nums

    def get_img_from_url(self):
        self.cap = cv2.VideoCapture(FLAGS.url)
        ret, img_raw = self.cap.read()
        return ret, img_raw
