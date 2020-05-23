#  !/usr/bin/env python
#
#  Created by Dmytro Kotsur on 9/22/19, 11:14 PM.
#  Copyright (c) 2019 Dmytro Kotsur. All rights reserved.

import numpy as np
from PyQt5 import QtCore


class VTracker(QtCore.QObject):

    maximum_found = QtCore.pyqtSignal(float, name="maximumFound")

    def __init__(self, reset_epsilon=25.0, init_epsilon=5.0):
        super(VTracker, self).__init__()
        self.reset_eps = reset_epsilon
        self.init_eps = init_epsilon
        self.track_value = 0.0
        self.initialized = False

    @QtCore.pyqtSlot(float)
    def update(self, value):
        if np.abs(value) < self.init_eps:
            self.initialized = True
            self.track_value = value
        elif self.initialized and np.abs(value) > np.abs(self.track_value):
            self.track_value = value
        elif self.initialized and np.abs(self.track_value - value) > self.reset_eps:
            self.initialized = False
            self.maximum_found.emit(self.track_value)










