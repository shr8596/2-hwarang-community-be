from fastapi import APIRouter
from .users.user_router import router as user_router
from .posts.post_router import router as post_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(user_router)
api_router.include_router(post_router)
