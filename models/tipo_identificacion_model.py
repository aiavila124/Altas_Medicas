from sqlalchemy import Column, Integer, String, TIMESTAMP
from Class.database import Database as db

class Tipo_identificacion_model(db.base_class):
    __tablename__ = 'tipo_identificacion'

    id = Column(Integer, primary_key=True)
    Tipo = Column(String(45), nullable=False)
    # registrarion_Date = Column(TIMESTAMP)
    # active = Column(Integer)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
