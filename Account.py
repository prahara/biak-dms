from PySide.QtCore import *
from PySide.QtGui import *
from lib import *
from libs.AccountUI import Ui_Account
import sys
import operator

class Account(QWidget, Ui_Account):
    def __init__(self, parent=None):
        super(Account, self).__init__(parent)
        self.setupUi(self)
        # class constructor
        self.tableData = data()
        self.db = db()
        self.crypto = crypto()
        self.mode = 1           # 1: add user, 2: edit user
        self.username = ""
        self.roleslevel = 0

        # init
        self.refreshTableView()

        # signal
        self.pushButtonAdd.clicked.connect(lambda: self.decorAddUser())
        self.pushButtonSave.clicked.connect(lambda: self.addUser())
        self.pushButtonCancel.clicked.connect(lambda: self.disableAll())
        self.pushButtonEdit.clicked.connect(lambda: self.editUser())
        self.pushButtonDelete.clicked.connect(lambda: self.deleteUser())

    # function
    def refreshTableView(self):
        try:
            self.tableData.currentTable = "account"
            self.tableData.sql = "SELECT * FROM account WHERE acc_roles_level <= %s" % self.roleslevel
            self.tableData.refreshData()
            # var
            self.tableList = self.tableData.dfList
            # table model update
            self.tableModel = tableModel(self,
                                    self.tableData.dfList,
                                    self.tableData.horizontalHeaderTitle[self.tableData.currentTable],
                                    self.tableData.verticalHeaderTitle
            )
            # table decor
            self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
            self.tableView.setModel(self.tableModel)
            self.tableView.setSortingEnabled(True)
            self.tableView.resizeColumnsToContents()
            self.tableView.resizeRowsToContents()
            self.tableView.horizontalHeader().setResizeMode(0, QHeaderView.Stretch)
            if self.roleslevel == 999:
                index = 3
            elif self.roleslevel == 800:
                self.comboBox0acc_roles_level.removeItem(3)
                index = 2
            elif self.roleslevel == 400:
                self.comboBox0acc_roles_level.removeItem(3)
                self.comboBox0acc_roles_level.removeItem(2)
                index = 1
            elif self.roleslevel == 100:
                self.comboBox0acc_roles_level.removeItem(3)
                self.comboBox0acc_roles_level.removeItem(2)
                self.comboBox0acc_roles_level.removeItem(1)
        except:
            pass

    def addUser(self):
        inserttuple = (
            self.lineEdit0acc_username.text(),
            self.crypto.encode("AutoGenerate", self.lineEdit0acc_password.text()),
            self.crypto.encodeKey,
            int(self.comboBox0acc_roles_level.currentText())
        )
        if self.mode == 1:
            if inserttuple[3] >= self.roleslevel:
                QMessageBox.about(self, "Failed", "You can't add user having the same roles level")
            else:
                if self.db.insert("account",
                                  "(acc_username, acc_password, acc_passkey, acc_roles_level)",
                                  inserttuple
                ):
                    QMessageBox.about(self, "Success", "Account: %s added" % inserttuple[0])
                else:
                    QMessageBox.about(self, "Failed", "Account add failed")
        elif self.mode == 2:
            if inserttuple[3] >= self.roleslevel:
                QMessageBox.about(self, "Failed", "You can't edit user having the same roles level. "
                                                  "If you just want to change your password, please use "
                                                  "Change Password instead")
            else:
                if self.db.update("account",
                                  "(acc_username, acc_password, acc_passkey, acc_roles_level)",
                                  inserttuple,
                                  "acc_username",
                                  self.lineEdit0acc_username.text()):
                    QMessageBox.about(self, "Success", "Account: %s edited" % inserttuple[0])
                else:
                    QMessageBox.about(self, "Failed", "Account edit failed")
        else:
            pass
        self.refreshTableView()
        self.disableAll()
        self.mode = 1

    def editUser(self):
        self.mode = 2
        self.editList = []
        for selected in self.tableView.selectionModel().selectedRows():
            if self.tableData.df.ix[self.tableData.df[
                self.tableData.df["acc_username"] == selected.data()
            ].index.tolist()[0]].tolist() not in self.editList:
                self.editList.append(
                    self.tableData.df.ix[self.tableData.df[
                        self.tableData.df["acc_username"] == selected.data()
                        ].index.tolist()[0]].to_dict()
                )
        self.decorAddUser()
        self.lineEdit0acc_username.setEnabled(False)
        self.lineEdit0acc_username.setText(str(self.editList[0]["acc_username"]))
        self.lineEdit0acc_password.setText(str(
            self.crypto.decode(self.editList[0]["acc_passkey"], self.editList[0]["acc_password"])
        ))
        if self.editList[0]["acc_roles_level"] == 999:
            index = 3
        elif self.editList[0]["acc_roles_level"] == 800:
            index = 2
        elif self.editList[0]["acc_roles_level"] == 400:
            index = 1
        elif self.editList[0]["acc_roles_level"] == 100:
            index = 0
        else:
            index = 0
        self.comboBox0acc_roles_level.setCurrentIndex(index)

    def deleteUser(self):
        self.editList = []
        for selected in self.tableView.selectionModel().selectedRows():
            if self.tableData.df.ix[self.tableData.df[
                self.tableData.df["acc_username"] == selected.data()
            ].index.tolist()[0]].tolist() not in self.editList:
                self.editList.append(
                    self.tableData.df.ix[self.tableData.df[
                        self.tableData.df["acc_username"] == selected.data()
                        ].index.tolist()[0]].to_dict()
                )
        ret = QMessageBox.question(self,
                          "Confirmation",
                          "Are you sure do you want to delete %s" % self.editList[0]["acc_username"],
                          QMessageBox.No | QMessageBox.Yes
        )
        if ret == QMessageBox.Yes:
            self.db.delete(
                "account",
                "acc_username",
                self.editList[0]["acc_username"]
            )
        elif ret == QMessageBox.No:
            pass
        else:
            pass
        self.refreshTableView()

    def decorAddUser(self):
        self.lineEdit0acc_username.clear()
        self.lineEdit0acc_password.clear()
        self.comboBox0acc_roles_level.setCurrentIndex(0)
        self.lineEdit0acc_username.setEnabled(True)
        self.lineEdit0acc_password.setEnabled(True)
        self.comboBox0acc_roles_level.setEnabled(True)
        self.pushButtonSave.setEnabled(True)
        self.pushButtonCancel.setEnabled(True)

    def disableAll(self):
        self.decorAddUser()
        self.lineEdit0acc_username.setEnabled(False)
        self.lineEdit0acc_password.setEnabled(False)
        self.comboBox0acc_roles_level.setEnabled(False)
        self.pushButtonSave.setEnabled(False)
        self.pushButtonCancel.setEnabled(False)

class tableModel(QAbstractTableModel):
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
    Account = Account()
    Account.show()
    app.exec_()
