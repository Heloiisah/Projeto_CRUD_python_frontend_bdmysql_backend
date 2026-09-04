from pydantic import AliasChoices, BaseModel, Field
from datetime import date


class CorridaSchema(BaseModel):
    descricao_corrida: str
    data_corrida: date
    # O contrato público da API segue o formato usado pelo front-end. Os
    # aliases preservam compatibilidade com clientes que ainda usam "_".
    distancia5km: bool = Field(
        validation_alias=AliasChoices("distancia5km", "distancia_5km")
    )
    distancia10km: bool = Field(
        validation_alias=AliasChoices("distancia10km", "distancia_10km")
    )
    distancia25km: bool = Field(
        validation_alias=AliasChoices("distancia25km", "distancia_25km")
    )


class CorridaResposta(CorridaSchema):
    id: int


def serializar_corrida(corrida) -> dict:
    """Converte o modelo do banco para o contrato público da API."""
    return {
        "id": corrida.idcorrida,
        "descricao_corrida": corrida.descricao_corrida,
        "data_corrida": corrida.data_corrida,
        "distancia5km": corrida.distancia_5km,
        "distancia10km": corrida.distancia_10km,
        "distancia25km": corrida.distancia_25km,
    }
