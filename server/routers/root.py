from fastapi import APIRouter

from .todo import router as todo_router
from .user import router as user_router

router = APIRouter()
router.include_router(todo_router, prefix="/todo", tags=["todo"])
router.include_router(user_router, prefix="/user", tags=["user"])
