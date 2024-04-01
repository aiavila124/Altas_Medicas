from sqlalchemy import Column, Integer, String
from Class.database import Database as DB

class Login_model(DB.base_class):

    __tablename__ = "login"

    id = Column(Integer, primary_key=True)
    user = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)


    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}