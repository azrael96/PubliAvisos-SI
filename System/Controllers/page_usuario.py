from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QMessageBox
from System.Views.ui_usuario import Ui_usuarios

from System.Models import db_usuario as usuariosData

class UsuarioWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setObjectName("home")
        self.ui = Ui_usuarios()
        self.ui.setupUi(self)

        def switchDelDisable(val):
            self.ui.usuNom1Text.setEnabled(val)
            self.ui.usuNom2Text.setEnabled(val)
            self.ui.usuApe1Text.setEnabled(val)
            self.ui.usuApe2Text.setEnabled(val)
            self.ui.usuCedText.setEnabled(val)
            self.ui.usuUbiText.setEnabled(val)
            self.ui.usuCorrText.setEnabled(val)
            self.ui.usuDirText.setEnabled(val)
            self.ui.usuTelText.setEnabled(val)
            self.ui.usuClearButton.setEnabled(val)

        def selectItem():
            global codigo
            row = self.ui.usuTable.currentRow()

            ced = self.ui.usuTable.item(row, 0).text()
            nom1 = self.ui.usuTable.item(row, 1).text()
            nom2 = self.ui.usuTable.item(row, 2).text()
            ape1 = self.ui.usuTable.item(row, 3).text()
            ape2 = self.ui.usuTable.item(row, 4).text()
            dir = self.ui.usuTable.item(row, 5).text()
            tel = self.ui.usuTable.item(row, 7).text()
            corr = self.ui.usuTable.item(row, 8).text()
            ubi = self.ui.usuTable.item(row, 9).text()
            codigo = ced

            self.ui.usuNom1Text.setText(nom1)
            self.ui.usuNom2Text.setText(nom2)
            self.ui.usuApe1Text.setText(ape1)
            self.ui.usuApe2Text.setText(ape2)
            self.ui.usuCedText.setText(ced)
            self.ui.usuUbiText.setText(ubi)
            self.ui.usuCorrText.setText(corr)
            self.ui.usuDirText.setText(dir)
            self.ui.usuTelText.setText(tel)

        def add():
            global pressed
            pressed = "add"

            self.clear()
            self.clearCod()
            self.switchDisable(True)

        def edit():
            global codigo, pressed
            if codigo != "":
                self.switchDisable(True)
                pressed = "edit"
            else:
                msgBox = QMessageBox()
                ## Add theme to the visuals
                QMessageBox.critical(msgBox, "Error en el proceso", "Seleccione un item de la lista para proceder")

        def delete():
            global codigo, pressed
            if codigo != "":
                self.switchDisable(True)
                switchDelDisable(False)
                pressed = "del"
            else:
                msgBox = QMessageBox()
                ## Add theme to the visuals
                QMessageBox.critical(msgBox, "Error en el proceso", "Seleccione un item de la lista para proceder")

        def cancel():
            self.switchDisable(False)
            self.clear()
            self.clearCod()

        def save():
            global codigo, pressed

            if pressed == "del":
                usuariosData.delEmpleado(codigo)
                switchDelDisable(True)

            ced = self.ui.usuCedText.text()
            nom1 = self.ui.usuNom1Text.text()
            nom2 = self.ui.usuNom2Text.text()
            ape1 = self.ui.usuApe1Text.text()
            ape2 = self.ui.usuApe2Text.text()
            dir = self.ui.usuDirText.text()
            tel = self.ui.usuTelText.text()
            corr = self.ui.usuCorrText.text()
            ubi = self.ui.usuUbiText.text()

            if ced != "" and nom1 != "" and nom2 != "" and ape1 != "" and ape2 != "" and dir != ""\
                    and tel != "" and corr != "" and ubi != "":
                if pressed == "add":
                    usuariosData.addEmpleado(ced, nom1, nom2, ape1, ape2, dir, tel, corr, ubi)
                if pressed == "edit":
                    usuariosData.updateEmpleado(ced, nom1, nom2, ape1, ape2, dir, tel, corr, ubi)
                    self.clearCod()
                self.clear()
                self.fillTable()
                self.switchDisable(False)
            else:
                msgBox = QMessageBox()
                QMessageBox.critical(msgBox, "Error en el guardado", "Llene el formulario completo para continuar")

        self.ui.usuClearButton.clicked.connect(self.clear)
        self.ui.usuSaveButton.clicked.connect(save)
        self.ui.usuCancelButton.clicked.connect(cancel)
        self.ui.usuAddButton.clicked.connect(add)
        self.ui.usuEditButton.clicked.connect(edit)
        self.ui.usuDelButton.clicked.connect(delete)

        self.ui.usuTable.itemClicked.connect(selectItem)
        ## add Stylesheet
        #functions.theme(self.ui.frame, constants.moduleTheme)
        self.reset()

    def reset(self):
        self.clear()
        self.fillTable()
        self.switchDisable(False)

    def clearCod(self):
        global codigo
        codigo = ""
        self.ui.usuTable.setCurrentCell(-1, -1)

    def switchDisable(self, val):
        self.ui.usuNom1Text.setEnabled(val)
        self.ui.usuNom2Text.setEnabled(val)
        self.ui.usuApe1Text.setEnabled(val)
        self.ui.usuApe2Text.setEnabled(val)
        self.ui.usuCedText.setEnabled(val)
        self.ui.usuUbiText.setEnabled(val)
        self.ui.usuCorrText.setEnabled(val)
        self.ui.usuDirText.setEnabled(val)
        self.ui.usuTelText.setEnabled(val)

        self.ui.usuClearButton.setEnabled(val)
        self.ui.usuSaveButton.setEnabled(val)
        self.ui.usuCancelButton.setEnabled(val)

        self.ui.usuTable.setEnabled(not val)
        self.ui.usuEditButton.setEnabled(not val)
        self.ui.usuAddButton.setEnabled(not val)
        self.ui.usuDelButton.setEnabled(not val)

    def clear(self):
        self.ui.usuNom1Text.setText("")
        self.ui.usuNom2Text.setText("")
        self.ui.usuApe1Text.setText("")
        self.ui.usuApe2Text.setText("")
        self.ui.usuCedText.setText("")
        self.ui.usuUbiText.setText("")
        self.ui.usuCorrText.setText("")
        self.ui.usuDirText.setText("")
        self.ui.usuTelText.setText("")

    def fillTable(self):
        data = usuariosData.getListEmpleados()
        dataLen = len(data[0])
        self.clearCod()
        self.ui.usuTable.clear()
        self.ui.usuTable.setColumnCount(dataLen)
        self.ui.usuTable.setRowCount(0)
        self.ui.usuTable.setHorizontalHeaderLabels(["Cedula", "Nombre 1", "Nombre 2", "Apellido 1", "Apellido 2", "Direccion", "Estado", "Telefono", "Correo", "Ubicacion"])

        self.ui.usuTable.setColumnHidden(6, True)

        if len(data) != 0:
            self.ui.usuTable.setRowCount(len(data))
            numrow = 0
            for row in data:
                numcol = 0
                for col in row:
                    self.ui.usuTable.setItem(numrow, numcol, QtWidgets.QTableWidgetItem(str(col)))
                    numcol += 1
                numrow += 1