from Class.database import Database as DB
from models.tipo_identificacion_model import Tipo_identificacion_model

class Tipo_identificacion:

    def __init__(self):
        pass

    def insert_tipo_identificacion(self,data):
        db = DB().session
        modelo = Tipo_identificacion_model(**data)
        db.add(modelo)
        db.commit()

        return modelo.as_dict()
    
    def get_tipo_identificacion(self):
        db = DB().session
        query = db.query(Tipo_identificacion_model).all()
        json_dict = [row.as_dict() for row in query]
        
        return json_dict
    