from PySide6.QtCore import QDate, Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QProgressBar

from System.Views.ui_orden import Ui_usuarios
from System.Controllers.clienteDialog import ClientDialog
from System.Models import db_orden as ordenesData
from System.Models import db_usuario as usuariosData
from System.Models import db_cliente as clientesData

cat_dic = {}
MinDate = QDate(2000, 1, 1)
class OrdenWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setObjectName("home")
        self.ui = Ui_usuarios()
        self.ui.setupUi(self)

        def switchDelDisable(val):
            self.ui.ordCliText.setEnabled(False)
            self.ui.ordRecDate.setEnabled(val)
            self.ui.ordEntDate.setEnabled(val)
            self.ui.ordEstText.setEnabled(False)

            self.ui.ordCliButton.setEnabled(val)
            self.ui.ordResCombo.setEnabled(val)
            self.ui.ordValText.setEnabled(val)
            self.ui.ordDesText.setEnabled(val)

            self.ui.ordClearButton.setEnabled(val)

        def selectItem():
            global codigo
            row = self.ui.ordTable.currentRow()

            ID = self.ui.ordTable.item(row, 0).text()
            est = self.ui.ordTable.item(row, 1).text()
            des = self.ui.ordTable.item(row, 2).text()
            val = self.ui.ordTable.item(row, 3).text()
            ent = self.ui.ordTable.item(row, 4).text()
            rec = self.ui.ordTable.item(row, 5).text()
            cli = self.ui.ordTable.item(row, 6).text()
            emp = self.ui.ordTable.item(row, 7).text()
            codigo = ID

            self.ui.ordCliText.setText(cli)
            recDate = QDate.fromString(rec, "yyyy-MM-dd")
            entDate = QDate.fromString(ent, "yyyy-MM-dd")
            self.ui.ordRecDate.setDate(recDate)
            self.ui.ordEntDate.setDate(entDate)

            self.ui.ordValText.setText(val)
            self.ui.ordDesText.setText(des)

            self.ui.ordResCombo.setCurrentText(cat_dic[emp])

            t_total = recDate.daysTo(entDate)
            t_gastado = recDate.currentDate().daysTo(entDate)

            self.ui.progressBar.setMaximum(t_total)
            self.ui.progressBar.setValue(t_total-t_gastado)
            self.ui.ordEstText.setText("Quedan " + str(t_gastado) + " dias de "+ str(t_total) +" para entregar")

            if t_gastado < t_total*0.5:
                self.ui.progressBar.setStyleSheet(
                    '''QProgressBar { border-color:  rgb(223, 0, 0); }
                    QProgressBar::chunk { background-color: rgb(223, 48, 48); }''')
            elif t_gastado < t_total*0.75:
                self.ui.progressBar.setStyleSheet(
                    '''QProgressBar { border-color:  rgb(255, 170, 0); }
                    QProgressBar::chunk { background-color: rgb(255, 188, 55); }''')
            elif t_gastado <= t_total:
                self.ui.progressBar.setStyleSheet(
                    '''QProgressBar { border-color:  rgb(0, 221, 0); }
                    QProgressBar::chunk { background-color: rgb(48, 221, 48); }''')

        def add():
            global pressed
            pressed = "add"

            self.clear()
            self.clearCod()
            self.switchDisable(True)

        def edit():
            pass

        def delete():
            pass

        def cancel():
            self.switchDisable(False)
            self.clear()
            self.clearCod()

        def save():
            global codigo, pressed

            if pressed == "del":
                ordenesData.delOrden(codigo)
                switchDelDisable(True)

            est = self.ui.ordEstText.text()
            des = self.ui.ordDesText.toPlainText()
            val = self.ui.ordValText.text()
            ent = self.ui.ordEntDate.date().toString("yyyy-MM-dd")
            rec = self.ui.ordRecDate.date().toString("yyyy-MM-dd")
            cli = self.ui.ordCliText.text()

            emp = self.ui.ordResCombo.currentText()
            res_emp = dict((v, k) for k, v in cat_dic.items()).get(emp)

            if est != "" and des != "" and val != "" and ent != "" and dir != ""\
                    and rec != "" and cli != "" and emp != "":
                if pressed == "add":
                    ordenesData.addOrden(des, val, ent, rec, cli, res_emp)
                if pressed == "edit":
                    ordenesData.updateOrden(codigo, est, des, val, ent, rec, cli, res_emp)
                    self.clearCod()
                self.clear()
                self.fillTable()
                self.switchDisable(False)
            else:
                msgBox = QMessageBox()
                QMessageBox.critical(msgBox, "Error en el guardado", "Llene el formulario completo para continuar")

        def changeCliente():
            dlgClient = ClientDialog()
            dlgClient.exec()
            cli = dlgClient.ui.usuCedText.text()
            self.ui.ordCliText.setText(cli)
            return cli

        self.ui.ordClearButton.clicked.connect(self.clear)
        self.ui.ordSaveButton.clicked.connect(save)
        self.ui.ordCancelButton.clicked.connect(cancel)
        self.ui.ordAddButton.clicked.connect(add)
        self.ui.ordEditButton.clicked.connect(edit)
        self.ui.ordDelButton.clicked.connect(delete)
        self.ui.ordCliButton.clicked.connect(changeCliente)
        self.ui.ordTable.itemClicked.connect(selectItem)
        ## add Stylesheet
        #functions.theme(self.ui.frame, constants.moduleTheme)
        self.reset()

    def reset(self):
        self.clear()
        self.fillTable()
        self.fillCombo()
        self.switchDisable(False)

    def clearCod(self):
        global codigo
        codigo = ""
        self.ui.ordTable.setCurrentCell(-1, -1)

    def switchDisable(self, val):
        self.ui.ordCliText.setEnabled(False)
        self.ui.ordRecDate.setEnabled(val)
        self.ui.ordEntDate.setEnabled(val)
        self.ui.ordEstText.setEnabled(False)

        self.ui.ordCliButton.setEnabled(val)
        self.ui.ordResCombo.setEnabled(val)
        self.ui.ordValText.setEnabled(val)
        self.ui.ordDesText.setEnabled(val)

        self.ui.ordClearButton.setEnabled(val)
        self.ui.ordSaveButton.setEnabled(val)
        self.ui.ordCancelButton.setEnabled(val)

        self.ui.ordTable.setEnabled(not val)
        self.ui.ordEditButton.setEnabled(not val)
        self.ui.ordAddButton.setEnabled(not val)
        self.ui.ordDelButton.setEnabled(not val)

    def clear(self):
        self.ui.ordCliText.setText("")
        self.ui.ordEstText.setText("ACTIVO")
        self.ui.ordRecDate.setDate(MinDate)
        self.ui.ordEntDate.setDate(MinDate)
        self.ui.ordValText.setText("")
        self.ui.ordDesText.setText("")

        self.ui.ordResCombo.setCurrentIndex(-1)

    def fillCombo(self):
        data = usuariosData.getListEmpleados()
        if len(data) != 0:
            global cat_dic
            cat_list = []
            for row in data:
                cat_dic[row[0]] = row[1] + " " + row[3]
                cat_list.append(self.tr(row[1] + " " + row[3]))

            self.ui.ordResCombo.clear()
            self.ui.ordResCombo.addItems(cat_list)
            self.ui.ordResCombo.setCurrentIndex(-1)

    def fillTable(self):
        data = ordenesData.getListOrdenes()
        dataLen = len(data[0])
        self.clearCod()
        self.ui.ordTable.clear()
        self.ui.ordTable.setColumnCount(dataLen+2)
        self.ui.ordTable.setRowCount(0)
        self.ui.ordTable.setHorizontalHeaderLabels(["Codigo", "Estado", "Descripcion", "Valor", "Entrega", "Recepcion",
                                                    "ClienteID", "EmpleadoID", "Cliente", "Empleado"])

        self.ui.ordTable.setColumnHidden(1, True)
        self.ui.ordTable.setColumnHidden(2, True)
        self.ui.ordTable.setColumnHidden(3, True)
        self.ui.ordTable.setColumnHidden(6, True)
        self.ui.ordTable.setColumnHidden(7, True)

        if len(data) != 0:
            self.ui.ordTable.setRowCount(len(data))
            numrow = 0
            for row in data:
                numcol = 0
                for col in row:
                    self.ui.ordTable.setItem(numrow, numcol, QTableWidgetItem(str(col)))
                    numcol += 1
                cliente = clientesData.searchCliente(data[numrow][6])
                empleado = usuariosData.searchEmpleado(data[numrow][7])
                clienteNombre =cliente[1]+" "+cliente[3]
                empleadoNombre =empleado[1]+" "+empleado[3]
                self.ui.ordTable.setItem(numrow, 8, QTableWidgetItem(str(clienteNombre)))
                self.ui.ordTable.setItem(numrow, 9, QTableWidgetItem(str(empleadoNombre)))
                numrow += 1
        self.ui.ordTable.resizeColumnsToContents()
        self.ui.ordTable.sortItems(4, Qt.AscendingOrder)
