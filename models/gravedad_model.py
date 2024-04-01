from sqlalchemy import Column, Integer, String
from Class.database import Database as DB

class Gravedad_model(DB.base_class):

    __tablename__ = 'gravedad'
    id = Column(Integer, primary_key=True)
    gravedad = Column(String(45), nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
