# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/About.ui'
#
# Created: Mon Jan 27 23:41:57 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AboutPage(object):
    def setupUi(self, AboutPage):
        AboutPage.setObjectName("AboutPage")
        AboutPage.setWindowModality(QtCore.Qt.ApplicationModal)
        AboutPage.resize(240, 320)
        AboutPage.setMinimumSize(QtCore.QSize(240, 320))
        AboutPage.setMaximumSize(QtCore.QSize(240, 320))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/mainwindow-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutPage.setWindowIcon(icon)
        self.textEdit = QtGui.QTextEdit(AboutPage)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(5, 5, 231, 311))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(AboutPage)
        QtCore.QMetaObject.connectSlotsByName(AboutPage)

    def retranslateUi(self, AboutPage):
        AboutPage.setWindowTitle(QtGui.QApplication.translate("AboutPage", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("AboutPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Biak DMS is currently distributed without license. However, commercial/enterprise use are stricly prohibited without statement from the creator. To be precise, this software and all of the flow business process inside are intended for personal use only.  No guarantee is given.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">If you found this software useful: bugs, improvement, and suggestion are very welcome by sending it to </span><span style=\" font-size:8pt; font-weight:600;\">biak@wahyu.org</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Wahyu Reza Prahara</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import res_rc
