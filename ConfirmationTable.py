from PySide.QtGui import *
from PySide.QtCore import *
from libs.ConfirmationTableUI import Ui_ConfirmationTable
from lib import *
import operator
import datetime
import pandas as pd

header = list()
# use numbers for numeric data to sort properly
# the different between show list is: show list>all string while
dataListProcess = list()
dataListSuccess = list()
dataListFailed = list()
mode = 1                    # 1 for insert, 2 for update, 3 for delete
count = 0
tableName = ''
columnNameList = ''
columnNameTuple = ''
colID = ''
oldString = ''
username = ""
log = "Manual Process from GUI"

class ConfirmationTable(QWidget, Ui_ConfirmationTable):
    def __init__(self, parent=None):
        super(ConfirmationTable, self).__init__(parent)
        self.setupUi(self)
        self.username = username
        tableModelProcess = tableModel(self, dataListProcess, header)
        self.tableViewProcess.setModel(tableModelProcess)
        self.tableViewProcess.resizeColumnsToContents()
        self.tableViewProcess.resizeRowsToContents()
        self.tableViewProcess.horizontalHeader().setStretchLastSection(False)
        self.tableViewProcess.horizontalHeader().setResizeMode(1, QHeaderView.Stretch)
        self.processRecordThread = processRecordThread()
        self.processRecordThread.username = self.username
        self.connect(self.processRecordThread, SIGNAL('refreshTableView()'), self.refreshTableView)
        self.connect(self.processRecordThread, SIGNAL('refreshProgressBar()'), self.refreshProgressBar)
        self.BtnProcess.clicked.connect(self.ProcessThreadStart)
        self.BtnCancel.clicked.connect(self.Cancel)
        self.BtnEditAboveRec.clicked.connect(self.EditAboveRec)
        self.LblTotalProcess.setText('Total: ' + str(len(dataListProcess)) + ' record(s)')
        self.BtnReport.setDisabled(True)

    def ProcessThreadStart(self):
        self.processRecordThread.start()

    def refreshProgressBar(self):
        self.progressBar.setValue(count / len(dataListProcess) * 100)

    def refreshTableView(self):
        tableModelSuccess = tableModel(self, dataListSuccess, header)
        self.tableViewSuccess.setModel(tableModelSuccess)
        self.tableViewSuccess.resizeColumnsToContents()
        self.tableViewSuccess.resizeRowsToContents()
        self.tableViewSuccess.horizontalHeader().setStretchLastSection(False)
        self.tableViewSuccess.horizontalHeader().setResizeMode(1, QHeaderView.Stretch)
        self.LblTotalSuccess.setText('Success: ' + str(len(dataListSuccess)) + ' record(s)')
        tableModelProcess = tableModel(self, dataListFailed, header)
        self.tableViewProcess.setModel(tableModelProcess)
        self.tableViewProcess.resizeColumnsToContents()
        self.tableViewProcess.resizeRowsToContents()
        self.tableViewProcess.horizontalHeader().setStretchLastSection(False)
        self.tableViewProcess.horizontalHeader().setResizeMode(1, QHeaderView.Stretch)
        self.LblTotalProcess.setText('Failed: ' + str(len(dataListFailed)) + ' record(s)')

    def Cancel(self):
        self.close()
        self.emit(SIGNAL('closeByCancel()'))

    def EditAboveRec(self):
        self.close()
        self.emit(SIGNAL('reEditRecord()'))

class tableModel(QAbstractTableModel):
    def __init__(self, parent, mylist, headerinput, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = []
        for x in mylist:
            self.mylist.append(self.itemtostring(x))
        self.header = headerinput

    def rowCount(self, parent):
        return len(self.mylist)

    def columnCount(self, parent):
        if len(self.mylist) > 0:
            return len(self.mylist[0])
        else:
            return 0

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.mylist[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    def sort(self, col, order):
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.mylist = sorted(self.mylist,
                             key=operator.itemgetter(col))
        if order == Qt.DescendingOrder:
            self.mylist.reverse()
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

class processRecordThread(QThread):
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.db = db()
        self.username = ""

    def run(self):
        global dataListSuccess, dataListFailed, count
        dataListSuccess = list()
        dataListFailed = list()
        count = 0
        post = db()
        if mode == 1:
            for record in dataListProcess:
                if post.insert(tableName,
                               '%s' % columnNameTuple,
                               record):
                    dataListSuccess.append(record)
                    try:
                        detaillog = {}
                        for k, v in zip(columnNameList, record):
                            detaillog[k] = v
                        post.log(
                            tableName,
                            self.username,
                            "ADD",
                            record[0],
                            str(detaillog).replace("u'", "'").replace("'", "''"),
                            str(datetime.datetime.now()),
                            log,
                            True
                        )
                    except:
                        pass
                else:
                    dataListFailed.append(record)
                    try:
                        detaillog = {}
                        for k, v in zip(columnNameList, record):
                            detaillog[k] = v
                        post.log(
                            tableName,
                            self.username,
                            "ADD",
                            record[0],
                            str(detaillog).replace("u'", "'").replace("'", "''"),
                            str(datetime.datetime.now()),
                            log,
                            False
                        )
                    except:
                        pass
                count += 1
                self.emit(SIGNAL('refreshProgressBar()'))
            self.emit(SIGNAL('refreshTableView()'))
        elif mode == 2:
            for record in dataListProcess:
                if post.update(
                        tableName,
                        '%s' % columnNameTuple,
                        record,
                        colID,
                        oldString[count]
                        ):
                    dataListSuccess.append(record)
                    try:
                        detaillog = {}
                        for k, v in zip(columnNameList, record):
                            detaillog[k] = v
                        post.log(
                            tableName,
                            self.username,
                            self.moveOrEdit(tableName, dataListProcess[0][0], record),
                            record[0],
                            str(detaillog).replace("u'", "'").replace("'", "''"),
                            str(datetime.datetime.now()),
                            "Manual Process from GUI",
                            True
                        )
                    except:
                        pass
                else:
                    dataListFailed.append(record)
                    try:
                        detaillog = {}
                        for k, v in zip(columnNameList, record):
                            detaillog[k] = v
                        post.log(
                            tableName,
                            self.username,
                            self.moveOrEdit(tableName, dataListProcess[0][0], record),
                            record[0],
                            str(detaillog).replace("u'", "'").replace("'", "''"),
                            str(datetime.datetime.now()),
                            "Manual Process from GUI",
                            False
                        )
                    except:
                        pass
                count += 1
                self.emit(SIGNAL('refreshProgressBar()'))
            self.emit(SIGNAL('refreshTableView()'))
        elif mode == 3:
            for record in dataListProcess:
                detaillog = {}
                for k, v in zip(columnNameList, record):
                    detaillog[k] = v
                if post.log(
                    tableName,
                    self.username,
                    "DELETE",
                    record[0],
                    str(detaillog).replace("u'", "'").replace("'", "''"),
                    str(datetime.datetime.now()),
                    "Manual Process from GUI",
                    True
                ):
                    dataListSuccess.append(record)
                else:
                    dataListFailed.append(record)
                    count += 1
                    self.emit(SIGNAL('refreshProgressBar()'))
                self.emit(SIGNAL('refreshTableView()'))
        else:
            pass

    def moveOrEdit(self, tablename, idrec, record):
        if tablename == "document":
            newrecord = self.db.queryRecord(tablename, "doc_id", idrec)
            oldrecord = {}
            for x in zip(columnNameList, record):
                oldrecord[x[0]] = str(x[1]).replace("u'", "'").replace("'", "''")
            newrecord.pop("doc_no", True)
            if (newrecord["doc_folder_id"] != oldrecord["doc_folder_id"] or
                        newrecord["doc_shelf_id"] != oldrecord["doc_shelf_id"] or
                        newrecord["doc_loc_id"] != oldrecord["doc_loc_id"]) and\
                    (newrecord["doc_type"] == oldrecord["doc_type"] and
                             newrecord["doc_proj_id"] == oldrecord["doc_proj_id"] and
                             newrecord["doc_date"] == oldrecord["doc_date"] and
                             newrecord["doc_title"] == oldrecord["doc_title"] and
                             newrecord["doc_id"] == oldrecord["doc_id"] and
                             newrecord["doc_url"] == oldrecord["doc_url"] and
                             newrecord["doc_hardnumber"] == oldrecord["doc_hardnumber"]):
                return "MOVE"
            elif (newrecord["doc_folder_id"] == oldrecord["doc_folder_id"] and
                        newrecord["doc_shelf_id"] == oldrecord["doc_shelf_id"] and
                        newrecord["doc_loc_id"] == oldrecord["doc_loc_id"]) and\
                    (newrecord["doc_type"] != oldrecord["doc_type"] or
                             newrecord["doc_proj_id"] != oldrecord["doc_proj_id"] or
                             newrecord["doc_date"] != oldrecord["doc_date"] or
                             newrecord["doc_title"] != oldrecord["doc_title"] or
                             newrecord["doc_id"] != oldrecord["doc_id"] or
                             newrecord["doc_url"] != oldrecord["doc_url"] or
                             newrecord["doc_hardnumber"] != oldrecord["doc_hardnumber"]):
                return "MODIFY"
            else:
                return  "MOVE AND MODIFY"
        elif tablename == "project":
            return "MODIFY"
        elif tablename == "folder":
            newrecord = self.db.queryRecord(tablename, "folder_id", idrec)
            oldrecord = {}
            for x in zip(columnNameList, record):
                oldrecord[x[0]] = str(x[1]).replace("u'", "'").replace("'", "''")
            if (newrecord["folder_shelf_id"] != oldrecord["folder_shelf_id"] or
                        newrecord["folder_loc_id"] != oldrecord["folder_loc_id"]) and\
                    (newrecord["folder_id"] == oldrecord["folder_id"] and
                             newrecord["folder_title"] == oldrecord["folder_title"]):
                return "MOVE"
            elif (newrecord["folder_shelf_id"] == oldrecord["folder_shelf_id"] and
                        newrecord["folder_loc_id"] == oldrecord["folder_loc_id"]) and\
                    (newrecord["folder_id"] != oldrecord["folder_id"] or
                             newrecord["folder_title"] != oldrecord["folder_title"]):
                return "MODIFY"
            else:
                return "MOVE AND MODIFY"
        elif tablename == "shelf":
            newrecord = self.db.queryRecord(tablename, "shelf_id", idrec)
            oldrecord = {}
            for x in zip(columnNameList, record):
                oldrecord[x[0]] = str(x[1]).replace("u'", "'").replace("'", "''")
            if (newrecord["shelf_loc_id"] != oldrecord["shelf_loc_id"]) and\
                    (newrecord["shelf_id"] == oldrecord["shelf_id"] and
                             newrecord["shelf_title"] == oldrecord["shelf_title"]):
                return "MOVE"
            elif (newrecord["shelf_loc_id"] == oldrecord["shelf_loc_id"]) and\
                    (newrecord["shelf_id"] != oldrecord["shelf_id"] or
                             newrecord["shelf_title"] != oldrecord["shelf_title"]):
                return "MODIFY"
            else:
                return "MOVE AND MODIFY"
        elif tablename == "location":
            return "MODIFY"
        else:
            pass