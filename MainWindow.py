import sys
import operator
from PySide.QtCore import *
from PySide.QtGui import *
from lib import *
from libs.MainWindowUI import Ui_MainWindow
from time import strftime
import AddDocument, AddFolder, AddProject, AddShelf, AddLocation
import EditDocument, EditFolder, EditProject, EditShelf, EditLocation
import Setting, ConfirmationTable, Account, LoginScreen, About
import pandas as pd

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # class construct
        self.tableData = data()
        self.tableDataEdit = data()
        self.AddDocument = AddDocument.AddDocument()
        self.AddFolder = AddFolder.AddFolder()
        self.AddProject = AddProject.AddProject()
        self.AddShelf = AddShelf.AddShelf()
        self.AddLocation = AddLocation.AddLocation()
        self.Setting = Setting.Setting()
        self.Account = Account.Account()
        self.LoginScreen = LoginScreen.LoginScreen()
        self.About = About.About()
        self.db = db()
        self.crypto = crypto()

        # thread
        self.refreshTableViewThread = RefreshTableView()
        self.generateCustomReportThread = GenerateReport()

        # init variable
        self.tableData.refreshData()
        self.data = self.tableData.dfList
        self.username = "sysdefault"

        # context menu variable
        self.contextAddRecord = QAction(self)
        self.contextEditRecord = QAction(self)
        self.contextDeleteRecord = QAction(self)
        self.contextAddRecord.setText("Add record(s)")
        self.contextEditRecord.setText("Edit selected record(s)")
        self.contextDeleteRecord.setText("Delete selected record(s)")

        # signal
        self.actionDocument.triggered.connect(lambda: self.viewTable("document"))
        self.actionProject.triggered.connect(lambda: self.viewTable("project"))
        self.actionFolder.triggered.connect(lambda: self.viewTable("folder"))
        self.actionShelf.triggered.connect(lambda: self.viewTable("shelf"))
        self.actionLocation.triggered.connect(lambda: self.viewTable("location"))
        self.actionJournal.triggered.connect(lambda: self.viewTable("journal"))
        self.actionConnection.triggered.connect(lambda: self.Setting.show())
        self.actionManage_User.triggered.connect(lambda: self.Account.show())
        self.actionAdd_Document.triggered.connect(lambda: self.AddDocument.show())
        self.actionAdd_Folder.triggered.connect(lambda: self.AddFolder.show())
        self.actionAdd_Project.triggered.connect(lambda: self.AddProject.show())
        self.actionAdd_Shelf.triggered.connect(lambda: self.AddShelf.show())
        self.actionAdd_Location.triggered.connect(lambda: self.AddLocation.show())
        self.actionCustom_Report.triggered.connect(lambda: self.generateCustomReportThread.start())
        self.actionQuery.triggered.connect(lambda: self.query(self.tableData.currentTable))
        self.actionAbout.triggered.connect(lambda: self.About.show())
        self.actionChange_Password.triggered.connect(lambda: self.changePassword())
        self.actionImportDocument.triggered.connect(lambda: self.importRecord("document"))
        self.actionImportProject.triggered.connect(lambda: self.importRecord("project"))
        self.actionImportFolder.triggered.connect(lambda: self.importRecord("folder"))
        self.actionImportShelf.triggered.connect(lambda: self.importRecord("shelf"))
        self.actionImportLocation.triggered.connect(lambda: self.importRecord("location"))
        self.LineEditSearch.returnPressed.connect(lambda: self.searchDataTitle(self.LineEditSearch.text()))
        self.contextAddRecord.triggered.connect(lambda: self.contextMenu("contextAddRecord"))
        self.contextEditRecord.triggered.connect(lambda: self.contextMenu("contextEditRecord"))
        self.contextDeleteRecord.triggered.connect(lambda: self.contextMenu("contextDeleteRecord"))
        self.pushButtonQueryDocument.clicked.connect(lambda: self.query(self.tableData.currentTable))
        self.pushButtonQueryProject.clicked.connect(lambda: self.query(self.tableData.currentTable))
        self.pushButtonQueryFolder.clicked.connect(lambda: self.query(self.tableData.currentTable))
        self.pushButtonQueryShelf.clicked.connect(lambda: self.query(self.tableData.currentTable))
        self.pushButtonQueryLocation.clicked.connect(lambda: self.query(self.tableData.currentTable))
        self.pushButtonQueryJournal.clicked.connect(lambda: self.query(self.tableData.currentTable))
        self.connect(self.refreshTableViewThread,
                     SIGNAL("refreshTableView()"),
                     self.refreshTableView,
                     Qt.QueuedConnection
        )
        self.connect(self.LoginScreen,
                     SIGNAL("loginOK()"),
                     self.loginok,
                     Qt.QueuedConnection
        )
        self.connect(self.generateCustomReportThread,
                     SIGNAL("reportSuccess()"),
                     self.reportSuccess,
                     Qt.QueuedConnection
        )

        # decoration
        self.LoginScreen.show()

    # class function
    def refreshTableView(self):
        # table model update
        self.tableModel = TableModel(self,
                                self.tableData.dfList,
                                self.tableData.horizontalHeaderTitle[self.tableData.currentTable],
                                self.tableData.verticalHeaderTitle
        )
        # table decor
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setModel(self.tableModel)
        self.tableView.setSortingEnabled(True)
        self.tableView.resizeColumnsToContents()
        self.tableView.resizeRowsToContents()
        self.tableView.horizontalHeader().setResizeMode(1, QHeaderView.Stretch)
        self.statusBar().showMessage("%s record(s) loaded" % len(self.tableData.dfList))

    # slot
    def loginok(self):
        self.username = self.LoginScreen.username
        try:
            self.roleslevel = int(self.db.queryRecord("account", "acc_username", self.username)["acc_roles_level"])
        except IndexError:
            self.roleslevel = 50
        self.AddDocument.username = self.username
        self.AddFolder.username = self.username
        self.AddProject.username = self.username
        self.AddLocation.username = self.username
        self.AddShelf.username = self.username
        self.Account.username = self.username
        self.Account.roleslevel = self.roleslevel
        self.Account.refreshTableView()
        MainWindow.show()
        self.refreshTableViewThread.start()
        self.statusBar().showMessage("Biak Document System v1.0")
        self.tableView.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.tableView.addAction(self.contextAddRecord)
        self.tableView.addAction(self.contextEditRecord)
        self.tableView.addAction(self.contextDeleteRecord)
        self.dockWidget.hide()
        self.QLabelStatus = QLabel(self)
        self.QLabelStatus.setText("Logged in as: %s" % self.username)
        self.statusbar.addPermanentWidget(self.QLabelStatus)
        self.rolesLevelCheck()

    def importRecord(self, table):
        fileName = QFileDialog.getOpenFileName(self, "Open File", "C:\\",
                                               "Excel Files (*.xls *.xlsx)")
        if not fileName[0] == "":
            self.df = pd.read_excel(fileName[0], 0)
            self.df = self.df.fillna("")
            ConfirmationTable.dataListProcess = list(self.df.itertuples(index=False))
            ConfirmationTable.header = self.tableData.horizontalHeaderTitle[table]
            ConfirmationTable.tableName = self.tableData.currentTable
            ConfirmationTable.columnNameList = self.tableData.tableColList[table]
            ConfirmationTable.columnNameTuple = '(' + self.tableData.tableCol[table] + ')'
            ConfirmationTable.mode = 1
            ConfirmationTable.username = self.username
            ConfirmationTable.log = "Import from Excel"
            self.importConfirmationTable = ConfirmationTable.ConfirmationTable()
            self.importConfirmationTable.show()
        else:
            pass

    def changePassword(self):
        text, ok = QInputDialog.getText(self, self.tr("Change Password"),
                                    self.tr("Enter current password:"), QLineEdit.Password)
        if self.db.authLogin(self.username, text) and ok:
            text, ok = QInputDialog.getText(self, self.tr("Change Password"),
                                    self.tr("Enter new password:"), QLineEdit.Password)
            if ok:
                textconfirm, ok = QInputDialog.getText(self, self.tr("Change Password"),
                                    self.tr("Re-enter new password:"), QLineEdit.Password)
                if (text == textconfirm) and ok:
                    inserttuple = (
                        self.username,
                        self.crypto.encode("AutoGenerate", textconfirm),
                        self.crypto.encodeKey
                    )
                    if self.db.update("account",
                                  "(acc_username, acc_password, acc_passkey)",
                                  inserttuple,
                                  "acc_username",
                                  self.username
                    ):
                        QMessageBox.about(self, "Success", "Password successfully changed")
                    else:
                        QMessageBox.about(self, "Failed", "Password change failed")
                else:
                    QMessageBox.about(self, "Failed", "Please enter password twice to reconfirm")
        else:
            if not self.db.authLogin(self.username, text) and ok:
                QMessageBox.about(self, "Failed", "Wrong password")

    def viewTable(self, tableName):
        self.tableData.currentTable = tableName
        # select * from document
        # join (select jo_doc_id, jo_act_id, rank() over (partition by jo_doc_id order by jo_datetime desc) ranking from journal)
        # journal on (journal.ranking = 1 and journal.jo_doc_id = document.doc_id and journal.jo_act_id <> 'DELETE')
        self.tableData.sql = "SELECT * from %s" % tableName
        if tableName == "document":
            self.stackedWidget.setCurrentIndex(0)
            self.tableData.sql = "SELECT * FROM %s " \
                                 "JOIN (SELECT jo_doc_id, jo_act_id, " \
                                 "RANK() OVER (PARTITION BY jo_doc_id ORDER by jo_datetime DESC) " \
                                 "RANKING FROM journal) journal " \
                                 "ON (journal.RANKING = 1 and journal.jo_doc_id = %s.doc_id " \
                                 "AND journal.jo_act_id <> 'DELETE')" % (tableName, tableName)
        elif tableName == "project":
            self.stackedWidget.setCurrentIndex(1)
            self.tableData.sql = "SELECT * FROM %s " \
                                 "JOIN (SELECT jo_proj_id, jo_act_id, " \
                                 "RANK() OVER (PARTITION BY jo_proj_id ORDER by jo_datetime DESC) " \
                                 "RANKING FROM journal) journal " \
                                 "ON (journal.RANKING = 1 and journal.jo_proj_id = %s.proj_id " \
                                 "AND journal.jo_act_id <> 'DELETE')" % (tableName, tableName)
        elif tableName == "folder":
            self.stackedWidget.setCurrentIndex(2)
            self.tableData.sql = "SELECT * FROM %s " \
                                 "JOIN (SELECT jo_folder_id, jo_act_id, " \
                                 "RANK() OVER (PARTITION BY jo_folder_id ORDER by jo_datetime DESC) " \
                                 "RANKING FROM journal) journal " \
                                 "ON (journal.RANKING = 1 and journal.jo_folder_id = %s.folder_id " \
                                 "AND journal.jo_act_id <> 'DELETE')" % (tableName, tableName)
        elif tableName == "shelf":
            self.stackedWidget.setCurrentIndex(3)
            self.tableData.sql = "SELECT * FROM %s " \
                                 "JOIN (SELECT jo_shelf_id, jo_act_id, " \
                                 "RANK() OVER (PARTITION BY jo_shelf_id ORDER by jo_datetime DESC) " \
                                 "RANKING FROM journal) journal " \
                                 "ON (journal.RANKING = 1 and journal.jo_shelf_id = %s.shelf_id " \
                                 "AND journal.jo_act_id <> 'DELETE')" % (tableName, tableName)
        elif tableName == "location":
            self.stackedWidget.setCurrentIndex(4)
            self.tableData.sql = "SELECT * FROM %s " \
                                 "JOIN (SELECT jo_loc_id, jo_act_id, " \
                                 "RANK() OVER (PARTITION BY jo_loc_id ORDER by jo_datetime DESC) " \
                                 "RANKING FROM journal) journal " \
                                 "ON (journal.RANKING = 1 and journal.jo_loc_id = %s.loc_id " \
                                 "AND journal.jo_act_id <> 'DELETE')" % (tableName, tableName)
        elif tableName == "journal":
            self.stackedWidget.setCurrentIndex(5)
            self.tableData.sql = "SELECT * FROM %s" % tableName
        else:
            pass
        self.refreshTableViewThread.start()

    def searchDataTitle(self, searchString):
        if not searchString == "":
            self.tableData.sql = "SELECT * from %s WHERE lower(%s) like lower('%%%s%%')" % (
                self.tableData.currentTable,
                self.tableData.tableTitleCol[self.tableData.currentTable],
                searchString
            )
            self.tableData.mode = 2
            self.refreshTableViewThread.start()
        else:
            self.viewTable(self.tableData.currentTable)
            self.tableData.mode = 1

    def contextMenu(self, action):
        if action == "contextAddRecord":
            if self.tableData.currentTable == "document":
                self.AddDocument.show()
            elif self.tableData.currentTable == "project":
                self.AddProject.show()
            elif self.tableData.currentTable == "folder":
                self.AddFolder.show()
            elif self.tableData.currentTable == "shelf":
                self.AddShelf.show()
            elif self.tableData.currentTable == "location":
                self.AddLocation.show()
            else:
                pass
        elif action == "contextEditRecord":
            self.editList = []
            if self.tableData.currentTable == "document":
                for selected in self.tableView.selectionModel().selectedRows():
                    if self.tableData.dfToDisplay.ix[self.tableData.dfToDisplay[
                        self.tableData.dfToDisplay["doc_id"] == selected.data()
                    ].index.tolist()[0]].tolist() not in self.editList:
                        self.editList.append(
                            self.tableData.dfToDisplay.ix[self.tableData.dfToDisplay[
                                self.tableData.dfToDisplay["doc_id"] == selected.data()
                                ].index.tolist()[0]].to_dict()
                        )
            elif self.tableData.currentTable == "project":
                for selected in self.tableView.selectionModel().selectedRows():
                    if self.tableData.dfToDisplay.ix[self.tableData.dfToDisplay[
                        self.tableData.dfToDisplay["proj_id"] == selected.data()
                    ].index.tolist()[0]].tolist() not in self.editList:
                        self.editList.append(
                            self.tableData.dfToDisplay.ix[self.tableData.dfToDisplay[
                                self.tableData.dfToDisplay["proj_id"] == selected.data()
                                ].index.tolist()[0]].to_dict()
                        )
            elif self.tableData.currentTable == "folder":
                for selected in self.tableView.selectionModel().selectedRows():
                    if self.tableData.dfToDisplay.ix[self.tableData.dfToDisplay[
                        self.tableData.dfToDisplay["folder_id"] == selected.data()
                    ].index.tolist()[0]].tolist() not in self.editList:
                        self.editList.append(
                            self.tableData.dfToDisplay.ix[self.tableData.dfToDisplay[
                                self.tableData.dfToDisplay["folder_id"] == selected.data()
                                ].index.tolist()[0]].to_dict()
                        )
            elif self.tableData.currentTable == "shelf":
                for selected in self.tableView.selectionModel().selectedRows():
                    if self.tableData.dfToDisplay.ix[self.tableData.dfToDisplay[
                        self.tableData.dfToDisplay["shelf_id"] == selected.data()
                    ].index.tolist()[0]].tolist() not in self.editList:
                        self.editList.append(
                            self.tableData.dfToDisplay.ix[self.tableData.dfToDisplay[
                                self.tableData.dfToDisplay["shelf_id"] == selected.data()
                                ].index.tolist()[0]].to_dict()
                        )
            elif self.tableData.currentTable == "location":
                for selected in self.tableView.selectionModel().selectedRows():
                    if self.tableData.dfToDisplay.ix[self.tableData.dfToDisplay[
                        self.tableData.dfToDisplay["loc_id"] == selected.data()
                    ].index.tolist()[0]].tolist() not in self.editList:
                        self.editList.append(
                            self.tableData.dfToDisplay.ix[self.tableData.dfToDisplay[
                                self.tableData.dfToDisplay["loc_id"] == selected.data()
                                ].index.tolist()[0]].to_dict()
                        )
            else:
                pass
            if self.tableData.currentTable == "document":
                self.EditDocument = EditDocument.EditDocument()
                self.EditDocument.setdf(self.editList)
                self.EditDocument.username = self.username
                self.EditDocument.show()
            elif self.tableData.currentTable == "project":
                self.EditProject = EditProject.EditProject()
                self.EditProject.username = self.username
                self.EditProject.setdf(self.editList)
                self.EditProject.show()
            elif self.tableData.currentTable == "folder":
                self.EditFolder = EditFolder.EditFolder()
                self.EditFolder.username = self.username
                self.EditFolder.setdf(self.editList)
                self.EditFolder.show()
            elif self.tableData.currentTable == "shelf":
                self.EditShelf = EditShelf.EditShelf()
                self.EditShelf.username = self.username
                self.EditShelf.setdf(self.editList)
                self.EditShelf.show()
            elif self.tableData.currentTable == "location":
                self.EditLocation = EditLocation.EditLocation()
                self.EditLocation.username = self.username
                self.EditLocation.setdf(self.editList)
                self.EditLocation.show()
            else:
                pass
        elif action == "contextDeleteRecord":
            if self.tableData.currentTable == "document":
                self.colid = "doc_id"
            elif self.tableData.currentTable == "project":
                self.colid = "proj_id"
            elif self.tableData.currentTable == "folder":
                self.colid = "folder_id"
            elif self.tableData.currentTable == "shelf":
                self.colid = "shelf_id"
            elif self.tableData.currentTable == "location":
                self.colid = "loc_id"
            else:
                pass

            self.editList = []
            if self.tableData.currentTable == "document":
                for selected in self.tableView.selectionModel().selectedRows():
                    if self.tableData.dfToDisplay.ix[self.tableData.dfToDisplay[
                        self.tableData.dfToDisplay["doc_id"] == selected.data()
                    ].index.tolist()[0]].tolist() not in self.editList:
                        self.editList.append(
                            self.tableData.dfToDisplay.ix[self.tableData.dfToDisplay[
                                self.tableData.dfToDisplay["doc_id"] == selected.data()
                                ].index.tolist()[0]].tolist()
                        )
            elif self.tableData.currentTable == "project":
                for selected in self.tableView.selectionModel().selectedRows():
                    if self.tableData.dfToDisplay.ix[self.tableData.dfToDisplay[
                        self.tableData.dfToDisplay["proj_id"] == selected.data()
                    ].index.tolist()[0]].tolist() not in self.editList:
                        self.editList.append(
                            self.tableData.dfToDisplay.ix[self.tableData.dfToDisplay[
                                self.tableData.dfToDisplay["proj_id"] == selected.data()
                                ].index.tolist()[0]].tolist()
                        )
            elif self.tableData.currentTable == "folder":
                for selected in self.tableView.selectionModel().selectedRows():
                    if self.tableData.dfToDisplay.ix[self.tableData.dfToDisplay[
                        self.tableData.dfToDisplay["folder_id"] == selected.data()
                    ].index.tolist()[0]].tolist() not in self.editList:
                        self.editList.append(
                            self.tableData.dfToDisplay.ix[self.tableData.dfToDisplay[
                                self.tableData.dfToDisplay["folder_id"] == selected.data()
                                ].index.tolist()[0]].tolist()
                        )
            elif self.tableData.currentTable == "shelf":
                for selected in self.tableView.selectionModel().selectedRows():
                    if self.tableData.dfToDisplay.ix[self.tableData.dfToDisplay[
                        self.tableData.dfToDisplay["shelf_id"] == selected.data()
                    ].index.tolist()[0]].tolist() not in self.editList:
                        self.editList.append(
                            self.tableData.dfToDisplay.ix[self.tableData.dfToDisplay[
                                self.tableData.dfToDisplay["folder_id"] == selected.data()
                                ].index.tolist()[0]].tolist()
                        )
            elif self.tableData.currentTable == "location":
                for selected in self.tableView.selectionModel().selectedRows():
                    if self.tableData.dfToDisplay.ix[self.tableData.dfToDisplay[
                        self.tableData.dfToDisplay["loc_id"] == selected.data()
                    ].index.tolist()[0]].tolist() not in self.editList:
                        self.editList.append(
                            self.tableData.dfToDisplay.ix[self.tableData.dfToDisplay[
                                self.tableData.dfToDisplay["loc_id"] == selected.data()
                                ].index.tolist()[0]].tolist()
                        )
            else:
                pass
            ConfirmationTable.dataListProcess = self.editList
            ConfirmationTable.header = self.tableData.horizontalHeaderTitle[self.tableData.currentTable]
            ConfirmationTable.tableName = self.tableData.currentTable
            ConfirmationTable.columnNameList = self.tableData.tableColList[self.tableData.currentTable]
            ConfirmationTable.columnNameTuple = '(' + self.tableData.tableCol[self.tableData.currentTable] + ')'
            ConfirmationTable.mode = 3
            ConfirmationTable.colID = self.colid
            ConfirmationTable.username = self.username
            self.frameConfirmationTable = ConfirmationTable.ConfirmationTable()
            self.frameConfirmationTable.show()
        else:
            pass

    def query(self, currenttable):
        self.dockWidget.show()
        if currenttable == "document":
            self.stackedWidget.setCurrentIndex(0)
            logic = []
            sqllogic = ''
            if self.checkBox0doc_id.isChecked():
                logic.append("lower(doc_id) " + self.comboBox0doc_id.currentText() + " lower('%s')" % self.lineEdit0doc_id.text())
            if self.checkBox0doc_title.isChecked():
                logic.append("lower(doc_title) " + self.comboBox0doc_title.currentText() + " lower('%s')" % self.lineEdit0doc_title.text())
            if self.checkBox0doc_proj_id.isChecked():
                logic.append("lower(doc_proj_id) " + self.comboBox0doc_proj_id.currentText() + " lower('%s')" % self.lineEdit0doc_proj_id.text())
            if self.checkBox0doc_folder_id.isChecked():
                logic.append("lower(doc_folder_id) " + self.comboBox0doc_folder_id.currentText() + " lower('%s')" % self.lineEdit0doc_folder_id.text())
            if self.checkBox0doc_shelf_id.isChecked():
                logic.append("lower(doc_shelf_id) " + self.comboBox0doc_shelf_id.currentText() + " lower('%s')" % self.lineEdit0doc_shelf_id.text())
            if self.checkBox0doc_loc_id.isChecked():
                logic.append("lower(doc_loc_id) " + self.comboBox0doc_loc_id.currentText() + " lower('%s')" % self.lineEdit0doc_loc_id.text())
            if self.checkBox0doc_hardnumber.isChecked():
                logic.append("lower(doc_hardnumber) " + self.comboBox0doc_hardnumber.currentText() + " lower('%s')" % self.lineEdit0doc_hardnumber.text())
            if self.checkBox0doc_type.isChecked():
                logic.append("lower(doc_type) " + self.comboBox0doc_type.currentText() + " lower('%s')" % self.lineEdit0doc_type.text())
            if self.checkBox0doc_date.isChecked():
                logic.append("doc_date " + self.comboBox0doc_date.currentText() + " '%s'" % self.dateEdit0doc_date.date().toPython())
        elif currenttable == "project":
            self.stackedWidget.setCurrentIndex(1)
            logic = []
            sqllogic = ''
            if self.checkBox0proj_id.isChecked():
                logic.append("lower(proj_id) " + self.comboBox0proj_id.currentText() + " lower('%s')" % self.lineEdit0proj_id.text())
            if self.checkBox0proj_title.isChecked():
                logic.append("lower(proj_title) " + self.comboBox0proj_title.currentText() + " lower('%s')" % self.lineEdit0proj_title.text())
            if self.checkBox0proj_contname.isChecked():
                logic.append("lower(proj_contname) " + self.comboBox0proj_contname.currentText() + " lower('%s')" % self.lineEdit0proj_contname.text())
            if self.checkBox0proj_contno.isChecked():
                logic.append("lower(proj_contno) " + self.comboBox0proj_contno.currentText() + " lower('%s')" % self.lineEdit0proj_contno.text())
            if self.checkBox0proj_startdate.isChecked():
                logic.append("proj_startdate " + self.comboBox0proj_startdate.currentText() + " '%s'" % self.dateEdit0proj_startdate.date().toPython())
            if self.checkBox0proj_enddate.isChecked():
                logic.append("proj_enddate " + self.comboBox0proj_enddate.currentText() + " '%s'" % self.dateEdit0proj_enddate.date().toPython())
        elif currenttable == "folder":
            self.stackedWidget.setCurrentIndex(2)
            logic = []
            sqllogic = ''
            if self.checkBox0folder_id.isChecked():
                logic.append("lower(folder_id) " + self.comboBox0folder_id.currentText() + " lower('%s')" % self.lineEdit0folder_id.text())
            elif self.checkBox0folder_title.isChecked():
                logic.append("lower(folder_title) " + self.comboBox0folder_title.currentText() + " lower('%s')" % self.lineEdit0folder_title.text())
            elif self.checkBox0folder_shelf_id.isChecked():
                logic.append("lower(folder_shelf_id) " + self.comboBox0folder_shelf_id.currentText() + " lower('%s')" % self.lineEdit0folder_shelf_id.text())
            elif self.checkBox0folder_loc_id.isChecked():
                logic.append("lower(folder_loc_id) " + self.comboBox0folder_loc_id.currentText() + " lower('%s')" % self.lineEdit0folder_loc_id.text())
        elif currenttable == "shelf":
            self.stackedWidget.setCurrentIndex(3)
            logic = []
            sqllogic = ''
            if self.checkBox0shelf_id.isChecked():
                logic.append("lower(shelf_id) " + self.comboBox0shelf_id.currentText() + " lower('%s')" % self.lineEdit0shelf_id.text())
            if self.checkBox0shelf_title.isChecked():
                logic.append("lower(shelf_title) " + self.comboBox0shelf_title.currentText() + " lower('%s')" % self.lineEdit0shelf_title.text())
            if self.checkBox0shelf_loc_id.isChecked():
                logic.append("lower(shelf_loc_id) " + self.comboBox0shelf_loc_id.currentText() + " lower('%s')" % self.lineEdit0shelf_loc_id.text())
        elif currenttable == "location":
            self.stackedWidget.setCurrentIndex(4)
            logic = []
            sqllogic = ''
            if self.checkBox0loc_id.isChecked():
                logic.append("lower(loc_id) " + self.comboBox0loc_id.currentText() + " lower('%s')" % self.lineEdit0loc_id.text())
            if self.checkBox0loc_title.isChecked():
                logic.append("lower(loc_title) " + self.comboBox0loc_title.currentText() + " lower('%s')" % self.lineEdit0loc_title.text())
        elif currenttable == "journal":
            self.stackedWidget.setCurrentIndex(5)
            logic = []
            sqllogic = ''
            if self.checkBox0jo_acc_username.isChecked():
                logic.append("lower(jo_act_username) " + self.comboBox0jo_acc_username.currentText() + " lower('%s')" % self.lineEdit0jo_acc_username.text())
            if self.checkBox0jo_act_id.isChecked():
                logic.append("lower(jo_act_id) " + self.comboBox0jo_act_id.currentText() + " lower('%s')" % self.lineEdit0jo_act_id.text())
            if self.checkBox0jo_proj_id.isChecked():
                logic.append("lower(jo_proj_id) " + self.comboBox0jo_proj_id.currentText() + " lower('%s')" % self.lineEdit0jo_proj_id.text())
            if self.checkBox0jo_doc_id.isChecked():
                logic.append("lower(jo_doc_id) " + self.comboBox0jo_doc_id.currentText() + " lower('%s')" % self.lineEdit0jo_doc_id.text())
            if self.checkBox0jo_folder_id.isChecked():
                logic.append("lower(jo_folder_id) " + self.comboBox0jo_folder_id.currentText() + " lower('%s')" % self.lineEdit0jo_folder_id.text())
            if self.checkBox0jo_shelf_id.isChecked():
                logic.append("lower(jo_shelf_id) " + self.comboBox0jo_shelf_id.currentText() + " lower('%s')" % self.lineEdit0jo_shelf_id.text())
            if self.checkBox0jo_loc_id.isChecked():
                logic.append("lower(jo_loc_id) " + self.comboBox0jo_loc_id.currentText() + " lower('%s')" % self.lineEdit0jo_loc_id.text())
            if self.checkBox0jo_detail.isChecked():
                logic.append("lower(jo_detail) " + self.comboBox0jo_detail.currentText() + " lower('%s')" % self.lineEdit0jo_detail.text())
            if self.checkBox0jo_datetime.isChecked():
                logic.append("jo_datetime " + self.comboBox0jo_datetime.currentText() + " '%s'" % self.dateTimeEdit0jo_datetime.dateTime().toPython())
        else:
            pass

        # logic
        for content in logic:
            index = logic.index(content)
            logic[index] = logic[index].replace("equals to", "=")
            logic[index] = logic[index].replace("contains lower('", "LIKE lower('%")
            if "LIKE" in logic[index]:
                logic[index] = logic[index][0:len(logic[index])-2] + "%')"
            if "is lower('" in logic[index]:
                logic[index] = logic[index].replace("is lower('", "is ")
                logic[index] = logic[index][0:len(logic[index])-2]
            sqllogic = " and ".join(logic)
        self.tableData.currentTable = currenttable
        if len(logic) == 0:
            if self.tableData.currentTable == "document":
                self.tableData.sql = "SELECT * FROM %s " \
                                     "JOIN (SELECT jo_doc_id, jo_act_id, " \
                                     "RANK() OVER (PARTITION BY jo_doc_id ORDER by jo_datetime DESC) " \
                                     "RANKING FROM journal) journal " \
                                     "ON (journal.RANKING = 1 and journal.jo_doc_id = %s.doc_id " \
                                     "AND journal.jo_act_id <> 'DELETE')" % (self.tableData.currentTable,
                self.tableData.currentTable)
            elif self.tableData.currentTable == "project":
                self.tableData.sql = "SELECT * FROM %s " \
                                     "JOIN (SELECT jo_proj_id, jo_act_id, " \
                                     "RANK() OVER (PARTITION BY jo_proj_id ORDER by jo_datetime DESC) " \
                                     "RANKING FROM journal) journal " \
                                     "ON (journal.RANKING = 1 and journal.jo_proj_id = %s.proj_id " \
                                     "AND journal.jo_act_id <> 'DELETE')" % (self.tableData.currentTable,
                self.tableData.currentTable)
            elif self.tableData.currentTable == "folder":
                self.tableData.sql = "SELECT * FROM %s " \
                                     "JOIN (SELECT jo_folder_id, jo_act_id, " \
                                     "RANK() OVER (PARTITION BY jo_folder_id ORDER by jo_datetime DESC) " \
                                     "RANKING FROM journal) journal " \
                                     "ON (journal.RANKING = 1 and journal.jo_folder_id = %s.folder_id " \
                                     "AND journal.jo_act_id <> 'DELETE')" % (self.tableData.currentTable,
                self.tableData.currentTable)
            elif self.tableData.currentTable == "shelf":
                self.tableData.sql = "SELECT * FROM %s " \
                                     "JOIN (SELECT jo_shelf_id, jo_act_id, " \
                                     "RANK() OVER (PARTITION BY jo_shelf_id ORDER by jo_datetime DESC) " \
                                     "RANKING FROM journal) journal " \
                                     "ON (journal.RANKING = 1 and journal.jo_shelf_id = %s.shelf_id " \
                                     "AND journal.jo_act_id <> 'DELETE')" % (self.tableData.currentTable,
                self.tableData.currentTable)
            elif self.tableData.currentTable == "location":
                self.tableData.sql = "SELECT * FROM %s " \
                                     "JOIN (SELECT jo_loc_id, jo_act_id, " \
                                     "RANK() OVER (PARTITION BY jo_loc_id ORDER by jo_datetime DESC) " \
                                     "RANKING FROM journal) journal " \
                                     "ON (journal.RANKING = 1 and journal.jo_loc_id = %s.loc_id " \
                                     "AND journal.jo_act_id <> 'DELETE')" % (self.tableData.currentTable,
                self.tableData.currentTable)
            elif self.tableData.currentTable == "journal":
                self.tableData.sql = "SELECT * FROM %s" % self.tableData.currentTable
            else:
                pass
        else:
            self.tableData.sql = "SELECT * from %s WHERE " % self.tableData.currentTable + sqllogic
            if self.tableData.currentTable == "document":
                self.stackedWidget.setCurrentIndex(0)
                self.tableData.sql = "SELECT * FROM %s " \
                                     "JOIN (SELECT jo_doc_id, jo_act_id, " \
                                     "RANK() OVER (PARTITION BY jo_doc_id ORDER by jo_datetime DESC) " \
                                     "RANKING FROM journal) journal " \
                                     "ON (journal.RANKING = 1 and journal.jo_doc_id = %s.doc_id " \
                                     "AND journal.jo_act_id <> 'DELETE') WHERE " % (self.tableData.currentTable,
                                                                                    self.tableData.currentTable) \
                                     + sqllogic
            elif self.tableData.currentTable == "project":
                self.stackedWidget.setCurrentIndex(1)
                self.tableData.sql = "SELECT * FROM %s " \
                                     "JOIN (SELECT jo_proj_id, jo_act_id, " \
                                     "RANK() OVER (PARTITION BY jo_proj_id ORDER by jo_datetime DESC) " \
                                     "RANKING FROM journal) journal " \
                                     "ON (journal.RANKING = 1 and journal.jo_proj_id = %s.proj_id " \
                                     "AND journal.jo_act_id <> 'DELETE') WHERE " % (self.tableData.currentTable,
                                                                                    self.tableData.currentTable) \
                                     + sqllogic
            elif self.tableData.currentTable == "folder":
                self.stackedWidget.setCurrentIndex(2)
                self.tableData.sql = "SELECT * FROM %s " \
                                     "JOIN (SELECT jo_folder_id, jo_act_id, " \
                                     "RANK() OVER (PARTITION BY jo_folder_id ORDER by jo_datetime DESC) " \
                                     "RANKING FROM journal) journal " \
                                     "ON (journal.RANKING = 1 and journal.jo_folder_id = %s.folder_id " \
                                     "AND journal.jo_act_id <> 'DELETE') WHERE " % (self.tableData.currentTable,
                                                                                    self.tableData.currentTable) \
                                     + sqllogic
            elif self.tableData.currentTable == "shelf":
                self.stackedWidget.setCurrentIndex(3)
                self.tableData.sql = "SELECT * FROM %s " \
                                     "JOIN (SELECT jo_shelf_id, jo_act_id, " \
                                     "RANK() OVER (PARTITION BY jo_shelf_id ORDER by jo_datetime DESC) " \
                                     "RANKING FROM journal) journal " \
                                     "ON (journal.RANKING = 1 and journal.jo_shelf_id = %s.shelf_id " \
                                     "AND journal.jo_act_id <> 'DELETE') WHERE " % (self.tableData.currentTable,
                                                                                    self.tableData.currentTable) \
                                     + sqllogic
            elif self.tableData.currentTable == "location":
                self.stackedWidget.setCurrentIndex(4)
                self.tableData.sql = "SELECT * FROM %s " \
                                     "JOIN (SELECT jo_loc_id, jo_act_id, " \
                                     "RANK() OVER (PARTITION BY jo_loc_id ORDER by jo_datetime DESC) " \
                                     "RANKING FROM journal) journal " \
                                     "ON (journal.RANKING = 1 and journal.jo_loc_id = %s.loc_id " \
                                     "AND journal.jo_act_id <> 'DELETE') WHERE " % (self.tableData.currentTable,
                                                                                    self.tableData.currentTable) \
                                     + sqllogic
            elif self.tableData.currentTable == "journal":
                self.stackedWidget.setCurrentIndex(5)
                self.tableData.sql = "SELECT * FROM %s WHERE " % self.tableData.currentTable + sqllogic
            else:
                pass
        self.refreshTableViewThread.start()

    def reportSuccess(self):
        self.tableData.df.to_excel("Report.xls")
        self.statusBar().showMessage("Report.xls has been generated on %s" % strftime("%Y-%m-%d %H:%M:%S"))

    def rolesLevelCheck(self):
        if self.roleslevel <= 50:
            self.actionAdd_Document.setDisabled(True)
            self.actionAdd_Project.setDisabled(True)
            self.actionAdd_Folder.setDisabled(True)
            self.actionAdd_Shelf.setDisabled(True)
            self.actionAdd_Location.setDisabled(True)
            self.actionJournal.setDisabled(True)
            self.actionQuery.setDisabled(True)
            self.actionCustom_Report.setDisabled(True)
            self.actionManage_User.setDisabled(True)
            self.actionSystem_Logs.setDisabled(True)
            self.actionImportDocument.setDisabled(True)
            self.actionImportProject.setDisabled(True)
            self.actionImportFolder.setDisabled(True)
            self.actionImportShelf.setDisabled(True)
            self.actionImportLocation.setDisabled(True)
            self.contextAddRecord.setDisabled(True)
            self.contextEditRecord.setDisabled(True)
            self.contextDeleteRecord.setDisabled(True)
        elif self.roleslevel <= 100:
            self.actionAdd_Document.setDisabled(True)
            self.actionAdd_Project.setDisabled(True)
            self.actionAdd_Folder.setDisabled(True)
            self.actionAdd_Shelf.setDisabled(True)
            self.actionAdd_Location.setDisabled(True)
            self.actionJournal.setDisabled(True)
            self.actionQuery.setDisabled(True)
            self.actionCustom_Report.setDisabled(True)
            self.actionManage_User.setDisabled(True)
            self.actionConnection.setDisabled(True)
            self.actionSystem_Logs.setDisabled(True)
            self.actionImportDocument.setDisabled(True)
            self.actionImportProject.setDisabled(True)
            self.actionImportFolder.setDisabled(True)
            self.actionImportShelf.setDisabled(True)
            self.actionImportLocation.setDisabled(True)
            self.contextAddRecord.setDisabled(True)
            self.contextEditRecord.setDisabled(True)
            self.contextDeleteRecord.setDisabled(True)
        elif self.roleslevel <= 400:
            self.actionJournal.setDisabled(True)
            self.actionManage_User.setDisabled(True)
            self.actionConnection.setDisabled(True)
            self.actionSystem_Logs.setDisabled(True)
        elif self.roleslevel <= 800:
            self.actionConnection.setDisabled(True)
            self.actionSystem_Logs.setDisabled(True)
        elif self.roleslevel >= 999:
            pass
        else:
            pass

class RefreshTableView(QThread):
    def __init__(self, parent=None):
        super(RefreshTableView, self).__init__(parent)

    def run(self):
        MainWindow.tableData.refreshData()
        self.emit(SIGNAL("refreshTableView()"))

class GenerateReport(QThread):
    def __init__(self, parent=None):
        super(GenerateReport, self).__init__(parent)

    def run(self):
        MainWindow.tableData.dfToDisplay.to_excel("Report.xls")
        self.emit(SIGNAL("reportSuccess()"))

class TableModel(QAbstractTableModel):
    def __init__(self, parent, tableList, columnHeader, rowHeader, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.tableList = []
        for x in tableList:
            self.tableList.append(self.itemtostring(x))
        self.colHeaderTitle = columnHeader
        self.rowHeaderTitle = rowHeader

    def rowCount(self, parent):
        return len(self.tableList)

    def columnCount(self, parent):
        if len(self.tableList) > 0:
            return len(self.tableList[0])
        else:
            return 0

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.tableList[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return self.rowHeaderTitle[col]
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.colHeaderTitle[col]
        return None

    def sort(self, col, order):
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.tableList = sorted(self.tableList,
            key=operator.itemgetter(col))
        if order == Qt.AscendingOrder:
            self.tableList.reverse()
        self.emit(SIGNAL("layoutChanged()"))

    def itemtostring(self, listuple):     # convert items in list/tuple to string
        # tData adaptation
        listtData = list(listuple)
        # change tData to string instead of unicode
        listuple = tuple([str(z) for z in list(listtData)])

        # tData adaptation
        listtData = list(listuple)
        # replace tData values "" to None
        for n, i in enumerate(list(listtData)):
            if i == "":
                listtData[n] = None
            elif type(i) is int:
                listtData[n] = int(listtData[n])
        return tuple(listtData)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    app.exec_()