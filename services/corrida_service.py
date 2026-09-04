from repositories.corrida_repository import CorridaRepository


class CorridaService:

    # Método construtor
    def __init__(self):
        self.repo = CorridaRepository()

    # Serviço listar
    def listar(self, db):
        return self.repo.listar(db)

    # Serviço listar por ID
    def listar_id(self, db, id):
        return self.repo.corrida_id(db, id)

    # Serviço cadastrar
    def cadastrar(self, db, corrida):
        return self.repo.cadastrar(db, corrida)

    # Serviço alterar
    def alterar(self, db, id, corrida):
        return self.repo.alterar(db, id, corrida)

    # Serviço excluir
    def excluir(self, db, id):
        return self.repo.excluir(db, id)
