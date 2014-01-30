from PySide.QtCore import *
from PySide.QtGui import *
import pandas as pd
import ConfirmationTable
from libs.EditShelfUI import Ui_EditShelf
import sys
from lib import *

__version__ = '0.0.1'

class EditShelf(QWidget, Ui_EditShelf):
    def __init__(self, parent=None):
        super(EditShelf, self).__init__(parent)
        self.setupUi(self)
        # class constructor
        self.data = data()
        self.db = db()

        # init call function
        self.data.currentTable = "shelf"
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

        # init decor

    # function
    def setdf(self, list):
        self.df = self.df.append(list)
        self.totalRecord = int(self.df.shape[0])
        self.nav(self.totalRecord)

    def showRecord(self):
        self.lineEdit0shelf_id.setText(str(self.dfCurRecordDict['shelf_id']))
        self.textEdit0shelf_title.setPlainText(str(self.dfCurRecordDict['shelf_title']))
        self.lineEdit0shelf_loc_id.setText(str(self.dfCurRecordDict['shelf_loc_id']))
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
                    shelf_id=self.lineEdit0shelf_id.text(),
                    shelf_title=self.textEdit0shelf_title.toPlainText(),
                    shelf_loc_id=self.lineEdit0shelf_loc_id.text(),
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
                ConfirmationTable.colID = "shelf_id"
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
        if self.lineEdit0shelf_id.text() == "":
            validateList.append("Shelf ID is required")
        if self.textEdit0shelf_title.toPlainText() == "":
            validateList.append("Shelf Title is required")
        if self.lineEdit0shelf_loc_id.text() == "":
            validateList.append("Shelf must be assigned to either a Shelf ID or Loc ID")
        elif self.lineEdit0shelf_loc_id.text() != self.db.queryItem("location", "loc_id", self.lineEdit0shelf_loc_id.text()) and self.lineEdit0shelf_loc_id.text() != "":
            validateList.append("Shelf Location ID must be referenced from Location table")
        if len(validateList) == 0:
            return True
        else:
            self.validateResult = "\n".join(validateList)
            return False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    EditShelf = EditShelf()
    EditShelf.show()
    app.exec_()