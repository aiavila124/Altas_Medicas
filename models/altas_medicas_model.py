from sqlalchemy import Column, Integer, String, Date
from Class.database import Database as DB

class Altas_medicas_model(DB.base_class):

    __tablename__ = "alta_medica"

    id = Column(Integer, primary_key=True)
    fecha_salida = Column(Date, nullable=False)
    procedimiento_id = Column(Integer, nullable=False)
    temp_corporal = Column(String(45), nullable=False)
    acompaniante = Column(String(45), nullable=False)
    receta_medica = Column(String(45), nullable=False)

    def as_dict(self):
        return {c.name : getattr(self, c.name) if c.name != 'fecha_salida' else self.fecha_salida.isoformat() for c in self.__table__.columns}
    

