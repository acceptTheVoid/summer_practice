# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.combo_genres = QtWidgets.QComboBox(self.centralwidget)
        self.combo_genres.setGeometry(QtCore.QRect(430, 80, 281, 22))
        self.combo_genres.setObjectName("combo_genres")
        self.films_list = QtWidgets.QListWidget(self.centralwidget)
        self.films_list.setGeometry(QtCore.QRect(10, 110, 781, 481))
        self.films_list.setObjectName("films_list")
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(720, 80, 75, 23))
        self.btn_search.setObjectName("btn_search")
        self.name_search = QtWidgets.QLineEdit(self.centralwidget)
        self.name_search.setGeometry(QtCore.QRect(10, 80, 411, 20))
        self.name_search.setText("")
        self.name_search.setObjectName("name_search")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(720, 50, 75, 23))
        self.btn_add.setObjectName("btn_add")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.combo_genres.setPlaceholderText(_translate("MainWindow", "а"))
        self.btn_search.setText(_translate("MainWindow", "Найти!"))
        self.btn_add.setText(_translate("MainWindow", "Добавить"))
