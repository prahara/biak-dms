# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/EditShelf.ui'
#
# Created: Sat Jan 18 13:02:58 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_EditShelf(object):
    def setupUi(self, EditShelf):
        EditShelf.setObjectName("EditShelf")
        EditShelf.setWindowModality(QtCore.Qt.NonModal)
        EditShelf.resize(410, 250)
        EditShelf.setMinimumSize(QtCore.QSize(410, 250))
        EditShelf.setMaximumSize(QtCore.QSize(410, 250))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/toolbar/shelf-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EditShelf.setWindowIcon(icon)
        self.verticalLayoutWidget_6 = QtGui.QWidget(EditShelf)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(10, 10, 391, 165))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.VL100 = QtGui.QVBoxLayout(self.verticalLayoutWidget_6)
        self.VL100.setContentsMargins(0, 0, 0, 0)
        self.VL100.setObjectName("VL100")
        self.HL110 = QtGui.QHBoxLayout()
        self.HL110.setObjectName("HL110")
        self.VL112 = QtGui.QVBoxLayout()
        self.VL112.setObjectName("VL112")
        self.LblFolderID = QtGui.QLabel(self.verticalLayoutWidget_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LblFolderID.sizePolicy().hasHeightForWidth())
        self.LblFolderID.setSizePolicy(sizePolicy)
        self.LblFolderID.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.LblFolderID.setFont(font)
        self.LblFolderID.setObjectName("LblFolderID")
        self.VL112.addWidget(self.LblFolderID)
        self.LblTitle = QtGui.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.LblTitle.setFont(font)
        self.LblTitle.setObjectName("LblTitle")
        self.VL112.addWidget(self.LblTitle)
        self.HL110.addLayout(self.VL112)
        self.HL111 = QtGui.QHBoxLayout()
        self.HL111.setObjectName("HL111")
        self.VL1111 = QtGui.QVBoxLayout()
        self.VL1111.setObjectName("VL1111")
        self.lineEdit0shelf_id = QtGui.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit0shelf_id.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit0shelf_id.setFont(font)
        self.lineEdit0shelf_id.setObjectName("lineEdit0shelf_id")
        self.VL1111.addWidget(self.lineEdit0shelf_id)
        self.textEdit0shelf_title = QtGui.QTextEdit(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textEdit0shelf_title.setFont(font)
        self.textEdit0shelf_title.setObjectName("textEdit0shelf_title")
        self.VL1111.addWidget(self.textEdit0shelf_title)
        self.HL111.addLayout(self.VL1111)
        self.HL110.addLayout(self.HL111)
        self.VL100.addLayout(self.HL110)
        self.VL120_2 = QtGui.QVBoxLayout()
        self.VL120_2.setObjectName("VL120_2")
        self.HL122_2 = QtGui.QHBoxLayout()
        self.HL122_2.setObjectName("HL122_2")
        self.LblStartDate_2 = QtGui.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.LblStartDate_2.setFont(font)
        self.LblStartDate_2.setObjectName("LblStartDate_2")
        self.HL122_2.addWidget(self.LblStartDate_2)
        self.VL120_2.addLayout(self.HL122_2)
        self.HL121_2 = QtGui.QHBoxLayout()
        self.HL121_2.setObjectName("HL121_2")
        self.lineEdit0shelf_loc_id = QtGui.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit0shelf_loc_id.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit0shelf_loc_id.setFont(font)
        self.lineEdit0shelf_loc_id.setObjectName("lineEdit0shelf_loc_id")
        self.HL121_2.addWidget(self.lineEdit0shelf_loc_id)
        self.VL120_2.addLayout(self.HL121_2)
        self.VL100.addLayout(self.VL120_2)
        self.horizontalLayoutWidget = QtGui.QWidget(EditShelf)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(135, 216, 266, 22))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.HL101 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.HL101.setContentsMargins(0, 0, 0, 0)
        self.HL101.setObjectName("HL101")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.HL101.addItem(spacerItem)
        self.GB2 = QtGui.QGroupBox(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GB2.sizePolicy().hasHeightForWidth())
        self.GB2.setSizePolicy(sizePolicy)
        self.GB2.setMinimumSize(QtCore.QSize(93, 0))
        self.GB2.setTitle("")
        self.GB2.setObjectName("GB2")
        self.LblTotalRecords = QtGui.QLabel(self.GB2)
        self.LblTotalRecords.setGeometry(QtCore.QRect(4, 0, 91, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LblTotalRecords.sizePolicy().hasHeightForWidth())
        self.LblTotalRecords.setSizePolicy(sizePolicy)
        self.LblTotalRecords.setMinimumSize(QtCore.QSize(65, 0))
        self.LblTotalRecords.setAlignment(QtCore.Qt.AlignCenter)
        self.LblTotalRecords.setObjectName("LblTotalRecords")
        self.HL101.addWidget(self.GB2)
        self.GB1 = QtGui.QGroupBox(EditShelf)
        self.GB1.setGeometry(QtCore.QRect(6, 176, 126, 68))
        self.GB1.setMaximumSize(QtCore.QSize(16777215, 68))
        self.GB1.setObjectName("GB1")
        self.LblRecNo = QtGui.QLabel(self.GB1)
        self.LblRecNo.setGeometry(QtCore.QRect(10, 40, 65, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LblRecNo.sizePolicy().hasHeightForWidth())
        self.LblRecNo.setSizePolicy(sizePolicy)
        self.LblRecNo.setMinimumSize(QtCore.QSize(65, 0))
        self.LblRecNo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LblRecNo.setObjectName("LblRecNo")
        self.lineEditRecordNo = QtGui.QLineEdit(self.GB1)
        self.lineEditRecordNo.setGeometry(QtCore.QRect(80, 40, 40, 20))
        self.lineEditRecordNo.setMinimumSize(QtCore.QSize(40, 0))
        self.lineEditRecordNo.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineEditRecordNo.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditRecordNo.setObjectName("lineEditRecordNo")
        self.pushButtonLast = QtGui.QPushButton(self.GB1)
        self.pushButtonLast.setGeometry(QtCore.QRect(95, 15, 26, 23))
        self.pushButtonLast.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/navigate/control-stop-right-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLast.setIcon(icon1)
        self.pushButtonLast.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonLast.setObjectName("pushButtonLast")
        self.pushButtonNext = QtGui.QPushButton(self.GB1)
        self.pushButtonNext.setGeometry(QtCore.QRect(65, 15, 26, 23))
        self.pushButtonNext.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/navigate/control-double-right-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonNext.setIcon(icon2)
        self.pushButtonNext.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.pushButtonPrev = QtGui.QPushButton(self.GB1)
        self.pushButtonPrev.setGeometry(QtCore.QRect(35, 15, 26, 23))
        self.pushButtonPrev.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/navigate/control-double-left-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonPrev.setIcon(icon3)
        self.pushButtonPrev.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonPrev.setObjectName("pushButtonPrev")
        self.pushButtonFirst = QtGui.QPushButton(self.GB1)
        self.pushButtonFirst.setGeometry(QtCore.QRect(5, 15, 26, 23))
        self.pushButtonFirst.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/navigate/control-stop-left-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonFirst.setIcon(icon4)
        self.pushButtonFirst.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonFirst.setObjectName("pushButtonFirst")
        self.horizontalLayoutWidget_2 = QtGui.QWidget(EditShelf)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(136, 191, 266, 25))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonAddMore = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAddMore.sizePolicy().hasHeightForWidth())
        self.pushButtonAddMore.setSizePolicy(sizePolicy)
        self.pushButtonAddMore.setMinimumSize(QtCore.QSize(95, 0))
        self.pushButtonAddMore.setObjectName("pushButtonAddMore")
        self.horizontalLayout.addWidget(self.pushButtonAddMore)
        self.pushButtonCommitAll = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonCommitAll.sizePolicy().hasHeightForWidth())
        self.pushButtonCommitAll.setSizePolicy(sizePolicy)
        self.pushButtonCommitAll.setMinimumSize(QtCore.QSize(95, 0))
        self.pushButtonCommitAll.setObjectName("pushButtonCommitAll")
        self.horizontalLayout.addWidget(self.pushButtonCommitAll)
        self.LblFolderID.setBuddy(self.lineEdit0shelf_id)
        self.LblTitle.setBuddy(self.textEdit0shelf_title)
        self.LblStartDate_2.setBuddy(self.lineEdit0shelf_loc_id)
        self.LblRecNo.setBuddy(self.lineEditRecordNo)

        self.retranslateUi(EditShelf)
        QtCore.QMetaObject.connectSlotsByName(EditShelf)
        EditShelf.setTabOrder(self.lineEdit0shelf_id, self.textEdit0shelf_title)
        EditShelf.setTabOrder(self.textEdit0shelf_title, self.lineEdit0shelf_loc_id)
        EditShelf.setTabOrder(self.lineEdit0shelf_loc_id, self.pushButtonAddMore)
        EditShelf.setTabOrder(self.pushButtonAddMore, self.pushButtonCommitAll)
        EditShelf.setTabOrder(self.pushButtonCommitAll, self.lineEditRecordNo)
        EditShelf.setTabOrder(self.lineEditRecordNo, self.pushButtonFirst)
        EditShelf.setTabOrder(self.pushButtonFirst, self.pushButtonPrev)
        EditShelf.setTabOrder(self.pushButtonPrev, self.pushButtonNext)
        EditShelf.setTabOrder(self.pushButtonNext, self.pushButtonLast)

    def retranslateUi(self, EditShelf):
        EditShelf.setWindowTitle(QtGui.QApplication.translate("EditShelf", "Edit Shelf", None, QtGui.QApplication.UnicodeUTF8))
        self.LblFolderID.setText(QtGui.QApplication.translate("EditShelf", "&Shelf ID", None, QtGui.QApplication.UnicodeUTF8))
        self.LblTitle.setText(QtGui.QApplication.translate("EditShelf", "&Title", None, QtGui.QApplication.UnicodeUTF8))
        self.LblStartDate_2.setText(QtGui.QApplication.translate("EditShelf", "&Location ID", None, QtGui.QApplication.UnicodeUTF8))
        self.LblTotalRecords.setText(QtGui.QApplication.translate("EditShelf", "0 record(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.GB1.setTitle(QtGui.QApplication.translate("EditShelf", "Records Navigation", None, QtGui.QApplication.UnicodeUTF8))
        self.LblRecNo.setText(QtGui.QApplication.translate("EditShelf", "Rec #", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAddMore.setText(QtGui.QApplication.translate("EditShelf", "&Save && Edit Next", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCommitAll.setText(QtGui.QApplication.translate("EditShelf", "&Commit All", None, QtGui.QApplication.UnicodeUTF8))

import res_rc
