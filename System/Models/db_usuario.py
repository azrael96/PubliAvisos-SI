#Import the necessary libraries
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import synonym

#Conect with the necessary internal components
from System.Models.db_conector import Base, session


#class that model the database table
class Empleado(Base):
    __tablename__ = "empleado"

    emp_cedula = Column(String(20), primary_key=True)
    emp_nombre1 = Column(String(50))
    emp_nombre2 = Column(String(50))
    emp_apellido1 = Column(String(50))
    emp_apellido2 = Column(String(50))
    emp_direccion = Column(String(50))
    emp_activo = Column(Boolean)
    emp_telefono = Column(String(32))
    emp_correo = Column(String(50))
    emp_ubicacion = Column(String(50))

    id = synonym("emp_cedula")
    def __repr__(self):
        return '<Empleado %r>' % self.id

def getListEmpleados():
    table = Empleado.__table__.columns
    filter = Empleado.emp_activo != False
    query = session.query(table).filter(filter).all()
    return query

def searchEmpleado(Ced):
    table = Empleado.__table__.columns
    filter = Empleado.emp_cedula == Ced
    query = session.query(table).filter(filter).first()
    return query

def addEmpleado(Ced, Nom1, Nom2, Ape1, Ape2, Dir, Tel, Cor, Ubi):

    new_emp = Empleado(emp_cedula = Ced,
                      emp_nombre1 = Nom1,
                      emp_nombre2 = Nom2,
                      emp_apellido1 = Ape1,
                      emp_apellido2 = Ape2,
                      emp_direccion = Dir,
                      emp_activo = True,
                      emp_telefono = Tel,
                      emp_correo = Cor,
                      emp_ubicacion = Ubi
                       )

    session.add(new_emp)
    session.commit()

def updateEmpleado(Ced, Nom1, Nom2, Ape1, Ape2, Dir, Tel, Cor, Ubi):

    table = Empleado
    filter = Empleado.emp_cedula == Ced
    updated_rec = session.query(table).filter(filter).first()

    updated_rec.emp_nombre1 = Nom1
    updated_rec.emp_nombre2 = Nom2
    updated_rec.emp_apellido1 = Ape1
    updated_rec.emp_apellido2 = Ape2
    updated_rec.emp_direccion = Dir
    updated_rec.emp_telefono = Tel
    updated_rec.emp_correo = Cor
    updated_rec.emp_ubicacion = Ubi
    session.commit()

def deactivateEmpleado(Ced):

    table = Empleado
    filter = Empleado.emp_cedula == Ced

    updated_rec = session.query(table).filter(filter).first()
    updated_rec.emp_activo = False

    session.commit()

#Probably need to be eliminated or change cuz of its dependecy on Order
def delEmpleado(Ced):

    table = Empleado
    filter = Empleado.emp_cedula == Ced

    deleted_rec = session.query(table).filter(filter).first()
    session.delete(deleted_rec)
    session.commit()
