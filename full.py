# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main_w(object):
    def setupUi(self, Main_w):
        Main_w.setObjectName("Main_w")
        Main_w.resize(450, 400)
        Main_w.setStyleSheet("")
        self.verticalLayoutWidget = QtWidgets.QWidget(Main_w)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, 49, 171, 421))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Main_w)
        self.label.setGeometry(QtCore.QRect(-4, 0, 121, 51))
        self.label.setStyleSheet("border:1px solid black;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Main_w)
        self.pushButton.setGeometry(QtCore.QRect(120, 10, 41, 25))
        self.pushButton.setObjectName("pushButton")
        self.graphicsView = QtWidgets.QGraphicsView(Main_w)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 450, 400))
        self.graphicsView.setStyleSheet("background: url(include/back.jpg);")
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.raise_()
        self.verticalLayoutWidget.raise_()
        self.label.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Main_w)
        QtCore.QMetaObject.connectSlotsByName(Main_w)

    def retranslateUi(self, Main_w):
        _translate = QtCore.QCoreApplication.translate
        Main_w.setWindowTitle(_translate("Main_w", "Dialog"))
        self.label.setText(_translate("Main_w", "@MyNIk"))
        self.pushButton.setText(_translate("Main_w", "Exit"))

