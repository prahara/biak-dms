from PySide.QtGui import *
from PySide.QtCore import *
import pandas as pd
from libs.AddProjectUI import Ui_AddProject
from lib import *
import ConfirmationTable
import sys
import datetime

__version__ = '0.0.1'

class AddProject(QWidget, Ui_AddProject):
    def __init__(self, parent=None):
        super(AddProject, self).__init__(parent)
        self.setupUi(self)

        # class constructor
        self.data = data()
        self.db = db()

        # init function
        self.data.currentTable = "project"
        self.data.initProcess()

        # init variable
        self.df = pd.DataFrame(columns=self.data.tableColList[self.data.currentTable])
        self.curRecord = 1                      # int, current df record
        self.totalRecord = 0                    # int, current df last record or total record
        self.indexColName = []                  # list, ["col1", "col2", ...]
        self.username = "sysdefault"

        # signal
        self.pushButtonNext.clicked.connect(lambda: self.nav(self.curRecord+1))
        self.pushButtonPrev.clicked.connect(lambda: self.nav(self.curRecord-1))
        self.pushButtonFirst.clicked.connect(lambda: self.nav(1))
        self.pushButtonLast.clicked.connect(lambda: self.nav(self.totalRecord))
        self.pushButtonAddMore.clicked.connect(lambda: self.addData())
        self.pushButtonCommitAll.clicked.connect(lambda: self.commitAll())
        self.lineEditRecordNo.returnPressed.connect(lambda: self.nav(int(self.lineEditRecordNo.text())))

        # init decor
        self.decorUpdate()

    # funtion
    def showRecord(self):
        self.lineEdit0proj_id.setText(str(self.dfCurRecordDict['proj_id']))
        self.textEdit0proj_title.setPlainText(str(self.dfCurRecordDict['proj_title']))
        self.dateEdit0proj_startdate.setDate(QDate(
            self.dfCurRecordDict['proj_startdate'].year,
            self.dfCurRecordDict['proj_startdate'].month,
            self.dfCurRecordDict['proj_startdate'].day
        ))
        self.dateEdit0proj_enddate.setDate(QDate(
            self.dfCurRecordDict['proj_enddate'].year,
            self.dfCurRecordDict['proj_enddate'].month,
            self.dfCurRecordDict['proj_enddate'].day
        ))
        self.lineEdit0proj_contname.setText(str(self.dfCurRecordDict['proj_contname']))
        self.lineEdit0proj_contno.setText(str(self.dfCurRecordDict['proj_contno']))
        self.lineEditRecordNo.setText(str(self.curRecord))
        self.LblTotalRecords.setText("%s record(s)" % self.totalRecord)

    def decorUpdate(self):
        self.lineEdit0proj_id.clear()
        self.textEdit0proj_title.clear()
        self.lineEdit0proj_contname.clear()
        self.lineEdit0proj_contno.clear()
        self.lineEditRecordNo.setText(str(self.curRecord))
        self.LblTotalRecords.setText("%s record(s)" % self.totalRecord)
        self.textEdit0proj_title.setTabChangesFocus(True)
        self.lineEdit0proj_id.setFocus()

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
            self.dfCurRecord.fillna("")
            self.dfCurRecordDict = self.dfCurRecord.to_dict()
            self.showRecord()

    def addData(self):
        if self.validateInput():
            if self.curRecord == self.totalRecord+1:
                self.dictRowToAdd = dict(
                    proj_id=self.lineEdit0proj_id.text(),
                    proj_title=self.textEdit0proj_title.toPlainText(),
                    proj_startdate=self.dateEdit0proj_startdate.date().toPython(),
                    proj_enddate=self.dateEdit0proj_enddate.date().toPython(),
                    proj_contname=self.lineEdit0proj_contname.text(),
                    proj_contno=self.lineEdit0proj_contno.text(),
                )
                self.df = self.df.append(self.dictRowToAdd, ignore_index=True)
                self.totalRecord += 1
                self.curRecord += 1
                self.decorUpdate()
            else:
                self.dictRowToEdit = dict(
                    proj_id=self.lineEdit0proj_id.text(),
                    proj_title=self.textEdit0proj_title.toPlainText(),
                    proj_startdate=self.dateEdit0proj_startdate.date().toPython(),
                    proj_enddate=self.dateEdit0proj_enddate.date().toPython(),
                    proj_contname=self.lineEdit0proj_contname.text(),
                    proj_contno=self.lineEdit0proj_contno.text(),
                )
                for x in self.dictRowToEdit: self.df.loc[self.curRecord-1]["%s" % x] = self.dictRowToEdit[x]
                self.curRecord = self.totalRecord+1
                self.decorUpdate()
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
                ConfirmationTable.mode = 1
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
        if self.lineEdit0proj_id.text() == "":
            validateList.append("Project ID is required")
        if self.textEdit0proj_title.toPlainText() == "":
            validateList.append("Project Title is required")
        if self.lineEdit0proj_contname.text() == "":
            validateList.append("Project Contractor Name is required")
        if self.dateEdit0proj_startdate.date().toPython() > datetime.date.today():
            validateList.append("Project Start Date should be today or older")
        elif self.dateEdit0proj_enddate.date().toPython() < self.dateEdit0proj_startdate.date().toPython():
            validateList.append("Project End Date should not be older than Project Start Date")
        if len(validateList) == 0:
            return True
        else:
            self.validateResult = "\n".join(validateList)
            return False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    AddProject = AddProject()
    AddProject.show()
    app.exec_()