#  !/usr/bin/env python
#
#  Created by Dmytro Kotsur on 9/19/19, 9:16 PM.
#  Copyright (c) 2019 Dmytro Kotsur. All rights reserved.

import numpy as np
from PyQt5 import QtGui


def toQImage(img):
    sz = img.shape
    bytes_per_line = sz[1] * 3
    rgb = img.copy()
    rgb = rgb.astype(np.uint8)
    rgb[..., 0], rgb[..., 2] = rgb[..., 2], rgb[..., 0]
    return QtGui.QImage(rgb.data, sz[1], sz[0], bytes_per_line, QtGui.QImage.Format_RGB888)
