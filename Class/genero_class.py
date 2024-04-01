from Class.database import Database as DB
from models.genero_model import Genero_model

class Genero_class:
    def insert_genero(self,data):
        db = DB().session
        modelo = Genero_model(**data)
        db.add(modelo)
        db.commit()

        return modelo.as_dict()