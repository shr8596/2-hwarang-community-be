from fastapi import APIRouter
from .users.user_router import router as user_router
from .posts.post_router import router as post_router
from .comments.comment_router import router as comment_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(user_router)
api_router.include_router(post_router)
api_router.include_router(comment_router)
