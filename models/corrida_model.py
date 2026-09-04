from sqlalchemy import Column, Integer, String, Boolean, Date

from database import Base


class Corrida(Base):
    __tablename__ = "corrida"

    idcorrida = Column(Integer, primary_key=True, index=True)
    descricao_corrida = Column(String(200), nullable=False)
    data_corrida = Column(Date, nullable=False)
    distancia_5km = Column(Boolean, nullable=False)
    distancia_10km = Column(Boolean, nullable=False)
    distancia_25km = Column(Boolean, nullable=False)
