from fastapi import APIRouter
from .endpoints.routers import users 

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["users"])