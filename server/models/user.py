from pydantic import BaseModel


class UserBaseModel(BaseModel):
    id: int
    name: str
