from controllers.posts import post_controller
from fastapi import APIRouter, Request, Depends
from dependencies.auth_dependency import get_current_session
from dependencies.rate_limit_dependency import rate_limiter
from dependencies.method_dependency import require_post, require_get, require_patch, require_delete, require_put

router = APIRouter(prefix="/posts", tags=["posts"])

# 게시글 작성
@router.post(
    "",
    dependencies=[
        Depends(require_post),
        Depends(get_current_session),
        Depends(rate_limiter),
    ]
)
async def create_post(request: Request):
    return await post_controller.create_post(request)

# 게시글 전체 목록 조회
@router.get(
    "",
    dependencies=[
        Depends(require_get),
        Depends(get_current_session),
        Depends(rate_limiter),
    ]
)
async def read_posts(request: Request, offset: int = 0, limit: int = 10):
    return await post_controller.read_posts(request, offset, limit)

# 게시글 상세 조회
@router.get(
    "/{post_id}",
    dependencies=[
        Depends(require_get),
        Depends(get_current_session),
        Depends(rate_limiter),
    ]
)
async def read_post(post_id: int, request: Request):
    return await post_controller.read_post(post_id, request)

# 게시글 수정
@router.put(
    "/{post_id}",
    dependencies=[
        Depends(require_put),
        Depends(get_current_session),
        Depends(rate_limiter),
    ]
)
async def update_post(post_id: int, request: Request):
    return await post_controller.update_post(post_id, request)

# 게시글 삭제
@router.delete(
    "/{post_id}",
    dependencies=[
        Depends(require_delete),
        Depends(get_current_session),
        Depends(rate_limiter),
    ]
)
async def delete_post(post_id: int, request: Request):
    return await post_controller.delete_post(post_id, request)

# 게시글 좋아요 추가
@router.patch(
    "/{post_id}/like",
    dependencies=[
        Depends(require_patch),
        Depends(get_current_session),
        Depends(rate_limiter),
    ]
)
async def like_post(post_id: int, request: Request):
    return await post_controller.like_post(post_id, request)

# 게시글 좋아요 제거
@router.patch(
    "/{post_id}/unlike",
    dependencies=[
        Depends(require_patch),
        Depends(get_current_session),
        Depends(rate_limiter),
    ]
)
async def unlike_post(post_id: int, request: Request):
    return await post_controller.unlike_post(post_id, request)

