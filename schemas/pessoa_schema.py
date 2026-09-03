from pydantic import BaseModel
from datetime import date

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