from sqlalchemy.orm import Session
from models.corrida_model import Corrida


class CorridaRepository:

    # Listar todas as corridas
    def listar(self, db: Session):
        return db.query(Corrida).all()

    # Cadastrar corrida
    def cadastrar(self, db: Session, corrida):
        nova_corrida = Corrida(
            descricao_corrida=corrida.descricao_corrida,
            data_corrida=corrida.data_corrida,
            distancia_5km=corrida.distancia5km,
            distancia_10km=corrida.distancia10km,
            distancia_25km=corrida.distancia25km
        )

        db.add(nova_corrida)
        db.commit()
        db.refresh(nova_corrida)

        return nova_corrida

    # Buscar corrida por ID
    def corrida_id(self, db: Session, id: int):
        return db.query(Corrida).filter(
            Corrida.idcorrida == id
        ).first()

    # Alterar corrida
    def alterar(self, db: Session, id: int, corrida):
        corrida_bd = self.corrida_id(db, id)

        corrida_bd.descricao_corrida = corrida.descricao_corrida
        corrida_bd.data_corrida = corrida.data_corrida
        corrida_bd.distancia_5km = corrida.distancia5km
        corrida_bd.distancia_10km = corrida.distancia10km
        corrida_bd.distancia_25km = corrida.distancia25km

        db.commit()
        db.refresh(corrida_bd)

        return corrida_bd

    # Excluir corrida
    def excluir(self, db: Session, id: int):
        corrida_bd = self.corrida_id(db, id)

        db.delete(corrida_bd)
        db.commit()

        return {"Mensagem": "Corrida Excluída com Sucesso!!"}
