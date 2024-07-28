import fastapi
from fastapi import Request, Response
import json

router = fastapi.APIRouter()


@router.get('/')
async def get_users():
    try:
        return Response(status_code=200, content="Hello")
    except Exception as error:
        res = json.dumps({"message": "Lỗi"})
        return Response(status_code=404, content=res)
