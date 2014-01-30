from PySide.QtCore import *
from PySide.QtGui import *
from lib import *
from libs.AboutUI import Ui_AboutPage
import sys

class About(QWidget, Ui_AboutPage):
    def __init__(self, parent=None):
        super(About, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    About = About()
    About.show()
    app.exec_()
