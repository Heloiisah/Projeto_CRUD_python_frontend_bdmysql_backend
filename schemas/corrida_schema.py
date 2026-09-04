from pydantic import BaseModel
from datetime import date


class CorridaSchema(BaseModel):
    descricao_corrida: str
    data_corrida: date
    distancia_5km: bool
    distancia_10km: bool
    distancia_25km: bool
