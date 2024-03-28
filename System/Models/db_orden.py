#Import the necessary libraries
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import synonym

#Conect with the necessary internal components
from System.Models.db_conector import Base
from System.Models.db_cliente import Cliente
from System.Models.db_usuario import Empleado


#class that model the database table
class Orden(Base):
    __tablename__ = "orden"

    ord_ID = Column(Integer, primary_key=True)
    ord_estado = Column(String(50))
    ord_descripcion = Column(String(100))
    ord_valor = Column(Integer)
    ord_fechaEntrega = Column(Date)
    ord_fechaRecepcion = Column(Date)

    cli_cedula_fk = Column(String(20), ForeignKey(Cliente.id))
    emp_cedula_fk = Column(String(20), ForeignKey(Empleado.id))

    id = synonym("ord_ID")
    def __repr__(self):
        return '<Orden %r>' % self.id
