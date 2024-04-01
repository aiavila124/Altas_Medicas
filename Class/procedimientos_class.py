from Class.database import Database as DB
from models.procedimientos_model import Procedimientos_model

class Procedimientos_class:

    def __init__(self):
        pass

    def insert_procedimientos(self, data):
        db = DB().session
        modelo = Procedimientos_model(**data)
        db.add(modelo)
        db.commit()

        return modelo.as_dict()