from sqlalchemy import Column, Integer, String
from Class.database import Database as DB

class Procedimientos_model(DB.base_class):
    __tablename__ = 'procedimiento'

    id = Column(Integer, primary_key=True)
    ingresos_pacientes_id = Column(Integer, nullable=False)
    medico_id = Column(Integer, nullable=False)
    tratamiento = Column(String(45), nullable=False)
    num_cama = Column(String, nullable=False)
    diagnostico = Column(String(45), nullable=False)
    gravedad_id = Column(Integer, nullable=False)
    

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}