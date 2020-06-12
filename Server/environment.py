import numpy as np
from Server.processing import Camera


class Environment(object):
    def __init__(self):
        self.cam = Camera()

    def reset(self):
        _, arr = self.cam.classification()
        return arr
