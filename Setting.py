from PySide.QtGui import *
import psycopg2
import sys
from libs.SettingUI import Ui_Setting
from lib import *


class Setting(QWidget, Ui_Setting):
    def __init__(self, parent=None):
        super(Setting, self).__init__(parent)
        self.setupUi(self)
        # class constructor
        self.config = config()
        self.crypto = crypto()

        # load init data to items
        try:
            self.lineEditHostname.setText(self.config.read('Connection', 'host'))
            self.lineEditPort.setText(self.config.read('Connection', 'port'))
            self.lineEditDatabase.setText(self.config.read('Connection', 'dbname'))
            self.lineEditUsername.setText(self.config.read('Connection', 'username'))
            self.lineEditPassword.setText(self.crypto.decode(self.config.read('Connection', 'passkey'),
                self.config.read('Connection', 'password')))
        except:
            pass

        # signal/slot
        self.pushButtonCheckConnection.clicked.connect(self.checkConnection)
        self.pushButtonSave.clicked.connect(self.Save)
        self.pushButtonCancel.clicked.connect(self.Cancel)

        # class variable
        self.success = False

        # items init
        self.pushButtonSave.setDisabled(True)

    def checkConnection(self):
        try:
            psycopg2.connect(host=self.lineEditHostname.text(),
                             port=self.lineEditPort.text(),
                             dbname=self.lineEditDatabase.text(),
                             user=self.lineEditUsername.text(),
                             password=self.lineEditPassword.text())
            self.success = True
            QMessageBox.about(self, 'Success', 'Connection settings are correct. You can now save the settings.')
            self.lineEditHostname.setDisabled(True)
            self.lineEditPort.setDisabled(True)
            self.lineEditDatabase.setDisabled(True)
            self.lineEditUsername.setDisabled(True)
            self.lineEditPassword.setDisabled(True)
            self.pushButtonSave.setDisabled(False)
        except:
            QMessageBox.about(self, 'Error', 'Connection failed, please check connection settings')

    def Save(self):
        if self.success:
            self.config.update('Connection', 'host', self.lineEditHostname.text())
            self.config.update('Connection', 'port', self.lineEditPort.text())
            self.config.update('Connection', 'dbname', self.lineEditDatabase.text())
            self.config.update('Connection', 'username', self.lineEditUsername.text())
            #edit this line below
            self.config.update('Connection', 'password', self.crypto.encode('AutoGenerate', self.lineEditPassword.text()))
            self.config.update('Connection', 'passkey', self.crypto.encodeKey)
            QMessageBox.about(self, 'Success', 'Config file updated')
            self.close()
        else:
            QMessageBox.about(self, 'Warning', 'You should test connection first and get success message to save settings. Good luck!')

    def Cancel(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Setting = Setting()
    Setting.show()
    app.exec_()