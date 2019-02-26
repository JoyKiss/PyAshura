#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-31 13:16:28

'''
pyuic5 test.ui –o test.py
if __name__=='__main__':

    app=QtWidgets.QApplication(sys.argv)

    Form=QtWidgets.QWidget()

    ui=Ui_Dialog()

    ui.setupUi(Form)

    Form.show()

    sys.exit(app.exec_())
'''

import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *  
import cv2
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(609, 367)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 10, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 571, 261))
        self.label.setText("")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 0, 421, 41))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 609, 26))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.A)

        # _translate = QtCore.QCoreApplication.translate

        # self.label.setText(_translate("Dialog", EditText))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
    def A(self,Dialog):
        # text = self.textEdit.toPlainText()
        # print(text)
        # self.textEdit.setText("")
        # history = self.label.text()
        # self.label.setText(history + "\n" + text)
        self.image = QtGui.QImage()
        self.image.load("jietu.jpg")

        self.label.setPixmap(QtGui.QPixmap.fromImage(self.image))
        #读取图片文件
    def imreadex(filename):
        return cv2.imdecode(np.fromfile(filename, dtype=np.uint8), cv2.IMREAD_COLOR)
    # def imageOpenCv2ToQImage (self, cv_img):
    #     height, width, bytesPerComponent = cv_img.shape
    #     bytesPerLine = bytesPerComponent * width;
    #     cv2.cvtColor(cv_img, cv2.CV_BGR2RGB, cv_img)
    #     return QtGui.QImage(cv_img.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
if __name__=='__main__':

    app=QtWidgets.QApplication(sys.argv)

    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
   