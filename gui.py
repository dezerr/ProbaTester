# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


# Conversion
# pyuic5 -x test.ui -o test.py


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import time
from datetime import datetime


class Ui_ProbaTester(object):
    def setupUi(self, ProbaTester):
        ProbaTester.setObjectName("ProbaTester")
        ProbaTester.setEnabled(True)
        ProbaTester.resize(788, 495)
        font = QtGui.QFont()
        font.setPointSize(15)
        ProbaTester.setFont(font)
        ProbaTester.setAutoFillBackground(False)
        ProbaTester.setStyleSheet("background-color: #333;\n"
"color #f1f1f1;")
        ProbaTester.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(ProbaTester)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 250, 291, 51))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setStyleSheet("background-color: #f1f1f1;\n"
"font-size: 15px;")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 190, 231, 40))
        self.lineEdit.setStyleSheet("backgroud-color: #f1f1f1;\n"
"color: #f1f1f1;\n"
"border: 1px solid orange;\n"
"font-size: 16px;\n"
"padding: 5px 10px;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 140, 381, 31)) # Gauche / Haut / Droite / Bas
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #f1f1f1;\n"
"font-size: 23px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(650, 400, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #f1f1f1;")
        self.label_2.setObjectName("label_2")
        ProbaTester.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ProbaTester)
        self.statusbar.setObjectName("statusbar")
        ProbaTester.setStatusBar(self.statusbar)

        self.retranslateUi(ProbaTester)
        QtCore.QMetaObject.connectSlotsByName(ProbaTester)

    def retranslateUi(self, ProbaTester):
        _translate = QtCore.QCoreApplication.translate
        ProbaTester.setWindowTitle(_translate("ProbaTester", "ProbaTester"))
        self.pushButton.setText(_translate("ProbaTester", "Lancer le programme"))
        self.label.setText(_translate("ProbaTester", "Entrez le nombre de tentatives"))
        self.label_2.setText(_translate("ProbaTester", "dezerr"))

        def clicked():
                max = lineEdit.text()
                maxInt = int(max)
                hour1 = datetime.now()

                for i in range(0, maxInt):
                    os.system("node tester.js")

                hour2 = datetime.now()

                print(f"\nHeure de début : {hour1.hour}h {hour1.minute}min {hour1.second}sec")
                print(f"Heure de fin : {hour2.hour}h {hour2.minute}min {hour2.second}sec")

        lineEdit = self.lineEdit

        b1 = self.pushButton
        b1.clicked.connect(clicked)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProbaTester = QtWidgets.QMainWindow()
    ui = Ui_ProbaTester()
    ui.setupUi(ProbaTester)
    ProbaTester.show()
    sys.exit(app.exec_())
