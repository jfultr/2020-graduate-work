import numpy as np
import Server.processing as processing


class Environment(object):

    def __init__(self):
        pass

    def reset(self):
        arr = np.array([0.1, 0.1, 0.666])
        return arr
