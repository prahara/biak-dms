# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Settings.ui'
#
# Created: Fri Jan 10 20:18:43 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Setting(object):
    def setupUi(self, Setting):
        Setting.setObjectName("Setting")
        Setting.resize(355, 240)
        Setting.setMinimumSize(QtCore.QSize(355, 240))
        Setting.setMaximumSize(QtCore.QSize(355, 240))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Setting.setWindowIcon(icon)
        self.pushButtonSave = QtGui.QPushButton(Setting)
        self.pushButtonSave.setGeometry(QtCore.QRect(275, 210, 75, 24))
        self.pushButtonSave.setMinimumSize(QtCore.QSize(0, 24))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.pushButtonCancel = QtGui.QPushButton(Setting)
        self.pushButtonCancel.setGeometry(QtCore.QRect(195, 210, 75, 24))
        self.pushButtonCancel.setMinimumSize(QtCore.QSize(0, 24))
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.tabWidget = QtGui.QTabWidget(Setting)
        self.tabWidget.setGeometry(QtCore.QRect(5, 5, 345, 200))
        self.tabWidget.setObjectName("tabWidget")
        self.tabConnection = QtGui.QWidget()
        self.tabConnection.setObjectName("tabConnection")
        self.horizontalLayoutWidget = QtGui.QWidget(self.tabConnection)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(5, 5, 216, 166))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 24))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 24))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 24))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 24))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(0, 24))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEditHostname = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditHostname.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEditHostname.setFont(font)
        self.lineEditHostname.setObjectName("lineEditHostname")
        self.verticalLayout.addWidget(self.lineEditHostname)
        self.lineEditPort = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditPort.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEditPort.setFont(font)
        self.lineEditPort.setMaxLength(5)
        self.lineEditPort.setObjectName("lineEditPort")
        self.verticalLayout.addWidget(self.lineEditPort)
        self.lineEditDatabase = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditDatabase.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEditDatabase.setFont(font)
        self.lineEditDatabase.setObjectName("lineEditDatabase")
        self.verticalLayout.addWidget(self.lineEditDatabase)
        self.lineEditUsername = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditUsername.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEditUsername.setFont(font)
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.verticalLayout.addWidget(self.lineEditUsername)
        self.lineEditPassword = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditPassword.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEditPassword.setFont(font)
        self.lineEditPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.verticalLayout.addWidget(self.lineEditPassword)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.pushButtonCheckConnection = QtGui.QPushButton(self.tabConnection)
        self.pushButtonCheckConnection.setGeometry(QtCore.QRect(230, 140, 101, 24))
        self.pushButtonCheckConnection.setMinimumSize(QtCore.QSize(0, 24))
        self.pushButtonCheckConnection.setObjectName("pushButtonCheckConnection")
        self.tabWidget.addTab(self.tabConnection, "")
        self.label.setBuddy(self.lineEditHostname)
        self.label_2.setBuddy(self.lineEditPort)
        self.label_3.setBuddy(self.lineEditDatabase)
        self.label_4.setBuddy(self.lineEditUsername)
        self.label_5.setBuddy(self.lineEditPassword)

        self.retranslateUi(Setting)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Setting)
        Setting.setTabOrder(self.lineEditHostname, self.lineEditPort)
        Setting.setTabOrder(self.lineEditPort, self.lineEditDatabase)
        Setting.setTabOrder(self.lineEditDatabase, self.lineEditUsername)
        Setting.setTabOrder(self.lineEditUsername, self.lineEditPassword)
        Setting.setTabOrder(self.lineEditPassword, self.pushButtonCheckConnection)
        Setting.setTabOrder(self.pushButtonCheckConnection, self.pushButtonCancel)
        Setting.setTabOrder(self.pushButtonCancel, self.pushButtonSave)
        Setting.setTabOrder(self.pushButtonSave, self.tabWidget)

    def retranslateUi(self, Setting):
        Setting.setWindowTitle(QtGui.QApplication.translate("Setting", "Setting", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSave.setText(QtGui.QApplication.translate("Setting", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancel.setText(QtGui.QApplication.translate("Setting", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Setting", "Hostname", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Setting", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Setting", "Database", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Setting", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Setting", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCheckConnection.setText(QtGui.QApplication.translate("Setting", "Test Connection", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabConnection), QtGui.QApplication.translate("Setting", "Connection", None, QtGui.QApplication.UnicodeUTF8))
