#Import the necessary libraries
from sqlalchemy import Column, String
from sqlalchemy.orm import synonym

#Conect with the necessary internal components
from System.Models.db_conector import Base, session

#class that model the database table
class Cliente(Base):
    __tablename__ = "cliente"

    cli_cedula = Column(String(20), primary_key=True)
    cli_nombre1 = Column(String(50))
    cli_nombre2 = Column(String(50))
    cli_apellido1 = Column(String(50))
    cli_apellido2 = Column(String(50))
    cli_direccion = Column(String(50))
    cli_telefono = Column(String(32))
    cli_correo = Column(String(50))
    cli_ubicacion = Column(String(50))

    id = synonym("cli_cedula")
    def __repr__(self):
        return '<Cliente %r>' % self.id
def getListClientes():
    table = Cliente.__table__.columns
    filter = Cliente.cli_cedula != 100000
    query = session.query(table).filter(filter).all()
    return query

def searchCliente(Ced):
    table = Cliente.__table__.columns
    filter = Cliente.cli_cedula == Ced
    query = session.query(table).filter(filter).first()
    return query

def addCliente(Ced, Nom1, Nom2, Ape1, Ape2, Dir, Tel, Cor, Ubi):

    new_cli = Cliente(cli_cedula = Ced,
                      cli_nombre1 = Nom1,
                      cli_nombre2 = Nom2,
                      cli_apellido1 = Ape1,
                      cli_apellido2 = Ape2,
                      cli_direccion = Dir,
                      cli_telefono = Tel,
                      cli_correo = Cor,
                      cli_ubicacion = Ubi
                      )

    session.add(new_cli)
    session.commit()

def updateCliente(Ced, Nom1, Nom2, Ape1, Ape2, Dir, Tel, Cor, Ubi):
    table = Cliente
    filter = Cliente.cli_cedula == Ced
    updated_rec = session.query(table).filter(filter).first()

    updated_rec.cli_nombre1 = Nom1
    updated_rec.cli_nombre2 = Nom2
    updated_rec.cli_apellido1 = Ape1
    updated_rec.cli_apellido2 = Ape2
    updated_rec.cli_direccion = Dir
    updated_rec.cli_telefono = Tel
    updated_rec.cli_correo = Cor
    updated_rec.cli_ubicacion = Ubi
    session.commit()

#Probably need to be eliminated or change cuz of its dependecy on Order
def delClient(Ced):

    table = Cliente
    filter = Cliente.cli_cedula == Ced

    deleted_rec = session.query(table).filter(filter).first()
    session.delete(deleted_rec)
    session.commit()