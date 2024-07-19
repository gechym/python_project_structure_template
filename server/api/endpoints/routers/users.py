from fastapi import APIRouter
from ..services.user_infer import infer_llm
router = APIRouter()

@router.get("/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"} , {"username" : infer_llm()}]
