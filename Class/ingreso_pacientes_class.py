from Class.database import Database as DB
from models.ingresos_pacientes_model import Ingreso_pacientes_model


class Ingreso_pacientes_class:
    def __init__(self):
        pass

    def insert_ingreso_pacientes(self, data):
        db = DB().session
        modelo = Ingreso_pacientes_model(**data)
        db.add(modelo)
        db.commit()

        return modelo.as_dict()

    def delete_ingreso_pacientes(self, data):
        db = DB().session
        modelo = db.query(Ingreso_pacientes_model).filter(Ingreso_pacientes_model.id == data).first()
        db.delete(modelo)
        db.commit()

        return "Registro eliminado"
