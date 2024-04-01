from Class.database import Database as DB
from models.gravedad_model import Gravedad_model

class Gravedad_class:

    def __init__(self):
        pass

    def insert_gravedad(self, data):
        db = DB().session
        modelo = Gravedad_model(**data)
        db.add(modelo)
        db.commit()

        return modelo.as_dict()
    
    # Otra forma de hacerlo es con un post y de ahi sacar el id y el nuevo valor
    def update_gravedad(self,data, new_value):
        db = DB().session
    
        modelo = db.query(Gravedad_model).filter(Gravedad_model.id == data).first()

        modelo.gravedad = new_value['gravedad']
        db.commit()

        return modelo.as_dict()