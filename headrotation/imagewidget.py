#  !/usr/bin/env python
#
#  Created by Dmytro Kotsur on 9/19/19, 9:18 PM.
#  Copyright (c) 2019 Dmytro Kotsur. All rights reserved.

from PyQt5 import QtWidgets


class ImageWidget(QtWidgets.QLabel):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setScaledContents(True)

    # def hasHeightForWidth(self):
    #     return self.pixmap() is not None
    #
    # def heightForWidth(self, w):
    #     if self.pixmap():
    #         return int(w * (self.pixmap().height() / self.pixmap().width()))
