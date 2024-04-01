from Class.database import Database as DB
from models.pacientes_model import Pacientes_model

class Pacientes_class:

    def __init__(self):
        self.db = DB().session

    def insert_pacientes(self,data):
        db = DB().session
        modelo = Pacientes_model(**data)
        db.add(modelo)
        db.commit()

        return modelo.as_dict()