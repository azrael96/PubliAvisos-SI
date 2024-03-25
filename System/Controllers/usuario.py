from PySide6.QtWidgets import QWidget

from System.Views.ui_usuario import Ui_usuarios

class UsuarioWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setObjectName("home")
        self.ui = Ui_usuarios()
        self.ui.setupUi(self)

    def reset(self):
        pass
