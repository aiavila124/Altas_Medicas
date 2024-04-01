from sqlalchemy import Column, Integer, String, TIMESTAMP
from Class.database import Database as DB

class Genero_model(DB.base_class):
    __tablename__ = 'genero'

    id = Column(Integer, primary_key=True)
    Genero = Column(String(45), nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}