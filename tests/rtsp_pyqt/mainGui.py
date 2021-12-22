# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainGui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Mainui(object):
    def setupUi(self, Mainui):
        Mainui.setObjectName("Mainui")
        Mainui.resize(683, 598)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ICONS/推流结果.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Mainui.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Mainui)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(Mainui)
        self.groupBox_2.setMaximumSize(QtCore.QSize(700, 500))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/ICONS/logo_new.png"))
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(Mainui)
        self.label_3.setMaximumSize(QtCore.QSize(90, 30))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(Mainui)
        self.groupBox.setMaximumSize(QtCore.QSize(400, 400))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.photoButton = QtWidgets.QPushButton(self.groupBox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ICONS/照相.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.photoButton.setIcon(icon1)
        self.photoButton.setObjectName("photoButton")
        self.verticalLayout_2.addWidget(self.photoButton)
        self.playButton = QtWidgets.QPushButton(self.groupBox)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ICONS/启动20190624.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playButton.setIcon(icon2)
        self.playButton.setObjectName("playButton")
        self.verticalLayout_2.addWidget(self.playButton)
        self.pauseButton = QtWidgets.QPushButton(self.groupBox)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ICONS/暂停.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseButton.setIcon(icon3)
        self.pauseButton.setObjectName("pauseButton")
        self.verticalLayout_2.addWidget(self.pauseButton)
        self.stopButton = QtWidgets.QPushButton(self.groupBox)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/ICONS/停止.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon4)
        self.stopButton.setObjectName("stopButton")
        self.verticalLayout_2.addWidget(self.stopButton)
        self.recordButton = QtWidgets.QPushButton(self.groupBox)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/ICONS/录制.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.recordButton.setIcon(icon5)
        self.recordButton.setObjectName("recordButton")
        self.verticalLayout_2.addWidget(self.recordButton)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(Mainui)
        self.groupBox_3.setMaximumSize(QtCore.QSize(400, 200))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ipInput = QtWidgets.QLineEdit(self.groupBox_3)
        self.ipInput.setObjectName("ipInput")
        self.verticalLayout.addWidget(self.ipInput)
        self.setupButton = QtWidgets.QPushButton(self.groupBox_3)
        self.setupButton.setIcon(icon2)
        self.setupButton.setObjectName("setupButton")
        self.verticalLayout.addWidget(self.setupButton)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(Mainui)
        QtCore.QMetaObject.connectSlotsByName(Mainui)

    def retranslateUi(self, Mainui):
        _translate = QtCore.QCoreApplication.translate
        Mainui.setWindowTitle(_translate("Mainui", "Form"))
        self.groupBox_2.setTitle(_translate("Mainui", "VideoStreaming"))
        self.label_3.setText(_translate("Mainui", "V 0.0.1"))
        self.groupBox.setTitle(_translate("Mainui", "ActionButtons"))
        self.photoButton.setText(_translate("Mainui", "take a picture"))
        self.playButton.setText(_translate("Mainui", "play"))
        self.pauseButton.setText(_translate("Mainui", "pause"))
        self.stopButton.setText(_translate("Mainui", "quit"))
        self.recordButton.setText(_translate("Mainui", "record"))
        self.groupBox_3.setTitle(_translate("Mainui", "IP config"))
        self.ipInput.setText(_translate("Mainui", "172.24.1.49"))
        self.setupButton.setText(_translate("Mainui", "setup"))
import icons_rc