#Import the necessary libraries
from sqlalchemy import Column, String, Integer, Date, ForeignKey, func
from sqlalchemy.orm import synonym

#Conect with the necessary internal components
from System.Models.db_conector import Base, session
from System.Models.db_cliente import Cliente
from System.Models.db_usuario import Empleado


min_ID = 100000
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

def getMaxID():
    query = session.query(func.max(Orden.ord_ID))
    print(query)

    maxCode = query.first()
    maxCode = maxCode[0]
    if maxCode == None:
        maxCode = min_ID
    else:
        maxCode += 1
    print(maxCode)
    return maxCode

def getListOrdenes():
    table = Orden.__table__.columns
    filter = Orden.ord_estado != "FINALIZADO"
    query = session.query(table).order_by(Orden.ord_estado.asc()).filter(filter).all()
    return query

def searchOrden(Cod):
    table = Orden.__table__.columns
    filter = Orden.ord_ID == Cod
    query = session.query(table).filter(filter).first()
    return query

def addOrden(des, val, entrega, recepcion, cli, emp):

    ID = getMaxID()
    est = "Mas del 50% del tiempo"
    new_ord = Orden(ord_ID = ID,
                    ord_estado = est,
                    ord_descripcion = des,
                    ord_valor = val,
                    ord_fechaEntrega = entrega,
                    ord_fechaRecepcion = recepcion,
                    cli_cedula_fk = cli,
                    emp_cedula_fk = emp
                    )

    session.add(new_ord)
    session.commit()

def updateOrden(ID, est, des, val, entrega, recepcion, cli, emp):

    table = Orden
    filter = Orden.ord_ID == ID
    updated_rec = session.query(table).filter(filter).first()

    #updated_rec.ord_estado = est
    updated_rec.ord_descripcion = des
    updated_rec.ord_valor = val
    updated_rec.ord_fechaEntrega = entrega
    #updated_rec.ord_fechaRecepcion = recepcion
    updated_rec.cli_cedula_fk = cli
    updated_rec.emp_cedula_fk = emp

    session.commit()


#Probably need to be eliminated or change cuz of its dependecy on Cliente y Usuario
def delOrden(Cod):

    table = Orden
    filter = Orden.id == Cod

    deleted_rec = session.query(table).filter(filter).first()
    session.delete(deleted_rec)
    session.commit()
