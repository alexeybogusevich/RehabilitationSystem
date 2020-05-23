#  !/usr/bin/env python
#
#  Created by Dmytro Kotsur on 9/22/19, 2:26 PM.
#  Copyright (c) 2019 Dmytro Kotsur. All rights reserved.

from PyQt5 import QtWidgets


class AnglesWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(AnglesWidget, self).__init__(parent)

        from angleswidget_ui import Ui_Form
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.labeYaw.setStyleSheet("QLabel { color : blue; }")
        self.ui.labePitch.setStyleSheet("QLabel { color : red; }")
        self.ui.labeRoll.setStyleSheet("QLabel { color : green; }")

        self.setRangeWidgetColor(self.ui.widgetYaw.ui, 'blue')
        self.setRangeWidgetColor(self.ui.widgetPitch.ui, 'red')
        self.setRangeWidgetColor(self.ui.widgetRoll.ui, 'green')

        self.setYaw(0)
        self.setPitch(0)
        self.setRoll(0)

    def setRangeWidgetColor(self, widget, color):
        label_obj_list = ['labelLMin', 'labelLMax', 'labelLAvg', 'labelLNum',
                          'labelRMin', 'labelRMax', 'labelRAvg', 'labelRNum']
        for att in dir(widget):
            if att in label_obj_list:
                getattr(widget, att).setStyleSheet("QLabel { color : " + color + "; }")

    def updateRangeLStatistics(self, widget_name, amin, amax, aavg, num):
        widget = getattr(self.ui, 'widget' + widget_name.capitalize()).ui
        widget.labelLMin.setText("{0:.0f}&deg;".format(amin))
        widget.labelLMax.setText("{0:.0f}&deg;".format(amax))
        widget.labelLAvg.setText("{0:.0f}&deg;".format(aavg))
        widget.labelLNum.setText("{0}".format(int(num)))

    def updateRangeRStatistics(self, widget_name, amin, amax, aavg, num):
        widget = getattr(self.ui, 'widget' + widget_name.capitalize()).ui
        widget.labelRMin.setText("{0:.0f}&deg;".format(amin))
        widget.labelRMax.setText("{0:.0f}&deg;".format(amax))
        widget.labelRAvg.setText("{0:.0f}&deg;".format(aavg))
        widget.labelRNum.setText("{0}".format(int(num)))

    def setYaw(self, angle):
        self.ui.labeYaw.setText("{0:.0f} &deg;".format(angle))

    def setPitch(self, angle):
        self.ui.labePitch.setText("{0:.0f} &deg;".format(angle))

    def setRoll(self, angle):
        self.ui.labeRoll.setText("{0:.0f} &deg;".format(angle))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = AnglesWidget()
    w.updateRangeRStatistics("yaw", 0.1, 1.0, 1.0, 10)
    w.setYaw(10.0)
    w.show()
    app.exec()