from controllers.comments import comment_controller
from fastapi import APIRouter, Request, Depends
from dependencies.auth_dependency import get_current_session
from dependencies.rate_limit_dependency import rate_limiter
from dependencies.method_dependency import require_post, require_get, require_patch, require_delete

router = APIRouter(prefix="/comments", tags=["comments"])

# 댓글 작성
@router.post(
    "",
    dependencies=[
        Depends(require_post),
        Depends(get_current_session),
        Depends(rate_limiter),
    ]
)
async def create_comment(post_id: int, request: Request):
    return await comment_controller.create_comment(post_id, request)

# 댓글 전체 목록 조회
@router.get(
    "",
    dependencies=[
        Depends(require_get),
        Depends(get_current_session),
        Depends(rate_limiter),
    ]
)
async def read_comments(post_id: int, request: Request, offset: int = 0, limit: int = 10):
    return await comment_controller.read_comments(post_id, request, offset, limit)

# 댓글 수정
@router.patch(
    "/{comment_id}",
    dependencies=[
        Depends(require_patch),
        Depends(get_current_session),
        Depends(rate_limiter),
    ]
)
async def update_comment(comment_id: int, post_id: int, request: Request):
    return await comment_controller.update_comment(comment_id, post_id, request)

# 댓글 삭제
@router.delete(
    "/{comment_id}",
    dependencies=[
        Depends(require_delete),
        Depends(get_current_session),
        Depends(rate_limiter),
    ]
)
async def delete_comment(comment_id: int, post_id: int, request: Request):
    return await comment_controller.delete_comment(comment_id, post_id, request)

