# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'range.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Range(object):
    def setupUi(self, Range):
        Range.setObjectName("Range")
        Range.resize(134, 89)
        self.verticalLayout = QtWidgets.QVBoxLayout(Range)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.labelRMax = QtWidgets.QLabel(Range)
        self.labelRMax.setMinimumSize(QtCore.QSize(30, 0))
        self.labelRMax.setMaximumSize(QtCore.QSize(30, 16777215))
        self.labelRMax.setTextFormat(QtCore.Qt.RichText)
        self.labelRMax.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRMax.setObjectName("labelRMax")
        self.gridLayout.addWidget(self.labelRMax, 1, 2, 1, 1)
        self.labelRAvg = QtWidgets.QLabel(Range)
        self.labelRAvg.setMinimumSize(QtCore.QSize(30, 0))
        self.labelRAvg.setMaximumSize(QtCore.QSize(30, 16777215))
        self.labelRAvg.setTextFormat(QtCore.Qt.RichText)
        self.labelRAvg.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRAvg.setObjectName("labelRAvg")
        self.gridLayout.addWidget(self.labelRAvg, 2, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(Range)
        self.label_12.setMinimumSize(QtCore.QSize(38, 0))
        self.label_12.setMaximumSize(QtCore.QSize(38, 16777215))
        self.label_12.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(Range)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(38, 0))
        self.label_10.setMaximumSize(QtCore.QSize(38, 16777215))
        self.label_10.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)
        self.labelLAvg = QtWidgets.QLabel(Range)
        self.labelLAvg.setMinimumSize(QtCore.QSize(30, 0))
        self.labelLAvg.setMaximumSize(QtCore.QSize(30, 16777215))
        self.labelLAvg.setTextFormat(QtCore.Qt.RichText)
        self.labelLAvg.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLAvg.setObjectName("labelLAvg")
        self.gridLayout.addWidget(self.labelLAvg, 2, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(Range)
        self.label_14.setMinimumSize(QtCore.QSize(38, 0))
        self.label_14.setMaximumSize(QtCore.QSize(38, 16777215))
        self.label_14.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 2, 0, 1, 1)
        self.labelLMin = QtWidgets.QLabel(Range)
        self.labelLMin.setMinimumSize(QtCore.QSize(30, 0))
        self.labelLMin.setMaximumSize(QtCore.QSize(30, 16777215))
        self.labelLMin.setTextFormat(QtCore.Qt.RichText)
        self.labelLMin.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLMin.setObjectName("labelLMin")
        self.gridLayout.addWidget(self.labelLMin, 0, 1, 1, 1)
        self.labelLMax = QtWidgets.QLabel(Range)
        self.labelLMax.setMinimumSize(QtCore.QSize(30, 0))
        self.labelLMax.setMaximumSize(QtCore.QSize(30, 16777215))
        self.labelLMax.setTextFormat(QtCore.Qt.RichText)
        self.labelLMax.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLMax.setObjectName("labelLMax")
        self.gridLayout.addWidget(self.labelLMax, 1, 1, 1, 1)
        self.labelRMin = QtWidgets.QLabel(Range)
        self.labelRMin.setMinimumSize(QtCore.QSize(30, 0))
        self.labelRMin.setMaximumSize(QtCore.QSize(30, 16777215))
        self.labelRMin.setTextFormat(QtCore.Qt.RichText)
        self.labelRMin.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRMin.setObjectName("labelRMin")
        self.gridLayout.addWidget(self.labelRMin, 0, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(Range)
        self.label_16.setMinimumSize(QtCore.QSize(38, 0))
        self.label_16.setMaximumSize(QtCore.QSize(38, 16777215))
        self.label_16.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 3, 0, 1, 1)
        self.labelLNum = QtWidgets.QLabel(Range)
        self.labelLNum.setMinimumSize(QtCore.QSize(30, 0))
        self.labelLNum.setMaximumSize(QtCore.QSize(30, 16777215))
        self.labelLNum.setTextFormat(QtCore.Qt.RichText)
        self.labelLNum.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLNum.setObjectName("labelLNum")
        self.gridLayout.addWidget(self.labelLNum, 3, 1, 1, 1)
        self.labelRNum = QtWidgets.QLabel(Range)
        self.labelRNum.setMinimumSize(QtCore.QSize(30, 0))
        self.labelRNum.setMaximumSize(QtCore.QSize(30, 16777215))
        self.labelRNum.setTextFormat(QtCore.Qt.RichText)
        self.labelRNum.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRNum.setObjectName("labelRNum")
        self.gridLayout.addWidget(self.labelRNum, 3, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(Range)
        QtCore.QMetaObject.connectSlotsByName(Range)

    def retranslateUi(self, Range):
        _translate = QtCore.QCoreApplication.translate
        Range.setWindowTitle(_translate("Range", "Form"))
        self.labelRMax.setText(_translate("Range", "0°"))
        self.labelRAvg.setText(_translate("Range", "0°"))
        self.label_12.setText(_translate("Range", "макс."))
        self.label_10.setText(_translate("Range", "мін."))
        self.labelLAvg.setText(_translate("Range", "0°"))
        self.label_14.setText(_translate("Range", "сер."))
        self.labelLMin.setText(
            _translate("Range", "<html><head/><body><p>0°</p></body></html>")
        )
        self.labelLMax.setText(_translate("Range", "0°"))
        self.labelRMin.setText(_translate("Range", "0°"))
        self.label_16.setText(_translate("Range", "повт."))
        self.labelLNum.setText(_translate("Range", "0"))
        self.labelRNum.setText(_translate("Range", "0"))
