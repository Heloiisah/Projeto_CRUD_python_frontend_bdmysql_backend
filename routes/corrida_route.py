from fastapi import APIRouter
from database import SessionLocal

from controllers.corrida_controller import CorridaController
from schemas.corrida_schema import CorridaResposta, CorridaSchema, serializar_corrida


router = APIRouter(
    prefix="/corrida",
    tags=["Corrida"]
)


controller = CorridaController()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[CorridaResposta])
def listar():
    db = next(get_db())

    return [serializar_corrida(corrida) for corrida in controller.listar(db)]


@router.get("/{id}", response_model=CorridaResposta)
def listar_id(id: int):
    db = next(get_db())

    return serializar_corrida(controller.listar_id(db, id))


@router.post("/", response_model=CorridaResposta)
def cadastrar(corrida: CorridaSchema):
    db = next(get_db())

    return serializar_corrida(controller.cadastrar(db, corrida))


@router.put("/{id}", response_model=CorridaResposta)
def alterar(id: int, corrida: CorridaSchema):
    db = next(get_db())

    corrida_alterada = controller.alterar(
        db,
        id,
        corrida
    )
    return serializar_corrida(corrida_alterada)


@router.delete("/{id}")
def excluir(id: int):
    db = next(get_db())

    return controller.excluir(
        db,
        id
    )
