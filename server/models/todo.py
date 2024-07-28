from pydantic import BaseModel


class TodoBaseModel(BaseModel):
    id: int
    content: str
