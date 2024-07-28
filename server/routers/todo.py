import fastapi
from fastapi import Request, Response
import json

from ..services.todo import get_todos as get_todos_service
from ..models.todo import TodoBaseModel

router = fastapi.APIRouter()


@router.get('/')
async def get_todos() -> TodoBaseModel:
    try:
        return {
            "id": 1,
            "content": "content",
            "oke": "oke"
        }
    except Exception as error:
        print(error)
        res = json.dumps({"message": "Lỗi"})
        return Response(status_code=404, content=res)
