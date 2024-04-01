from Class.database import Database as DB
from models.altas_medicas_model import Altas_medicas_model

class Altas_medicas_class():

    def __init__(self):
        pass

    def insert_altas_medicas(self, data):
        db = DB().session
        modelo = Altas_medicas_model(**data)
        db.add(modelo)
        db.commit()

        return modelo.as_dict()