from pydantic import BaseModel


class Cat(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
