# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/LoginScreen.ui'
#
# Created: Sun Feb 02 10:48:52 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(230, 200)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(230, 200))
        Dialog.setMaximumSize(QtCore.QSize(230, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/dialog-login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.BtnLogin = QtGui.QPushButton(Dialog)
        self.BtnLogin.setGeometry(QtCore.QRect(150, 160, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.BtnLogin.setFont(font)
        self.BtnLogin.setObjectName("BtnLogin")
        self.EditUsername = QtGui.QLineEdit(Dialog)
        self.EditUsername.setGeometry(QtCore.QRect(10, 80, 210, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EditUsername.setFont(font)
        self.EditUsername.setObjectName("EditUsername")
        self.EditPassword = QtGui.QLineEdit(Dialog)
        self.EditPassword.setGeometry(QtCore.QRect(10, 120, 210, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.EditPassword.setFont(font)
        self.EditPassword.setInputMask("")
        self.EditPassword.setMaxLength(32767)
        self.EditPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.EditPassword.setObjectName("EditPassword")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 70, 60))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/form/dialog-password.png"))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 10, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 30, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(70, 50, 150, 15))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 41, 31))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/form/network-connect.png"))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.EditUsername, self.EditPassword)
        Dialog.setTabOrder(self.EditPassword, self.BtnLogin)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.BtnLogin.setText(QtGui.QApplication.translate("Dialog", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.EditUsername.setPlaceholderText(QtGui.QApplication.translate("Dialog", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.EditPassword.setPlaceholderText(QtGui.QApplication.translate("Dialog", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Biak  ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Document System", None, QtGui.QApplication.UnicodeUTF8))

import res_rc
