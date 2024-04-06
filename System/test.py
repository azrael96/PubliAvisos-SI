from PySide6.QtCore import QDate

Inicio_Date = QDate(2024, 4, 1)
Final_Date = QDate(2024, 4, 29)
Actual = QDate().currentDate()

t_total = Inicio_Date.daysTo(Final_Date)
t_gastado = Actual.daysTo(Final_Date)



print(t_total, t_gastado)