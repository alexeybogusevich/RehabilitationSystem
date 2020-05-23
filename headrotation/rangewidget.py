#  !/usr/bin/env python
#
#  Created by Dmytro Kotsur on 9/22/19, 5:38 PM.
#  Copyright (c) 2019 Dmytro Kotsur. All rights reserved.

from PyQt5 import QtWidgets


class RangeWidget(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        super(RangeWidget, self).__init__(parent)

        from rangewidget_ui import Ui_Range
        self.ui = Ui_Range()
        self.ui.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = RangeWidget()
    w.show()
    app.exec()
