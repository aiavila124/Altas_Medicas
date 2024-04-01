from sqlalchemy import Column, Integer, String
from Class.database import Database as DB

class Medico_model(DB.base_class):
    __tablename__ = "medico"

    id = Column(Integer, primary_key=True)
    Nombre = Column(String(45), nullable=False)
    Apellido = Column(String(45), nullable=False)
    genero_id = Column(Integer, nullable=False)
    tipo_identificacion_id = Column(Integer, nullable=False)
    Numero_identificacion = Column(String(45), nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}