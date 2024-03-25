from PySide6 import QtCore
from PySide6.QtWidgets import QWidget
from datetime import datetime

from System.Views.ui_home import Ui_home

class HomeWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setObjectName("home")
        self.ui = Ui_home()
        self.ui.setupUi(self)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(lambda: self.ui.textTime.setText(datetime.now().strftime("%H:%M:%S")))
        self.timer.timeout.connect(lambda: self.ui.textDate.setText(datetime.now().strftime("%Y-%m-%d")))
        self.timer.start()


    def reset(self):
        pass
