from PySide.QtCore import *
from PySide.QtGui import *
import pandas as pd
import ConfirmationTable
from libs.EditFolderUI import Ui_EditFolder
import sys
from lib import *

__version__ = '0.0.1'

class EditFolder(QWidget, Ui_EditFolder):
    def __init__(self, parent=None):
        super(EditFolder, self).__init__(parent)
        self.setupUi(self)
        # class constructor
        self.data = data()
        self.db = db()

        # init call function
        self.data.currentTable = "folder"
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
        self.lineEdit0folder_shelf_id.textEdited.connect(lambda: self.decorLocationOption("folder_shelf_id"))
        self.lineEdit0folder_loc_id.textEdited.connect(lambda: self.decorLocationOption("folder_loc_id"))
        self.lineEdit0folder_shelf_id.editingFinished.connect(lambda: self.decorLocationOption("folder_shelf_id"))
        self.lineEdit0folder_loc_id.editingFinished.connect(lambda: self.decorLocationOption("folder_loc_id"))

        # init decor

    # function
    def setdf(self, list):
        self.df = self.df.append(list)
        self.totalRecord = int(self.df.shape[0])
        self.nav(self.totalRecord)

    def showRecord(self):
        self.lineEdit0folder_id.setText(str(self.dfCurRecordDict['folder_id']))
        self.textEdit0folder_title.setPlainText(str(self.dfCurRecordDict['folder_title']))
        self.lineEdit0folder_shelf_id.setText(str(self.dfCurRecordDict['folder_shelf_id']))
        self.lineEdit0folder_loc_id.setText(str(self.dfCurRecordDict['folder_loc_id']))
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
                    folder_id=self.lineEdit0folder_id.text(),
                    folder_title=self.textEdit0folder_title.toPlainText(),
                    folder_shelf_id=self.lineEdit0folder_shelf_id.text(),
                    folder_loc_id=self.lineEdit0folder_loc_id.text(),
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
                ConfirmationTable.colID = "folder_id"
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
        if field == "folder_shelf_id":
            if self.lineEdit0folder_shelf_id.text() == "":
                self.lineEdit0folder_loc_id.setEnabled(True)
            else:
                self.lineEdit0folder_loc_id.setDisabled(True)
        elif field == "folder_loc_id":
            if self.lineEdit0folder_loc_id.text() == "":
                self.lineEdit0folder_shelf_id.setEnabled(True)
            else:
                self.lineEdit0folder_shelf_id.setDisabled(True)
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
        if self.lineEdit0folder_id.text() == "":
            validateList.append("Folder ID is required")
        if self.textEdit0folder_title.toPlainText() == "":
            validateList.append("Folder Title is required")
        if self.lineEdit0folder_shelf_id.text() == "" and self.lineEdit0folder_loc_id.text() == "":
            validateList.append("Folder must be assigned to either a Shelf ID or Loc ID")
        elif self.lineEdit0folder_shelf_id.text() != self.db.queryItem("shelf", "shelf_id", self.lineEdit0folder_shelf_id.text()) and self.lineEdit0folder_shelf_id.text() != "":
            validateList.append("Folder Shelf ID must be referenced from Shelf table")
        elif self.lineEdit0folder_loc_id.text() != self.db.queryItem("location", "loc_id", self.lineEdit0folder_loc_id.text()) and self.lineEdit0folder_loc_id.text() != "":
            validateList.append("Folder Location ID must be referenced from Location table")
        if len(validateList) == 0:
            return True
        else:
            self.validateResult = "\n".join(validateList)
            return False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    EditFolder = EditFolder()
    EditFolder.show()
    app.exec_()