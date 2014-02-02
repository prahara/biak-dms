import time
from PySide import QtGui
from PySide.QtCore import *
from PySide.QtGui import *
import sys
from lib import *
from libs.LoginScreenUI import Ui_Dialog

__version__ = '0.0.1'

class LoginScreen(QWidget, Ui_Dialog):
    def __init__(self, parent=None):
        super(LoginScreen, self).__init__(parent)
        self.setupUi(self)
        self.BtnLogin.clicked.connect(self.login)
        self.EditUsername.returnPressed.connect(self.login)
        self.EditPassword.returnPressed.connect(self.login)
        self.ConnectionStatus = ConnectionStatus()
        self.ConnectionStatus.start()
        self.connect(self.ConnectionStatus, SIGNAL("Connected()"), self.Connected, Qt.QueuedConnection)
        self.connect(self.ConnectionStatus, SIGNAL("NotConnected()"), self.NotConnected, Qt.QueuedConnection)
        self.username = ''
        self.password = ''

    def login(self):
        self.username = self.EditUsername.text()
        self.password = self.EditPassword.text()
        login = db()
        if login.authLogin(self.username, self.password):
            self.emit(SIGNAL("loginOK()"))
            self.close()
        else:
            QMessageBox.about(self, "Authentication", "Wrong username/password")
            self.emit(SIGNAL("loginFAIL()"))
            self.close()

    def Connected(self):
        self.label_4.setPixmap(QtGui.QPixmap(":/form/network-connect.png"))
    def NotConnected(self):
        self.label_4.setPixmap(QtGui.QPixmap(":/form/network-disconnect.png"))

class ConnectionStatus(QThread):
    def __init__(self, parent=None):
        super(ConnectionStatus, self).__init__(parent)

    def run(self):
        try:
            runConnStatus = db()
            if not runConnStatus.connect() == False:
                ConnStatus = True
            else:
                ConnStatus = False
        except:
            ConnStatus = False
        if ConnStatus:
            self.emit(SIGNAL("Connected()"))
        else:
            while (ConnStatus == False):
                self.emit(SIGNAL("Connected()"))
                time.sleep(0.6)
                self.emit(SIGNAL("NotConnected()"))
                time.sleep(0.6)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    LoginScreen = LoginScreen()
    LoginScreen.show()
    app.exec_()