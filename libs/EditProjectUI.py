# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/EditProject.ui'
#
# Created: Wed Jan 15 23:29:17 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_EditProject(object):
    def setupUi(self, EditProject):
        EditProject.setObjectName("EditProject")
        EditProject.setWindowModality(QtCore.Qt.NonModal)
        EditProject.resize(410, 320)
        EditProject.setMinimumSize(QtCore.QSize(410, 320))
        EditProject.setMaximumSize(QtCore.QSize(410, 320))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/toolbar/project-new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EditProject.setWindowIcon(icon)
        self.verticalLayoutWidget_6 = QtGui.QWidget(EditProject)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(10, 10, 391, 231))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.VL100 = QtGui.QVBoxLayout(self.verticalLayoutWidget_6)
        self.VL100.setContentsMargins(0, 0, 0, 0)
        self.VL100.setObjectName("VL100")
        self.HL110 = QtGui.QHBoxLayout()
        self.HL110.setObjectName("HL110")
        self.VL112 = QtGui.QVBoxLayout()
        self.VL112.setObjectName("VL112")
        self.LblDocID = QtGui.QLabel(self.verticalLayoutWidget_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LblDocID.sizePolicy().hasHeightForWidth())
        self.LblDocID.setSizePolicy(sizePolicy)
        self.LblDocID.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.LblDocID.setFont(font)
        self.LblDocID.setObjectName("LblDocID")
        self.VL112.addWidget(self.LblDocID)
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
        self.lineEdit0proj_id = QtGui.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit0proj_id.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit0proj_id.setFont(font)
        self.lineEdit0proj_id.setObjectName("lineEdit0proj_id")
        self.VL1111.addWidget(self.lineEdit0proj_id)
        self.textEdit0proj_title = QtGui.QTextEdit(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textEdit0proj_title.setFont(font)
        self.textEdit0proj_title.setObjectName("textEdit0proj_title")
        self.VL1111.addWidget(self.textEdit0proj_title)
        self.HL111.addLayout(self.VL1111)
        self.HL110.addLayout(self.HL111)
        self.VL100.addLayout(self.HL110)
        self.VL120 = QtGui.QVBoxLayout()
        self.VL120.setObjectName("VL120")
        self.HL122 = QtGui.QHBoxLayout()
        self.HL122.setObjectName("HL122")
        self.LblStartDate = QtGui.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.LblStartDate.setFont(font)
        self.LblStartDate.setObjectName("LblStartDate")
        self.HL122.addWidget(self.LblStartDate)
        self.LblEndDate = QtGui.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.LblEndDate.setFont(font)
        self.LblEndDate.setObjectName("LblEndDate")
        self.HL122.addWidget(self.LblEndDate)
        self.VL120.addLayout(self.HL122)
        self.HL121 = QtGui.QHBoxLayout()
        self.HL121.setObjectName("HL121")
        self.dateEdit0proj_startdate = QtGui.QDateEdit(self.verticalLayoutWidget_6)
        self.dateEdit0proj_startdate.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.dateEdit0proj_startdate.setFont(font)
        self.dateEdit0proj_startdate.setDate(QtCore.QDate(1900, 1, 1))
        self.dateEdit0proj_startdate.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1900, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit0proj_startdate.setCalendarPopup(True)
        self.dateEdit0proj_startdate.setObjectName("dateEdit0proj_startdate")
        self.HL121.addWidget(self.dateEdit0proj_startdate)
        self.dateEdit0proj_enddate = QtGui.QDateEdit(self.verticalLayoutWidget_6)
        self.dateEdit0proj_enddate.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.dateEdit0proj_enddate.setFont(font)
        self.dateEdit0proj_enddate.setDate(QtCore.QDate(1900, 1, 1))
        self.dateEdit0proj_enddate.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1900, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit0proj_enddate.setMinimumDate(QtCore.QDate(1900, 1, 1))
        self.dateEdit0proj_enddate.setCalendarPopup(True)
        self.dateEdit0proj_enddate.setObjectName("dateEdit0proj_enddate")
        self.HL121.addWidget(self.dateEdit0proj_enddate)
        self.VL120.addLayout(self.HL121)
        self.VL100.addLayout(self.VL120)
        self.HL130 = QtGui.QHBoxLayout()
        self.HL130.setObjectName("HL130")
        self.VL132 = QtGui.QVBoxLayout()
        self.VL132.setObjectName("VL132")
        self.LblContName = QtGui.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.LblContName.setFont(font)
        self.LblContName.setObjectName("LblContName")
        self.VL132.addWidget(self.LblContName)
        self.LblContNo = QtGui.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.LblContNo.setFont(font)
        self.LblContNo.setObjectName("LblContNo")
        self.VL132.addWidget(self.LblContNo)
        self.HL130.addLayout(self.VL132)
        self.HL131 = QtGui.QHBoxLayout()
        self.HL131.setObjectName("HL131")
        self.VL131 = QtGui.QVBoxLayout()
        self.VL131.setObjectName("VL131")
        self.lineEdit0proj_contname = QtGui.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit0proj_contname.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit0proj_contname.setFont(font)
        self.lineEdit0proj_contname.setPlaceholderText("")
        self.lineEdit0proj_contname.setObjectName("lineEdit0proj_contname")
        self.VL131.addWidget(self.lineEdit0proj_contname)
        self.lineEdit0proj_contno = QtGui.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit0proj_contno.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit0proj_contno.setFont(font)
        self.lineEdit0proj_contno.setObjectName("lineEdit0proj_contno")
        self.VL131.addWidget(self.lineEdit0proj_contno)
        self.HL131.addLayout(self.VL131)
        self.HL130.addLayout(self.HL131)
        self.VL100.addLayout(self.HL130)
        self.horizontalLayoutWidget = QtGui.QWidget(EditProject)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(139, 285, 261, 22))
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
        self.LblTotalRecords.setGeometry(QtCore.QRect(4, 0, 71, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LblTotalRecords.sizePolicy().hasHeightForWidth())
        self.LblTotalRecords.setSizePolicy(sizePolicy)
        self.LblTotalRecords.setMinimumSize(QtCore.QSize(65, 0))
        self.LblTotalRecords.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LblTotalRecords.setObjectName("LblTotalRecords")
        self.HL101.addWidget(self.GB2)
        self.GB1 = QtGui.QGroupBox(EditProject)
        self.GB1.setGeometry(QtCore.QRect(5, 246, 126, 68))
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
        self.horizontalLayoutWidget_2 = QtGui.QWidget(EditProject)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(140, 260, 261, 25))
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
        self.LblDocID.setBuddy(self.lineEdit0proj_id)
        self.LblTitle.setBuddy(self.textEdit0proj_title)
        self.LblStartDate.setBuddy(self.dateEdit0proj_startdate)
        self.LblEndDate.setBuddy(self.dateEdit0proj_enddate)
        self.LblContName.setBuddy(self.lineEdit0proj_contname)
        self.LblContNo.setBuddy(self.lineEdit0proj_contno)
        self.LblRecNo.setBuddy(self.lineEditRecordNo)

        self.retranslateUi(EditProject)
        QtCore.QMetaObject.connectSlotsByName(EditProject)
        EditProject.setTabOrder(self.lineEdit0proj_id, self.textEdit0proj_title)
        EditProject.setTabOrder(self.textEdit0proj_title, self.dateEdit0proj_startdate)
        EditProject.setTabOrder(self.dateEdit0proj_startdate, self.dateEdit0proj_enddate)
        EditProject.setTabOrder(self.dateEdit0proj_enddate, self.lineEdit0proj_contname)
        EditProject.setTabOrder(self.lineEdit0proj_contname, self.lineEdit0proj_contno)
        EditProject.setTabOrder(self.lineEdit0proj_contno, self.pushButtonAddMore)
        EditProject.setTabOrder(self.pushButtonAddMore, self.pushButtonCommitAll)
        EditProject.setTabOrder(self.pushButtonCommitAll, self.lineEditRecordNo)
        EditProject.setTabOrder(self.lineEditRecordNo, self.pushButtonFirst)
        EditProject.setTabOrder(self.pushButtonFirst, self.pushButtonPrev)
        EditProject.setTabOrder(self.pushButtonPrev, self.pushButtonNext)
        EditProject.setTabOrder(self.pushButtonNext, self.pushButtonLast)

    def retranslateUi(self, EditProject):
        EditProject.setWindowTitle(QtGui.QApplication.translate("EditProject", "Edit Project", None, QtGui.QApplication.UnicodeUTF8))
        self.LblDocID.setText(QtGui.QApplication.translate("EditProject", "&Project ID", None, QtGui.QApplication.UnicodeUTF8))
        self.LblTitle.setText(QtGui.QApplication.translate("EditProject", "&Title", None, QtGui.QApplication.UnicodeUTF8))
        self.LblStartDate.setText(QtGui.QApplication.translate("EditProject", "&Start Date", None, QtGui.QApplication.UnicodeUTF8))
        self.LblEndDate.setText(QtGui.QApplication.translate("EditProject", "&End Date", None, QtGui.QApplication.UnicodeUTF8))
        self.LblContName.setText(QtGui.QApplication.translate("EditProject", "&Contractor Name", None, QtGui.QApplication.UnicodeUTF8))
        self.LblContNo.setText(QtGui.QApplication.translate("EditProject", "Contract &Number", None, QtGui.QApplication.UnicodeUTF8))
        self.LblTotalRecords.setText(QtGui.QApplication.translate("EditProject", "0 record(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.GB1.setTitle(QtGui.QApplication.translate("EditProject", "Records Navigation", None, QtGui.QApplication.UnicodeUTF8))
        self.LblRecNo.setText(QtGui.QApplication.translate("EditProject", "&Rec #", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAddMore.setText(QtGui.QApplication.translate("EditProject", "&Save && Edit Next", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCommitAll.setText(QtGui.QApplication.translate("EditProject", "&Commit Changes", None, QtGui.QApplication.UnicodeUTF8))

import res_rc
