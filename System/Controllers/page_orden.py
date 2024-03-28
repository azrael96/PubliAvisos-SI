from PySide6.QtWidgets import QWidget

from System.Views.ui_orden import Ui_usuarios

class OrdenWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setObjectName("home")
        self.ui = Ui_usuarios()
        self.ui.setupUi(self)

    def reset(self):
        pass
