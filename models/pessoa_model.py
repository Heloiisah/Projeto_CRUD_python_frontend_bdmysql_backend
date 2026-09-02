from sqlalchemy import Column, Integer, String, DECIMAL, Date

from database import Base


class Pessoa(Base):
    __tablename__ = "pessoa"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(60), nullable=True)
    cpf = Column(Integer, nullable=True)
    data_nascimento = Column(Date, nullable=True)
    peso = Column(Integer, nullable=True)
    altura = Column(DECIMAL(10, 2), nullable=True)
    sexo = Column(String(1), nullable=True)
    cep = Column(Integer, nullable=True)
    rua_logradouro = Column(String(100), nullable=True)
    bairro = Column(String(20), nullable=True)
    cidade = Column(String(70), nullable=True)
    uf = Column(String(2), nullable=True)
