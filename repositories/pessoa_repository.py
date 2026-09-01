from sqlalchemy.orm import Session
from models.pessoa_model import Pessoa

class PessoaRepository:
    #listar todas as pessoas
    def listar(self, db: Session):
        return db.query(Pessoa).all()
    
    #cadastra Pessoa
    def cadastar(self, db: Session, pessoa):
        nova_pessoa = Pessoa(
            nome = pessoa.nome,
            cpf = pessoa.cpf,
            data_nascimento = pessoa.data_nascimento,
            peso = pessoa.peso,
            altura = pessoa.altura,
            sexo = pessoa.sexo,
            cep = pessoa.cep,
            rua_logradouro = pessoa.rua_logradouro,
            bairro = pessoa.bairro,
            cidade = pessoa.cidade,
            uf = pessoa.uf
        )

        db.add(nova_pessoa)
        db.commit()
        db.refresh(nova_pessoa)

        return nova_pessoa
    
    #listar pessoa por id
    def pessoa_id(self, db: Session, id: int):
        return db.query(Pessoa).filter(Pessoa.id == id).first()
    
    #alterar pessoa
    def alterar (self, db: Session, id: int, pessoa):
        pessoa_bd = self.pessoa_id(db, id)

        pessoa_bd.nome = pessoa.nome
        pessoa_bd.cpf = pessoa.cpf
        pessoa_bd.data_nascimento = pessoa.data_nascimento
        pessoa_bd.peso = pessoa.peso
        pessoa_bd.altura = pessoa.altura
        pessoa_bd.sexo = pessoa.sexo
        pessoa_bd.cep = pessoa.cep
        pessoa_bd.rua_logradouro = pessoa.rua_logradouro
        pessoa_bd.bairro = pessoa.bairro
        pessoa_bd.cidade = pessoa.cidade
        pessoa_bd.uf = pessoa.uf        
        
        db.commit()
        db.refresh(pessoa_bd)
        
        return pessoa_bd
    
    #excluir pessoa
    def excluir (self, db: Session, id: int):
       pessoa_bd = self.pessoa_id(db, id)
       
       db.delete(pessoa_bd)
       db.commit()

       return{"Mensagem": "Pessoa Excluída com Sucesso!"}
   