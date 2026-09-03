
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal

from controllers.pessoa_controller import PessoaController
from schemas.pessoa_schema import PessoaSchema


router = APIRouter(
    prefix="/pessoa",
    tags=["Pessoa"]
)

controller = PessoaController()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.get("/")
def listar(db: Session = Depends(get_db)):
    return controller.listar(db)


@router.get("/{id}")
def listar_id(id: int, db: Session = Depends(get_db)):
    return controller.listar_id(db, id)


@router.post("/")
def cadastrar(pessoa: PessoaSchema, db: Session = Depends(get_db)):
    return controller.cadastrar(db, pessoa)


@router.put("/{id}")
def alterar(
    id: int,
    pessoa: PessoaSchema,
    db: Session = Depends(get_db)
):
    return controller.alterar(
        db,
        id,
        pessoa
    )


@router.delete("/{id}")
def excluir(id: int, db: Session = Depends(get_db)):
    return controller.excluir(
        db,
        id
    )

