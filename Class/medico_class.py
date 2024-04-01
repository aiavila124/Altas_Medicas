from models.medico_model import Medico_model
from Class.database import Database as DB

class Medico_class:
    def __init__(self):
        self.db = DB().session

    def insert_medico(self,data):
        db = DB().session
        modelo = Medico_model(**data)
        db.add(modelo)
        db.commit()

        return modelo.as_dict()