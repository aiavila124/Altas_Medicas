from sqlalchemy import Column, Integer, String, Date
from Class.database import Database as DB


class Ingreso_pacientes_model(DB.base_class):
    __tablename__ = "ingresos_pacientes"
    id = Column(Integer, primary_key=True)
    pacientes_id = Column(Integer, nullable=False)
    fecha_entrada = Column(Date, nullable=False)
    temp_corporal_C = Column(String(45), nullable=False)
    malestar = Column(String(45), nullable=False)
    eps_id = Column(Integer, nullable=False)

    def as_dict(self):
        fecha_entrada_str = self.fecha_entrada.isoformat() if self.fecha_entrada else None
        data = {
            c.name: getattr(self, c.name) if c.name != 'fecha_entrada' else fecha_entrada_str
            for c in self.__table__.columns
            }

        return data