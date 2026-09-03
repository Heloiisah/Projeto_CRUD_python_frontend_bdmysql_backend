from pydantic import BaseModel, field_validator
from datetime import date
import re

class PessoaSchema(BaseModel):
    nome : str
    cpf: int
    data_nascimento: date
    peso: int
    altura: float
    sexo : str
    cep : int
    rua_logradouro : str
    bairro : str
    cidade : str
    uf : str
    
    @field_validator("cpf", "cep", mode="before")
    @classmethod
    def remove_non_digits(cls, v):
        if isinstance(v, str):
            v = re.sub(r'\D', '', v)
        return v