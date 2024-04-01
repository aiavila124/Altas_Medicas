from Class.database import Database as DB
from models.eps_model import Eps_model

class Eps_class():
    def __init__(self):
        pass

    def insert_eps(self,data):
        db = DB().session
        modelo = Eps_model(**data)
        db.add(modelo)
        db.commit()

        return modelo.as_dict()