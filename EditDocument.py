from PySide.QtCore import *
from PySide.QtGui import *
import pandas as pd
import ConfirmationTable
from libs.EditDocumentUI import Ui_EditDocument
import sys
from lib import *
import datetime

__version__ = '0.0.1'

class EditDocument(QWidget, Ui_EditDocument):
    def __init__(self, parent=None):
        super(EditDocument, self).__init__(parent)
        self.setupUi(self)
        # class constructor
        self.data = data()
        self.db = db()

        # init call function
        self.data.currentTable = "document"
        self.data.initProcess()

        # init variable
        self.df = pd.DataFrame(columns=self.data.tableColList[self.data.currentTable])
        self.curRecord = 1                          # int, current df record
        self.totalRecord = int(self.df.shape[0])    # int, current df last record or total record
        self.indexColName = []                      # list, ["col1", "col2", ...]
        self.username = "sysdefault"

        # signal
        self.pushButtonNext.clicked.connect(lambda: self.nav(self.curRecord+1))
        self.pushButtonPrev.clicked.connect(lambda: self.nav(self.curRecord-1))
        self.pushButtonFirst.clicked.connect(lambda: self.nav(1))
        self.pushButtonLast.clicked.connect(lambda: self.nav(self.totalRecord))
        self.pushButtonAddMore.clicked.connect(lambda: self.editData())
        self.pushButtonCommitAll.clicked.connect(lambda: self.commitAll())
        self.lineEditRecordNo.returnPressed.connect(lambda: self.nav(int(self.lineEditRecordNo.text())))
        self.lineEdit0doc_folder_id.textEdited.connect(lambda: self.decorLocationOption("doc_folder_id"))
        self.lineEdit0doc_shelf_id.textEdited.connect(lambda: self.decorLocationOption("doc_shelf_id"))
        self.lineEdit0doc_loc_id.textEdited.connect(lambda: self.decorLocationOption("doc_loc_id"))
        self.lineEdit0doc_folder_id.editingFinished.connect(lambda: self.decorLocationOption("doc_folder_id"))
        self.lineEdit0doc_shelf_id.editingFinished.connect(lambda: self.decorLocationOption("doc_shelf_id"))
        self.lineEdit0doc_loc_id.editingFinished.connect(lambda: self.decorLocationOption("doc_loc_id"))

        # init decor

    # function
    def setdf(self, list):
        self.df = self.df.append(list)
        self.totalRecord = int(self.df.shape[0])
        self.nav(self.totalRecord)

    def showRecord(self):
        self.lineEdit0doc_id.setText(str(self.dfCurRecordDict['doc_id']))
        self.textEdit0doc_title.setPlainText(str(self.dfCurRecordDict['doc_title']))
        self.lineEdit0doc_proj_id.setText(str(self.dfCurRecordDict['doc_proj_id']))
        self.lineEdit0doc_folder_id.setText(str(self.dfCurRecordDict['doc_folder_id']))
        self.lineEdit0doc_shelf_id.setText(str(self.dfCurRecordDict['doc_shelf_id']))
        self.lineEdit0doc_loc_id.setText(str(self.dfCurRecordDict['doc_loc_id']))
        self.lineEdit0doc_hardnumber.setText(str(self.dfCurRecordDict['doc_hardnumber']))
        self.lineEdit0doc_type.setText(str(self.dfCurRecordDict['doc_type']))
        self.dateEdit0doc_date.setDate(QDate(
            self.dfCurRecordDict['doc_date'].year,
            self.dfCurRecordDict['doc_date'].month,
            self.dfCurRecordDict['doc_date'].day
        ))
        self.lineEdit0doc_url.setText(str(self.dfCurRecordDict['doc_url']))
        self.lineEditRecordNo.setText(str(self.curRecord))
        self.LblTotalRecords.setText("%s record(s)" % self.totalRecord)

    # slot
    def nav(self, recordno):
        if recordno < 1:
            QMessageBox.about(self,
                              "Navigation Error",
                              "Reach first record on loop"
            )
        elif recordno > self.totalRecord:
            QMessageBox.about(self,
                              "Navigation Error",
                              "Currently there are only %s record(s) available. Please try again" % self.totalRecord
            )
        else:
            self.curRecord = recordno
            self.dfCurRecord = self.df.loc[self.curRecord-1]
            self.dfCurRecord = self.dfCurRecord.fillna("")
            self.dfCurRecordDict = self.dfCurRecord.to_dict()
            self.showRecord()

    def editData(self):
        if self.validateInput():
            self.dictRowToEdit = dict(
                doc_id=self.lineEdit0doc_id.text(),
                doc_title=self.textEdit0doc_title.toPlainText(),
                doc_proj_id=self.lineEdit0doc_proj_id.text(),
                doc_folder_id=self.lineEdit0doc_folder_id.text(),
                doc_shelf_id=self.lineEdit0doc_shelf_id.text(),
                doc_loc_id=self.lineEdit0doc_loc_id.text(),
                doc_hardnumber=self.lineEdit0doc_hardnumber.text(),
                doc_date=self.dateEdit0doc_date.date().toPython(),
                doc_type=self.lineEdit0doc_type.text(),
                doc_url=self.lineEdit0doc_url.text()
            )
            for x in self.dictRowToEdit: self.df.loc[self.curRecord-1]["%s" % x] = self.dictRowToEdit[x]
            if self.curRecord == self.totalRecord:
                QMessageBox.about(self,
                                  "Message",
                                  "After editing, hit commit changes button to make changes you've made persistent"
                )
            else:
                self.curRecord += 1
                self.nav(self.curRecord)
        else:
            QMessageBox.about(self, "Input Validation Error", self.validateResult)

    def commitAll(self):
        if self.df.shape[0] != 0:
            self.nav(self.totalRecord)
            if self.validateInput():
                ConfirmationTable.dataListProcess = list(self.df.itertuples(index=False))
                ConfirmationTable.header = self.data.horizontalHeaderTitle[self.data.currentTable]
                ConfirmationTable.tableName = self.data.currentTable
                ConfirmationTable.columnNameList = self.data.tableColList[self.data.currentTable]
                ConfirmationTable.columnNameTuple = '(' + self.data.tableCol[self.data.currentTable] + ')'
                ConfirmationTable.mode = 2
                ConfirmationTable.colID = "doc_id"
                ConfirmationTable.oldString = self.df["%s" % ConfirmationTable.colID].tolist()
                ConfirmationTable.username = self.username
                self.frameConfirmationTable = ConfirmationTable.ConfirmationTable()
                self.frameConfirmationTable.username = self.username
                self.frameConfirmationTable.show()
                self.frameConfirmationTable.connect(self.frameConfirmationTable, SIGNAL('reEditRecord()'), self.reEditRecord)
            else:
                QMessageBox.about(self, "Input Validation Error", self.validateResult)
        else:
            pass

    def decorLocationOption(self, field):
        if field == "doc_folder_id":
            if self.lineEdit0doc_folder_id.text() == "":
                self.lineEdit0doc_shelf_id.setEnabled(True)
                self.lineEdit0doc_loc_id.setEnabled(True)
            else:
                self.lineEdit0doc_shelf_id.setDisabled(True)
                self.lineEdit0doc_loc_id.setDisabled(True)
        elif field == "doc_shelf_id":
            if self.lineEdit0doc_shelf_id.text() == "":
                self.lineEdit0doc_folder_id.setEnabled(True)
                self.lineEdit0doc_loc_id.setEnabled(True)
            else:
                self.lineEdit0doc_folder_id.setDisabled(True)
                self.lineEdit0doc_loc_id.setDisabled(True)
        elif field == "doc_loc_id":
            if self.lineEdit0doc_loc_id.text() == "":
                self.lineEdit0doc_folder_id.setEnabled(True)
                self.lineEdit0doc_shelf_id.setEnabled(True)
            else:
                self.lineEdit0doc_folder_id.setDisabled(True)
                self.lineEdit0doc_shelf_id.setDisabled(True)
        else:
            pass

    def reEditRecord(self):
        self.dictRowToAddfromReEditRecord = []
        if len(ConfirmationTable.dataListFailed) == 0:
            for i in ConfirmationTable.dataListProcess:
                self.dictRowToAddfromReEditRecord.append(dict(zip(ConfirmationTable.columnNameList, i)))
        else:
            for i in ConfirmationTable.dataListFailed:
                self.dictRowToAddfromReEditRecord.append(dict(zip(ConfirmationTable.columnNameList, i)))
        self.df = pd.DataFrame(columns=ConfirmationTable.columnNameList)
        self.df = self.df.append(self.dictRowToAddfromReEditRecord, ignore_index=True)
        self.totalRecord = self.df.shape[0]
        self.curRecord = self.totalRecord
        self.nav(self.curRecord)

    def validateInput(self):
        validateList = []
        self.validateResult = ""
        if self.lineEdit0doc_id.text() == "":
            validateList.append("Document ID is required")
        if self.textEdit0doc_title.toPlainText() == "":
            validateList.append("Document Title is required")
        if self.lineEdit0doc_proj_id.text() == "":
            validateList.append("Document Project ID is required")
        elif self.lineEdit0doc_proj_id.text() != self.db.queryItem("project", "proj_id", self.lineEdit0doc_proj_id.text()):
            validateList.append("Document Project ID should be referenced from Project table")
        if self.lineEdit0doc_folder_id.text() == "" and self.lineEdit0doc_shelf_id.text() == "" and self.lineEdit0doc_loc_id.text() == "":
            validateList.append("Document should be assigned to either a Folder, Shelf, or Location")
        elif self.lineEdit0doc_folder_id.text() != self.db.queryItem("folder", "folder_id", self.lineEdit0doc_folder_id.text()) and self.lineEdit0doc_folder_id.text() != "":
            validateList.append("Document Folder ID should be referenced from Folder table")
        elif self.lineEdit0doc_shelf_id.text() != self.db.queryItem("shelf", "shelf_id", self.lineEdit0doc_shelf_id.text()) and self.lineEdit0doc_shelf_id.text() != "":
            validateList.append("Document Shelf ID should be referenced from Shelf table")
        elif self.lineEdit0doc_loc_id.text() != self.db.queryItem("location", "loc_id", self.lineEdit0doc_loc_id.text()) and self.lineEdit0doc_loc_id.text() != "":
            validateList.append("Document Location ID should be referenced from Location table")
        if self.lineEdit0doc_type.text() == "":
            validateList.append("Document Type is required")
        if self.dateEdit0doc_date.date().toPython() > datetime.date.today():
            validateList.append("Document date must be today or older")
        if len(validateList) == 0:
            return True
        else:
            self.validateResult = "\n".join(validateList)
            return False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    EditDocument = EditDocument()
    EditDocument.show()
    app.exec_()