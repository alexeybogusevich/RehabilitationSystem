# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'intro.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(568, 394)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/open/icons/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        Form.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem)
        self.toolButton = QtWidgets.QToolButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.toolButton.setFont(font)
        self.toolButton.setCheckable(True)
        self.toolButton.setChecked(True)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.toolButton_3 = QtWidgets.QToolButton(Form)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.toolButton_3.setFont(font)
        self.toolButton_3.setCheckable(True)
        self.toolButton_3.setChecked(True)
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout.addWidget(self.toolButton_3)
        self.toolButton_2 = QtWidgets.QToolButton(Form)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setCheckable(True)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout.addWidget(self.toolButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toolButtonWebCamera = QtWidgets.QToolButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.toolButtonWebCamera.sizePolicy().hasHeightForWidth()
        )
        self.toolButtonWebCamera.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(32)
        self.toolButtonWebCamera.setFont(font)
        self.toolButtonWebCamera.setFocusPolicy(QtCore.Qt.TabFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/open/icons/cam.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.toolButtonWebCamera.setIcon(icon1)
        self.toolButtonWebCamera.setIconSize(QtCore.QSize(256, 256))
        self.toolButtonWebCamera.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButtonWebCamera.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButtonWebCamera.setAutoRaise(False)
        self.toolButtonWebCamera.setArrowType(QtCore.Qt.NoArrow)
        self.toolButtonWebCamera.setObjectName("toolButtonWebCamera")
        self.horizontalLayout_2.addWidget(self.toolButtonWebCamera)
        self.toolButtonFile = QtWidgets.QToolButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.toolButtonFile.sizePolicy().hasHeightForWidth()
        )
        self.toolButtonFile.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(32)
        self.toolButtonFile.setFont(font)
        self.toolButtonFile.setFocusPolicy(QtCore.Qt.TabFocus)
        self.toolButtonFile.setIcon(icon)
        self.toolButtonFile.setIconSize(QtCore.QSize(256, 256))
        self.toolButtonFile.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButtonFile.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButtonFile.setAutoRaise(False)
        self.toolButtonFile.setArrowType(QtCore.Qt.NoArrow)
        self.toolButtonFile.setObjectName("toolButtonFile")
        self.horizontalLayout_2.addWidget(self.toolButtonFile)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MUAE Source Type..."))
        self.toolButton.setText(_translate("Form", "3D"))
        self.toolButton_3.setText(_translate("Form", "VIDEO"))
        self.toolButton_2.setText(_translate("Form", "Face"))
        self.toolButtonWebCamera.setText(_translate("Form", "Web Camera"))
        self.toolButtonFile.setText(_translate("Form", "File"))


import resources_rc
