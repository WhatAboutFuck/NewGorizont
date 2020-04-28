# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dis.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(450, 394)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setAutoFillBackground(True)
        Dialog.setStyleSheet("")
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 450, 400))
        self.graphicsView.setStyleSheet("background: url(include/back.jpg);")
        self.graphicsView.setObjectName("graphicsView")
        self.pushNew = QtWidgets.QPushButton(Dialog)
        self.pushNew.setGeometry(QtCore.QRect(150, 100, 125, 25))
        self.pushNew.setAcceptDrops(True)
        self.pushNew.setAutoFillBackground(True)
        self.pushNew.setStyleSheet("")
        self.pushNew.setObjectName("pushNew")
        self.pushConnect = QtWidgets.QPushButton(Dialog)
        self.pushConnect.setGeometry(QtCore.QRect(150, 210, 125, 25))
        self.pushConnect.setAcceptDrops(False)
        self.pushConnect.setToolTip("")
        self.pushConnect.setWhatsThis("")
        self.pushConnect.setAccessibleName("")
        self.pushConnect.setAccessibleDescription("")
        self.pushConnect.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushConnect.setAutoFillBackground(True)
        self.pushConnect.setStyleSheet("")
        self.pushConnect.setCheckable(False)
        self.pushConnect.setFlat(True)
        self.pushConnect.setObjectName("pushConnect")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 50, 125, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(185, 70, 125, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(150, 140, 125, 17))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushNew.setText(_translate("Dialog", " Новый участник"))
        self.pushConnect.setText(_translate("Dialog", "Продолжить"))
        self.label.setText(_translate("Dialog", "Приветствуем!"))
        self.label_2.setText(_translate("Dialog", "Вы"))
        self.label_3.setText(_translate("Dialog", "Или хотели бы"))

