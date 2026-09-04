from services.corrida_service import CorridaService


class CorridaController:

    # Método construtor
    def __init__(self):
        self.servico = CorridaService()

    # Controller listar
    def listar(self, db):
        return self.servico.listar(db)

    # Controller listar por ID
    def listar_id(self, db, id):
        return self.servico.listar_id(db, id)

    # Controller cadastrar
    def cadastrar(self, db, corrida):
        return self.servico.cadastrar(db, corrida)

    # Controller alterar
    def alterar(self, db, id, corrida):
        return self.servico.alterar(db, id, corrida)

    # Controller excluir
    def excluir(self, db, id):
        return self.servico.excluir(db, id)
