#Import the necessary libraries
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import synonym

#Conect with the necessary internal components
from System.Models.db_conector import Base
from System.Models.db_orden import Orden


#class that model the database table
class Registro(Base):
    __tablename__ = "registro"

    reg_ID = Column(Integer, primary_key=True)
    reg_fechaCambio = Column(Date)
    reg_descripcion = Column(String(100))

    ord_ID_fk = Column(Integer, ForeignKey(Orden.id))

    id = synonym("reg_ID")
    def __repr__(self):
        return '<Registro %r>' % self.id