from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from System.Views.ui_cliente import Ui_usuarios

from System.Models import db_cliente as clientesData

class ClienteWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setObjectName("home")
        self.ui = Ui_usuarios()
        self.ui.setupUi(self)

        def switchDelDisable(val):
            self.ui.cliNom1Text.setEnabled(val)
            self.ui.cliNom2Text.setEnabled(val)
            self.ui.cliApe1Text.setEnabled(val)
            self.ui.cliApe2Text.setEnabled(val)
            self.ui.cliUbiText.setEnabled(val)
            self.ui.cliCorrText.setEnabled(val)
            self.ui.cliDirText.setEnabled(val)
            self.ui.cliTelText.setEnabled(val)
            self.ui.usuClearButton.setEnabled(val)
            self.ui.cliCedText.setEnabled(False)

        def selectItem():
            global codigo
            row = self.ui.cliTable.currentRow()

            ced = self.ui.cliTable.item(row, 0).text()
            nom1 = self.ui.cliTable.item(row, 1).text()
            nom2 = self.ui.cliTable.item(row, 2).text()
            ape1 = self.ui.cliTable.item(row, 3).text()
            ape2 = self.ui.cliTable.item(row, 4).text()
            dir = self.ui.cliTable.item(row, 5).text()
            tel = self.ui.cliTable.item(row, 6).text()
            corr = self.ui.cliTable.item(row, 7).text()
            ubi = self.ui.cliTable.item(row, 8).text()
            codigo = ced

            self.ui.cliNom1Text.setText(nom1)
            self.ui.cliNom2Text.setText(nom2)
            self.ui.cliApe1Text.setText(ape1)
            self.ui.cliApe2Text.setText(ape2)
            self.ui.cliCedText.setText(ced)
            self.ui.cliUbiText.setText(ubi)
            self.ui.cliCorrText.setText(corr)
            self.ui.cliDirText.setText(dir)
            self.ui.cliTelText.setText(tel)

        def add():
            global pressed
            pressed = "add"

            self.clear()
            self.clearCod()
            self.switchDisable(True)
            self.ui.cliCedText.setEnabled(True)

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
                clientesData.delClient(codigo)
                switchDelDisable(True)

            ced = self.ui.cliCedText.text()
            nom1 = self.ui.cliNom1Text.text()
            nom2 = self.ui.cliNom2Text.text()
            ape1 = self.ui.cliApe1Text.text()
            ape2 = self.ui.cliApe2Text.text()
            dir = self.ui.cliDirText.text()
            tel = self.ui.cliTelText.text()
            corr = self.ui.cliCorrText.text()
            ubi = self.ui.cliUbiText.text()

            if ced != "" and nom1 != "" and nom2 != "" and ape1 != "" and ape2 != "" and dir != ""\
                    and tel != "" and corr != "" and ubi != "":
                if pressed == "add":
                    clientesData.addCliente(ced, nom1, nom2, ape1, ape2, dir, tel, corr, ubi)
                if pressed == "edit":
                    clientesData.updateCliente(ced, nom1, nom2, ape1, ape2, dir, tel, corr, ubi)
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

        self.ui.cliTable.itemClicked.connect(selectItem)
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
        self.ui.cliTable.setCurrentCell(-1, -1)

    def switchDisable(self, val):

        self.ui.cliCedText.setEnabled(False)
        self.ui.cliNom1Text.setEnabled(val)
        self.ui.cliNom2Text.setEnabled(val)
        self.ui.cliApe1Text.setEnabled(val)
        self.ui.cliApe2Text.setEnabled(val)
        self.ui.cliUbiText.setEnabled(val)
        self.ui.cliCorrText.setEnabled(val)
        self.ui.cliDirText.setEnabled(val)
        self.ui.cliTelText.setEnabled(val)

        self.ui.usuClearButton.setEnabled(val)
        self.ui.usuSaveButton.setEnabled(val)
        self.ui.usuCancelButton.setEnabled(val)

        self.ui.cliTable.setEnabled(not val)
        self.ui.usuEditButton.setEnabled(not val)
        self.ui.usuAddButton.setEnabled(not val)
        self.ui.usuDelButton.setEnabled(not val)

    def clear(self):
        self.ui.cliNom1Text.setText("")
        self.ui.cliNom2Text.setText("")
        self.ui.cliApe1Text.setText("")
        self.ui.cliApe2Text.setText("")
        self.ui.cliCedText.setText("")
        self.ui.cliUbiText.setText("")
        self.ui.cliCorrText.setText("")
        self.ui.cliDirText.setText("")
        self.ui.cliTelText.setText("")

    def fillTable(self):
        data = clientesData.getListClientes()
        dataLen = len(data[0])
        self.clearCod()
        self.ui.cliTable.clear()
        self.ui.cliTable.setColumnCount(dataLen)
        self.ui.cliTable.setRowCount(0)
        self.ui.cliTable.setHorizontalHeaderLabels(["Cedula", "Nombre 1", "Nombre 2", "Apellido 1", "Apellido 2", "Direccion", "Estado", "Telefono", "Correo", "Ubicacion"])

        #self.ui.usuTable.setColumnHidden(6, True)

        if len(data) != 0:
            self.ui.cliTable.setRowCount(len(data))
            numrow = 0
            for row in data:
                numcol = 0
                for col in row:
                    self.ui.cliTable.setItem(numrow, numcol, QTableWidgetItem(str(col)))
                    numcol += 1
                numrow += 1
