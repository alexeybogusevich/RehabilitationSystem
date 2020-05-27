#  !/usr/bin/env python
#
#  Created by Dmytro Kotsur on 10/21/19, 12:02 AM.
#  Copyright (c) 2019 Dmytro Kotsur. All rights reserved.

from intro_ui import Ui_Form
from PyQt5 import QtWidgets, QtGui
from mainwindow import MainWindow

class LoginWidget(QtWidgets.QWidget):
    def __init__(self):
        super(IntroWidget, self).__init__()

        self.ui = Ui_Form()

class IntroWidget(QtWidgets.QWidget):
    def __init__(self):
        super(IntroWidget, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.toolButtonWebCamera.clicked.connect(self.runWebCam)
        self.ui.toolButtonFile.clicked.connect(self.runFromFile)

    def runWebCam(self):
        class Arg(object):
            input = 0
            no3d = not self.ui.toolButton.isChecked()
            save_video = self.ui.toolButton_3.isChecked()
            show_face = self.ui.toolButton_2.isChecked()

        window = MainWindow(Arg(), parent=self)
        window.destroyed.connect(self.showAgain)
        window.showMaximized()
        self.setVisible(False)

    def runFromFile(self):
        filename, ext = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open video file...", ".", "Video (*.avi *.mp4)"
        )
        if filename == "" or filename is None:
            return
        else:

            class Arg(object):
                input = str(filename)
                no3d = not self.ui.toolButton.isChecked()
                save_video = self.ui.toolButton_3.isChecked()
                show_face = self.ui.toolButton_2.isChecked()

            window = MainWindow(Arg(), parent=self)
            window.destroyed.connect(self.showAgain)
            window.showMaximized()
            self.setVisible(False)

    def showAgain(self):
        self.setVisible(True)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        QtWidgets.QApplication.quit()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    widget = IntroWidget()
    widget.show()
    app.exec()
