#Import the necessary libraries
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import synonym

#Conect with the necessary internal components
from System.Models.db_conector import Base
from System.Models.db_cliente import Cliente
from System.Models.db_usuario import Empleado


#class that model the database table
class Cotizacion(Base):
    __tablename__ = "cotizacion"

    cot_ID = Column(Integer, primary_key=True)
    cot_descripcion = Column(String(100))
    cot_valor = Column(Integer)

    cli_cedula_fk = Column(String(20), ForeignKey(Cliente.id))

    id = synonym("cot_ID")
    def __repr__(self):
        return '<Cotizacion %r>' % self.id
