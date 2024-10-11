from fastapi import APIRouter
from . import schemas

router = APIRouter()


@router.get("/hello/{name}")
def hello_cat(name: str) -> schemas.Cat:
    return schemas.Cat(
        id=0,
        name=name,
    )
