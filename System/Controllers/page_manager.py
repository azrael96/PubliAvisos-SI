import sys

from System.Models import functions

from System.Views.ui_manager import Ui_MainWindow as Ui_ManagerWindow

from System.Controllers.page_home import HomeWidget
from System.Controllers.page_cliente import ClienteWidget
from System.Controllers.page_usuario import UsuarioWidget
from System.Controllers.page_orden import OrdenWidget

from PySide6.QtCore import QEvent, QTimer
from PySide6.QtGui import Qt, QColor, QIcon
from PySide6.QtWidgets import QMainWindow, QGraphicsDropShadowEffect, QSizeGrip, QPushButton, QApplication

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ManagerWindow()
        self.ui.setupUi(self)

        # CREATE THE MODULES
        self.moduleHome = HomeWidget()
        self.moduleCliente = ClienteWidget()
        self.moduleUsuario = UsuarioWidget()
        self.moduleOrden = OrdenWidget()

        def configEvents():
            # DOUBLE CLICK TO MAXIMIZE
            def dobleClickMaximizeRestore(event):
                if event.type() == QEvent.MouseButtonDblClick:
                    QTimer.singleShot(250, lambda: functions.maximize_restore(self))

            # MOVE WINDOW / MAXIMIZE / RESTORE
            def moveWindow(event):
                # IF MAXIMIZED CHANGE TO NORMAL
                if functions.returnStatus(self):
                    functions.maximize_restore(self)
                # MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
                    self.dragPos = event.globalPosition().toPoint()
                    event.accept()

            self.ui.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore
            self.ui.titleRightInfo.mouseMoveEvent = moveWindow

        def configVisual():

            #BASIC ATRIBUTES
            #self.setWindowTitle(constants.title)
            #self.ui.titleRightInfo.setText(constants.manager)
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground, True)

            # DROP SHADOW
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(0)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 100, 0, 150))
            self.ui.bgApp.setGraphicsEffect(self.shadow)

            # RESIZE WINDOW
            self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
            self.sizegrip.setStyleSheet("width: 20px; height: 20px;")

            # SET CUSTOM THEME
            #functions.theme(self.ui.styleSheet, constants.mainTheme)

        def configButtons():
            # EXTRA LEFT BOX
            def openCloseLeftBox():
                functions.toggleLeftBox(self, True)

            # EXTRA RIGHT BOX
            def openCloseRightBox():
                functions.toggleRightBox(self, True)

            # OPEN MENU BUTTONS
            self.ui.toggleButton.clicked.connect(lambda: functions.toggleMenu(self, True))
            self.ui.toggleLeftBox.clicked.connect(openCloseLeftBox)
            self.ui.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)
            self.ui.settingsTopBtn.clicked.connect(openCloseRightBox)

            # MINIMIZE
            self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

            # MAXIMIZE
            self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: functions.maximize_restore(self))

            # CLOSE APPLICATION
            self.ui.closeAppBtn.clicked.connect(lambda: self.close())
            #Make invisible no use buttons
            #self.ui.closeAppBtn.setVisible(False)
            #self.ui.settingsTopBtn.setVisible(False)

            # LEFT MENUS
            self.ui.btn_home.clicked.connect(self.buttonClick)
            self.ui.btn_cliente.clicked.connect(self.buttonClick)
            self.ui.btn_usuario.clicked.connect(self.buttonClick)
            self.ui.btn_orden.clicked.connect(self.buttonClick)
            self.ui.btn_reporte.clicked.connect(self.buttonClick)

        def configModules():
            # ADD THE SYSTEM MODULES
            self.ui.stackedWidget.addWidget(self.moduleHome)
            self.ui.stackedWidget.addWidget(self.moduleCliente)
            self.ui.stackedWidget.addWidget(self.moduleUsuario)
            self.ui.stackedWidget.addWidget(self.moduleOrden)
            #self.ui.stackedWidget.addWidget(self.moduleReporte)

            # SET THE STARTING MODULE
            self.ui.stackedWidget.setCurrentWidget(self.moduleHome)

        # BASIC CONFIGURATION
        configModules()
        configEvents()
        configVisual()
        configButtons()

        #SHOW THE WINDOW
        self.show()


    # MENU BUTTONS FUNCTIONS
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SELECT MENU STYLE
        def selectMenu(getStyle):
            select = getStyle + functions.MENU_SELECTED_STYLESHEET
            return select

        # DESELECT MENU STYLE
        def deselectMenu(getStyle):
            deselect = getStyle.replace(functions.MENU_SELECTED_STYLESHEET, "")
            return deselect

        # RESET SELECTION
        def resetStyle(widget):
            for w in self.ui.topMenu.findChildren(QPushButton):
                if w.objectName() != widget:
                    w.setStyleSheet(deselectMenu(w.styleSheet()))


        # CONNECT MENU BUTTONS TO WIDGET
        if btnName == "btn_home":
            self.moduleHome.reset()
            self.ui.stackedWidget.setCurrentWidget(self.moduleHome)

        if btnName == "btn_cliente":
            self.moduleCliente.reset()
            self.ui.stackedWidget.setCurrentWidget(self.moduleCliente)

        if btnName == "btn_usuario":
            self.moduleUsuario.reset()
            self.ui.stackedWidget.setCurrentWidget(self.moduleUsuario)

        if btnName == "btn_orden":
            self.moduleOrden.reset()
            self.ui.stackedWidget.setCurrentWidget(self.moduleOrden)

        if btnName == "btn_reporte":
            pass
            #self.moduleReporte.reset()
            #self.ui.stackedWidget.setCurrentWidget(self.moduleReporte)

        resetStyle(btnName)
        btn.setStyleSheet(selectMenu(btn.styleSheet()))

    # MOUSE CLICK EVENTS
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("images/images/Icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())