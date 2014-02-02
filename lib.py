import base64
import random
import ConfigParser
from itertools import izip
import datetime

import pandas.io.sql as psql
from Crypto.Cipher import AES
import psycopg2

class crypto:
    def __init__(self):
        self.config = config()
        self.BlockSize = 32
        self.Padding = ']'
        self.pad = lambda s: s + (self.BlockSize - len(s) % self.BlockSize) * self.Padding
        self.encodetoaes = lambda c, s: base64.b64encode(c.encrypt(self.pad(s)))
        self.decodefromaes = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(self.Padding)

    def encode(self, key, content):
        if key == 'AutoGenerate':
            self.maskKey = self.config.read('Local', 'maskKey')
            self.encodeKey = str()
            for i in range(0, self.BlockSize):
                self.encodeKey = self.encodeKey + random.choice(self.maskKey)
            self.encodeKeyAES = AES.new(self.encodeKey)
        else:
            self.encodeKey = key
            self.encodeKeyAES = AES.new(key)
        returnvalue = self.encodetoaes(self.encodeKeyAES, content)
        return returnvalue

    def decode(self, key, content):
        key = AES.new(key)
        return self.decodefromaes(key, content)

class config():
    def __init__(self):
        self.configuration = ConfigParser.ConfigParser()
        self.configuration.readfp(open('settings.ini'))

    def read(self, section, option):
        return self.configuration.get(section, option)

    def update(self, sect, opt, val):
        self.configuration.set(sect, opt, val)
        with open('settings.ini', 'w') as configfile:
            self.configuration.write(configfile)

class db:
    def __init__(self):
        # class variable
        self.config = config()      # config class constructor
        self.crypto = crypto()      # crypto class constructor
        self.maxPage = 0
        self.maxPageSearch = 0
        self.countRows = 0
        self.countRowsSearch = 0
        self.dfList = []
        self.dfListSearch = []
        self.Mode = 1               # 1 for general, 2 for search, 3 for query
        self.dfCurrentTable = ''    # navigate between table variable
        self.headerCol = ''
        self.queryDict = {}
        self.user = "administrator" # logged user session
        self.userlevel = 100        # user roles level

    def connect(self):
        try:
            dbCrypto = crypto()
            self.confHost = self.config.read('Connection', 'host')
            self.confPort = self.config.read('Connection', 'port')
            self.confDbName = self.config.read('Connection', 'dbname')
            self.confUser = self.config.read('Connection', 'username')
            self.confPassKey = self.config.read('Connection', 'passkey')
            self.confPassword = self.config.read('Connection', 'password')
            return psycopg2.connect(host=self.confHost,
                                    port=self.confPort,
                                    dbname=self.confDbName,
                                    user=self.confUser,
                                    password=dbCrypto.decode(self.confPassKey, self.confPassword)
            )
        except:
            return False
    # input: get config from configuration
    # output: psycopg2 connect return

    def insert(self, sTableName, sColumnName, tData):
        # tData adaptation
        listtData = list(tData)
        # change tData to string instead of unicode
        tData = tuple([str(z) for z in list(listtData)])

        # tData adaptation
        listtData = list(tData)
        # replace tData values "" to None
        for n, i in enumerate(list(listtData)):
            if i == "":
                listtData[n] = None
        tData = tuple(listtData)

        iColumnNumber = (sColumnName.count(',')+1) # calculate number of column based on ',' string
        sMagicString = ('%s, '*iColumnNumber)[0:(len('%s, '*iColumnNumber)-2)]
        conn = self.connect()
        try:
            cur = conn.cursor()
            sql = "INSERT INTO %s %s VALUES (%s);" % (sTableName, sColumnName, sMagicString)
            cur.execute(sql, tData)
            cur.close()
            conn.commit()
            conn.close()
            return True
        except:
            return False
    # input: table name, column name, and tuples of data
    # output: True on success, false on exception

    def update(self, sTableName, sColumnName, tData, sColID, sOldRecord):
        # tData adaptation
        listtData = list(tData)
        # change tData to string instead of unicode
        tData = tuple([str(z) for z in list(listtData)])

        # tData adaptation
        listtData = list(tData)
        # replace tData values "" to None
        for n, i in enumerate(list(listtData)):
            if i == "" or i == "None":
                listtData[n] = None
        tData = tuple(listtData)

        iColumnNumber = (sColumnName.count(',')+1) # calculate number of column based on ',' string, +2 to also catch sColumnID & sOldData
        sMagicString = ('%s, '*iColumnNumber)[0:(len('%s, '*iColumnNumber)-2)]
        conn = self.connect()
        try:
            cur = conn.cursor()
            sql = "UPDATE %s SET %s = (%s) WHERE %s = '%s';" % (sTableName, sColumnName, sMagicString, sColID, sOldRecord)
            cur.execute(sql, tData)
            cur.close()
            conn.commit()
            conn.close()
            return True
        except:
            return False
    # input: table name, column name, idvalue, and tuples of data
    # output: True on success, false on exception

    def delete(self, sTableName, sColID, sOldRecord):
        conn = self.connect()
        try:
            cur = conn.cursor()
            sql = "DELETE from %s WHERE %s = '%s';" % (sTableName, sColID, sOldRecord)
            cur.execute(sql)
            cur.close()
            conn.commit()
            conn.close()
            return True
        except:
            return False

    def log(self, tablename, username, act, id, detail, datetime, comment, status):
        stablename = ""
        if tablename == "document":
            stablename = "jo_doc_id"
        elif tablename == "project":
            stablename = "jo_proj_id"
        elif tablename == "folder":
            stablename = "jo_folder_id"
        elif tablename == "shelf":
            stablename = "jo_shelf_id"
        elif tablename == "location":
            stablename = "jo_loc_id"
        else:
            pass
        sColumnName = "(jo_acc_username, jo_act_id, %s, jo_detail, jo_datetime, jo_comment, jo_status)" % stablename
        sMagicString = "('%s', '%s', '%s', '%s', '%s', '%s', %s)" % (username, act, id, detail, datetime, comment, status)
        conn = self.connect()
        try:
            cur = conn.cursor()
            sql = "INSERT INTO journal %s VALUES %s;" % (sColumnName, sMagicString)
            cur.execute(sql)
            cur.close()
            conn.commit()
            conn.close()
            return True
        except:
            return False

    def queryItem(self, sTableName, sColumnName, sString):
        conn = self.connect()
        try:
            cur = conn.cursor()
            sql = "SELECT %s FROM %s WHERE %s = '%s';" % (sColumnName, sTableName, sColumnName, sString)
            cur.execute(sql)
            returnitem = cur.fetchone()[0]
            conn.commit()
            conn.close()
            return returnitem
        except:
            return None

    def queryRecord(self, tablename, indexcol, idrec):
        conn = self.connect()
        self.sql = "SELECT * FROM %s WHERE %s = '%s'" % (tablename, indexcol, idrec)
        self.df = psql.read_frame(self.sql,
                                   con=self.connect()
        )
        self.df = self.df.fillna("")
        returndict = {}
        for record in self.df.to_dict(outtype="list"):
            if type(self.df.to_dict(outtype="list")[record][0]) is datetime.date:
                returndict[record] = self.df.to_dict(outtype="list")[record][0].isoformat()
            else:
                returndict[record] = self.df.to_dict(outtype="list")[record][0]
        return returndict

    def authLogin(self, username, password):
        try:
            conn = self.connect()
            cur = conn.cursor()
            SQL = "SELECT * FROM account WHERE acc_username='%s'" % username
            cur.execute(SQL)
            record = cur.fetchone()
            if (username == record[1] and password == self.crypto.decode(record[3], record[2])):
                return True
            else:
                return False
            cur.close()
            conn.close()
        except:
            if (username == self.crypto.decode(self.config.read("Local", "userkey"), self.config.read("Local", "user")) and (password == self.crypto.decode(self.config.read("Local", "passkey"), self.config.read("Local", "password")))):
                return True
            else:
                return False
    # input username & password
    # output TRUE / FALSE

class data:
    def __init__(self):
        # class constructor
        self.config = config()
        self.crypto = crypto()
        self.db = db()

        # class variable
        self.currentTable = 'document'                  # str, current table
        self.tableIndexCol = {}                         # dict, table index column name
        self.tableTitleCol = {}                         # dict, table title column name
        self.tableCol = {}                              # dict, {"tablename" : "(col 1, col2, ...)"}
        self.tableColList = {}                          # dict, {"tablename" : ["col 1", "col 2", ...]}
        self.columnToDisplay = {}                       # dict, {"tablename" : "(col 1, col2, ...)"}
        self.columnToDisplayList = {}                   # dict, {"tablename" : ["col 1", "col 2", ...]}
        self.columnCount = 0                            # int, column count
        self.rowCount = 0                               # int, row count
        self.horizontalHeaderTitle = {}                 # dict, {"tablename" : ["col 1", "col 2", ...]}
        self.verticalHeaderTitle = {}                   # assigned after dataframe instantiated
        self.mode = 1                                   # int, 1: general, 2: search title, 3: query
        self.totalRecord = 0                            # int, total records
        self.sql = "SELECT * FROM %s " \
                   "JOIN (SELECT jo_doc_id, jo_act_id, " \
                   "RANK() OVER (PARTITION BY jo_doc_id ORDER by jo_datetime DESC) RANKING FROM journal) " \
                   "journal ON (journal.RANKING = 1 and journal.jo_doc_id = %s.doc_id AND journal.jo_act_id <> 'DELETE')" \
                   % (self.currentTable, self.currentTable)

        # init process
        self.initProcess()

    # class function
    def initProcess(self):
        # init process
        listVar1 = []
        listVar2 = []

        # main process
        # update self.tableIndexCol
        for list1 in self.config.read("Database", "indexcol").split("; "):
            for list2 in list1.split(":"):
                listVar1.append(list2)
        i = iter(listVar1)
        self.tableIndexCol = dict(izip(i,i))
        listVar1 = [] # reset list

        # update self.tableTitleCol
        for list1 in self.config.read("Database", "titlecol").split("; "):
            for list2 in list1.split(":"):
                listVar1.append(list2)
        i = iter(listVar1)
        self.tableTitleCol = dict(izip(i,i))
        listVar1 = [] # reset list

        # update self.tableCol
        for list1 in self.config.read("Database", "tablecol").split("; "):
            for list2 in list1.split(":"):
                listVar1.append(list2)
        i = iter(listVar1)
        self.tableCol = dict(izip(i,i))
        listVar1 = [] # reset list

        # update self.tableColList
        for list1 in self.config.read("Database", "tablecol").split("; "):
            for list2 in list1.split(":"):
                if ", " in list2:
                    for list3 in list2.split(", "):
                        listVar1.append(list3)          # list var 1 contains all list values
                    listVar2.append(listVar1)
                else:
                    listVar2.append(list2)
            listVar1 = []   # reset listVar2 in loop
        i = iter(listVar2)
        self.tableColList = dict(izip(i,i))
        listVar1 = [] # reset list
        listVar2 = []

        # update self.columnToDisplay
        for list1 in self.config.read("Display", "coltodisplay").split("; "):
            for list2 in list1.split(":"):
                listVar1.append(list2)
        i = iter(listVar1)
        self.columnToDisplay = dict(izip(i,i))
        listVar1 = [] # reset list

        # update self.columnToDisplayList
        for list1 in self.config.read("Display", "coltodisplay").split("; "):
            for list2 in list1.split(":"):
                if ", " in list2:
                    for list3 in list2.split(", "):
                        listVar1.append(list3)          # listVar1 contains all list values
                    listVar2.append(listVar1)
                else:
                    listVar2.append(list2)
            listVar1 = []   # reset listVar2 in loop
        i = iter(listVar2)
        self.columnToDisplayList = dict(izip(i,i))
        listVar1 = [] # reset list
        listVar2 = []

        # update self.horizontalHeaderTitle
        for list1 in self.config.read("Display", "horheadertitle").split("; "):
            for list2 in list1.split(":"):
                if ", " in list2:
                    for list3 in list2.split(", "):
                        listVar1.append(list3)          # list var 1 contains all list values
                    listVar2.append(listVar1)
                else:
                    listVar2.append(list2)
            listVar1 = []   # reset listVar2 in loop
        i = iter(listVar2)
        self.horizontalHeaderTitle = dict(izip(i,i))
        listVar1 = [] # reset list
        listVar2 = []

    def refreshData(self):
        # update self.df
        try:
            self.df = psql.read_sql(self.sql,
                                       con=self.db.connect(),
                                       index_col=self.tableIndexCol[self.currentTable]
            )
            # update self.dfToDisplay, self.dfList
            self.df = self.df.sort_index()
            self.dfToDisplay = self.df[self.columnToDisplayList[self.currentTable]]
            self.dfToDisplay = self.dfToDisplay.fillna("")
            self.dfList = list(self.dfToDisplay.itertuples(index=False))
            self.rowCount = len(self.dfList)
            self.columnCount = len(self.horizontalHeaderTitle[self.currentTable])
            self.verticalHeaderTitle = [str(items) for items in self.dfToDisplay.index.tolist()]
        except:
            pass