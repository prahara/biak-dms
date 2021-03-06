# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/AddDocument.ui'
#
# Created: Fri Jan 17 21:11:53 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AddDocument(object):
    def setupUi(self, AddDocument):
        AddDocument.setObjectName("AddDocument")
        AddDocument.setWindowModality(QtCore.Qt.NonModal)
        AddDocument.resize(410, 440)
        AddDocument.setMinimumSize(QtCore.QSize(410, 440))
        AddDocument.setMaximumSize(QtCore.QSize(410, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/toolbar/document-new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddDocument.setWindowIcon(icon)
        self.verticalLayoutWidget_6 = QtGui.QWidget(AddDocument)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(10, 10, 391, 349))
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
        self.lineEdit0doc_id = QtGui.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit0doc_id.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit0doc_id.setFont(font)
        self.lineEdit0doc_id.setObjectName("lineEdit0doc_id")
        self.VL1111.addWidget(self.lineEdit0doc_id)
        self.textEdit0doc_title = QtGui.QTextEdit(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textEdit0doc_title.setFont(font)
        self.textEdit0doc_title.setObjectName("textEdit0doc_title")
        self.VL1111.addWidget(self.textEdit0doc_title)
        self.HL111.addLayout(self.VL1111)
        self.HL110.addLayout(self.HL111)
        self.VL100.addLayout(self.HL110)
        self.VL120 = QtGui.QVBoxLayout()
        self.VL120.setObjectName("VL120")
        self.HL122 = QtGui.QHBoxLayout()
        self.HL122.setObjectName("HL122")
        self.LblEndDate = QtGui.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.LblEndDate.setFont(font)
        self.LblEndDate.setObjectName("LblEndDate")
        self.HL122.addWidget(self.LblEndDate)
        self.LblStartDate = QtGui.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.LblStartDate.setFont(font)
        self.LblStartDate.setObjectName("LblStartDate")
        self.HL122.addWidget(self.LblStartDate)
        self.VL120.addLayout(self.HL122)
        self.HL121 = QtGui.QHBoxLayout()
        self.HL121.setObjectName("HL121")
        self.lineEdit0doc_proj_id = QtGui.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit0doc_proj_id.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit0doc_proj_id.setFont(font)
        self.lineEdit0doc_proj_id.setObjectName("lineEdit0doc_proj_id")
        self.HL121.addWidget(self.lineEdit0doc_proj_id)
        self.lineEdit0doc_folder_id = QtGui.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit0doc_folder_id.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit0doc_folder_id.setFont(font)
        self.lineEdit0doc_folder_id.setObjectName("lineEdit0doc_folder_id")
        self.HL121.addWidget(self.lineEdit0doc_folder_id)
        self.VL120.addLayout(self.HL121)
        self.VL100.addLayout(self.VL120)
        self.VL120_2 = QtGui.QVBoxLayout()
        self.VL120_2.setObjectName("VL120_2")
        self.HL122_2 = QtGui.QHBoxLayout()
        self.HL122_2.setObjectName("HL122_2")
        self.LblEndDate_2 = QtGui.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.LblEndDate_2.setFont(font)
        self.LblEndDate_2.setObjectName("LblEndDate_2")
        self.HL122_2.addWidget(self.LblEndDate_2)
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
        self.lineEdit0doc_shelf_id = QtGui.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit0doc_shelf_id.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit0doc_shelf_id.setFont(font)
        self.lineEdit0doc_shelf_id.setObjectName("lineEdit0doc_shelf_id")
        self.HL121_2.addWidget(self.lineEdit0doc_shelf_id)
        self.lineEdit0doc_loc_id = QtGui.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit0doc_loc_id.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit0doc_loc_id.setFont(font)
        self.lineEdit0doc_loc_id.setObjectName("lineEdit0doc_loc_id")
        self.HL121_2.addWidget(self.lineEdit0doc_loc_id)
        self.VL120_2.addLayout(self.HL121_2)
        self.VL100.addLayout(self.VL120_2)
        self.HL130 = QtGui.QHBoxLayout()
        self.HL130.setObjectName("HL130")
        self.VL132 = QtGui.QVBoxLayout()
        self.VL132.setObjectName("VL132")
        self.LblContName = QtGui.QLabel(self.verticalLayoutWidget_6)
        self.LblContName.setMinimumSize(QtCore.QSize(80, 0))
        self.LblContName.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.LblContName.setFont(font)
        self.LblContName.setObjectName("LblContName")
        self.VL132.addWidget(self.LblContName)
        self.HL130.addLayout(self.VL132)
        self.HL131 = QtGui.QHBoxLayout()
        self.HL131.setObjectName("HL131")
        self.VL131 = QtGui.QVBoxLayout()
        self.VL131.setObjectName("VL131")
        self.lineEdit0doc_hardnumber = QtGui.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit0doc_hardnumber.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit0doc_hardnumber.setFont(font)
        self.lineEdit0doc_hardnumber.setPlaceholderText("")
        self.lineEdit0doc_hardnumber.setObjectName("lineEdit0doc_hardnumber")
        self.VL131.addWidget(self.lineEdit0doc_hardnumber)
        self.HL131.addLayout(self.VL131)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.HL131.addLayout(self.verticalLayout_3)
        self.HL130.addLayout(self.HL131)
        self.VL100.addLayout(self.HL130)
        self.VL120_3 = QtGui.QVBoxLayout()
        self.VL120_3.setObjectName("VL120_3")
        self.HL122_3 = QtGui.QHBoxLayout()
        self.HL122_3.setObjectName("HL122_3")
        self.LblEndDate_3 = QtGui.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.LblEndDate_3.setFont(font)
        self.LblEndDate_3.setObjectName("LblEndDate_3")
        self.HL122_3.addWidget(self.LblEndDate_3)
        self.LblStartDate_3 = QtGui.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.LblStartDate_3.setFont(font)
        self.LblStartDate_3.setObjectName("LblStartDate_3")
        self.HL122_3.addWidget(self.LblStartDate_3)
        self.VL120_3.addLayout(self.HL122_3)
        self.HL121_3 = QtGui.QHBoxLayout()
        self.HL121_3.setObjectName("HL121_3")
        self.dateEdit0doc_date = QtGui.QDateEdit(self.verticalLayoutWidget_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit0doc_date.sizePolicy().hasHeightForWidth())
        self.dateEdit0doc_date.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.dateEdit0doc_date.setFont(font)
        self.dateEdit0doc_date.setDate(QtCore.QDate(1990, 1, 1))
        self.dateEdit0doc_date.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1900, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit0doc_date.setCalendarPopup(True)
        self.dateEdit0doc_date.setObjectName("dateEdit0doc_date")
        self.HL121_3.addWidget(self.dateEdit0doc_date)
        self.lineEdit0doc_type = QtGui.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit0doc_type.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit0doc_type.setFont(font)
        self.lineEdit0doc_type.setObjectName("lineEdit0doc_type")
        self.HL121_3.addWidget(self.lineEdit0doc_type)
        self.VL120_3.addLayout(self.HL121_3)
        self.VL100.addLayout(self.VL120_3)
        self.HL130_2 = QtGui.QHBoxLayout()
        self.HL130_2.setObjectName("HL130_2")
        self.VL132_2 = QtGui.QVBoxLayout()
        self.VL132_2.setObjectName("VL132_2")
        self.LblContName_2 = QtGui.QLabel(self.verticalLayoutWidget_6)
        self.LblContName_2.setMinimumSize(QtCore.QSize(80, 0))
        self.LblContName_2.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.LblContName_2.setFont(font)
        self.LblContName_2.setObjectName("LblContName_2")
        self.VL132_2.addWidget(self.LblContName_2)
        self.HL130_2.addLayout(self.VL132_2)
        self.HL131_2 = QtGui.QHBoxLayout()
        self.HL131_2.setObjectName("HL131_2")
        self.VL131_2 = QtGui.QVBoxLayout()
        self.VL131_2.setObjectName("VL131_2")
        self.lineEdit0doc_url = QtGui.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit0doc_url.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit0doc_url.setFont(font)
        self.lineEdit0doc_url.setPlaceholderText("")
        self.lineEdit0doc_url.setObjectName("lineEdit0doc_url")
        self.VL131_2.addWidget(self.lineEdit0doc_url)
        self.HL131_2.addLayout(self.VL131_2)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.HL131_2.addLayout(self.verticalLayout_4)
        self.HL130_2.addLayout(self.HL131_2)
        self.VL100.addLayout(self.HL130_2)
        self.horizontalLayoutWidget = QtGui.QWidget(AddDocument)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(144, 403, 261, 22))
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
        self.GB1 = QtGui.QGroupBox(AddDocument)
        self.GB1.setGeometry(QtCore.QRect(10, 364, 126, 68))
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
        self.horizontalLayoutWidget_2 = QtGui.QWidget(AddDocument)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(145, 378, 261, 25))
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
        self.LblDocID.setBuddy(self.lineEdit0doc_id)
        self.LblTitle.setBuddy(self.textEdit0doc_title)
        self.LblEndDate.setBuddy(self.lineEdit0doc_proj_id)
        self.LblStartDate.setBuddy(self.lineEdit0doc_folder_id)
        self.LblEndDate_2.setBuddy(self.lineEdit0doc_shelf_id)
        self.LblStartDate_2.setBuddy(self.lineEdit0doc_loc_id)
        self.LblContName.setBuddy(self.lineEdit0doc_hardnumber)
        self.LblEndDate_3.setBuddy(self.dateEdit0doc_date)
        self.LblStartDate_3.setBuddy(self.lineEdit0doc_type)
        self.LblContName_2.setBuddy(self.lineEdit0doc_url)
        self.LblRecNo.setBuddy(self.lineEditRecordNo)

        self.retranslateUi(AddDocument)
        QtCore.QMetaObject.connectSlotsByName(AddDocument)
        AddDocument.setTabOrder(self.lineEdit0doc_id, self.textEdit0doc_title)
        AddDocument.setTabOrder(self.textEdit0doc_title, self.lineEdit0doc_proj_id)
        AddDocument.setTabOrder(self.lineEdit0doc_proj_id, self.lineEdit0doc_folder_id)
        AddDocument.setTabOrder(self.lineEdit0doc_folder_id, self.lineEdit0doc_shelf_id)
        AddDocument.setTabOrder(self.lineEdit0doc_shelf_id, self.lineEdit0doc_loc_id)
        AddDocument.setTabOrder(self.lineEdit0doc_loc_id, self.lineEdit0doc_hardnumber)
        AddDocument.setTabOrder(self.lineEdit0doc_hardnumber, self.dateEdit0doc_date)
        AddDocument.setTabOrder(self.dateEdit0doc_date, self.lineEdit0doc_type)
        AddDocument.setTabOrder(self.lineEdit0doc_type, self.lineEdit0doc_url)
        AddDocument.setTabOrder(self.lineEdit0doc_url, self.pushButtonAddMore)
        AddDocument.setTabOrder(self.pushButtonAddMore, self.pushButtonCommitAll)
        AddDocument.setTabOrder(self.pushButtonCommitAll, self.lineEditRecordNo)
        AddDocument.setTabOrder(self.lineEditRecordNo, self.pushButtonFirst)
        AddDocument.setTabOrder(self.pushButtonFirst, self.pushButtonPrev)
        AddDocument.setTabOrder(self.pushButtonPrev, self.pushButtonNext)
        AddDocument.setTabOrder(self.pushButtonNext, self.pushButtonLast)

    def retranslateUi(self, AddDocument):
        AddDocument.setWindowTitle(QtGui.QApplication.translate("AddDocument", "Add Document", None, QtGui.QApplication.UnicodeUTF8))
        self.LblDocID.setText(QtGui.QApplication.translate("AddDocument", "&Document ID", None, QtGui.QApplication.UnicodeUTF8))
        self.LblTitle.setText(QtGui.QApplication.translate("AddDocument", "&Title", None, QtGui.QApplication.UnicodeUTF8))
        self.LblEndDate.setText(QtGui.QApplication.translate("AddDocument", "&Project ID", None, QtGui.QApplication.UnicodeUTF8))
        self.LblStartDate.setText(QtGui.QApplication.translate("AddDocument", "&Folder ID", None, QtGui.QApplication.UnicodeUTF8))
        self.LblEndDate_2.setText(QtGui.QApplication.translate("AddDocument", "&Shelf ID", None, QtGui.QApplication.UnicodeUTF8))
        self.LblStartDate_2.setText(QtGui.QApplication.translate("AddDocument", "&Location ID", None, QtGui.QApplication.UnicodeUTF8))
        self.LblContName.setText(QtGui.QApplication.translate("AddDocument", "&Hard Number", None, QtGui.QApplication.UnicodeUTF8))
        self.LblEndDate_3.setText(QtGui.QApplication.translate("AddDocument", "&Date", None, QtGui.QApplication.UnicodeUTF8))
        self.LblStartDate_3.setText(QtGui.QApplication.translate("AddDocument", "&Type", None, QtGui.QApplication.UnicodeUTF8))
        self.LblContName_2.setText(QtGui.QApplication.translate("AddDocument", "Lin&k", None, QtGui.QApplication.UnicodeUTF8))
        self.LblTotalRecords.setText(QtGui.QApplication.translate("AddDocument", "0 record(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.GB1.setTitle(QtGui.QApplication.translate("AddDocument", "Records Navigation", None, QtGui.QApplication.UnicodeUTF8))
        self.LblRecNo.setText(QtGui.QApplication.translate("AddDocument", "&Rec #", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAddMore.setText(QtGui.QApplication.translate("AddDocument", "&Save && Add More", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCommitAll.setText(QtGui.QApplication.translate("AddDocument", "&Commit All", None, QtGui.QApplication.UnicodeUTF8))

import res_rc
