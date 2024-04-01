from sqlalchemy import Column, Integer, String
from Class.database import Database as DB

class Eps_model(DB.base_class):
    __tablename__ = 'eps'

    id = Column(Integer, primary_key=True)
    eps = Column(String(45), nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns} 