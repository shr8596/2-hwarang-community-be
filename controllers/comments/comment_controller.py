from fastapi import Request, HTTPException, Depends
from fastapi.responses import JSONResponse
from utils.response_schema import response_schema
from utils.success_message import successfully
import utils.error_message
from utils.validator.request_validator import (
    validate_content, validate_comment_create_request, validate_comment_list_params, validate_comment_modify_params
)
from dependencies.auth_dependency import get_current_user

# 댓글 임시 데이터
comment_model = {
    "commentId": "1",
    "postId": "1",
    "userId": "1",
    "content": "댓글 내용입니다.",
    "createdAt": "2026-01-01T00:00:00.000Z",
    "updatedAt": "2026-01-01T00:00:00.000Z",
}

# 댓글 작성
# 401, 405, 429 검증은 라우터의 Depends에서 처리
async def create_comment(
    post_id: int,
    request: Request,
    current_user: dict = Depends(get_current_user)
):
    body = await request.json()

    # 모든 유효성 검증을 통합 함수로 처리 (400, 422)
    post_id, content = validate_comment_create_request(post_id, body)

    # 인증된 사용자 정보
    user_id = current_user["user_data"]["userId"]

    try:
        # TODO: 실제 DB에 댓글 생성 : 추후 구현
        return JSONResponse(
            status_code=201,
            content=response_schema(
                message=successfully("comment_created"),
                data={
                    "commentId": "1",
                    "postId": post_id,
                    "userId": user_id,
                    "content": content,
                },
            ),
        )
    except Exception:
        raise HTTPException(
            status_code=500,
            detail=response_schema(
                message=utils.error_message.internal_server_error,
                data=None,
            ),
        )

# 댓글 전체 목록 조회
# 401, 405, 429 검증은 라우터의 Depends에서 처리
async def read_comments(
    post_id: int,
    offset: int,
    limit: int,
    current_user: dict = Depends(get_current_user)
):
    # 모든 유효성 검증을 통합 함수로 처리 (400, 422)
    post_id, offset, limit = validate_comment_list_params(post_id, offset, limit)

    # 404
    # TODO: 존재하지 않는 게시글인 경우 : 추후 구현

    try:
        # TODO: 실제 DB에서 댓글 목록 조회 : 추후 구현
        return JSONResponse(
            status_code=200,
            content=response_schema(
                message=successfully("comments_fetched"),
                data={
                    "comments": [comment_model],
                    "total": 1,
                    "offset": offset,
                    "limit": limit,
                },
            ),
        )
    except Exception:
        raise HTTPException(
            status_code=500,
            detail=response_schema(
                message=utils.error_message.internal_server_error,
                data=None,
            ),
        )

# 댓글 수정
# 401, 405, 429 검증은 라우터의 Depends에서 처리
async def update_comment(
    comment_id: int,
    post_id: int,
    request: Request,
    current_user: dict = Depends(get_current_user)
):
    body = await request.json()

    # 모든 유효성 검증을 통합 함수로 처리 (400, 422)
    comment_id, post_id = validate_comment_modify_params(comment_id, post_id)
    content = validate_content(body.get("content"))

    # 403
    # TODO: 본인이 작성한 댓글이 아닌 경우 권한 없음 : 추후 구현
    # current_user_id = current_user["user_data"]["userId"]
    # if comment_author_id != current_user_id:
    #     raise HTTPException(status_code=403, detail=...)

    # 404
    # TODO: 존재하지 않는 댓글인 경우 : 추후 구현

    try:
        # TODO: 실제 DB에서 댓글 수정 : 추후 구현
        return JSONResponse(
            status_code=200,
            content=response_schema(
                message=successfully("comment_updated"),
                data={
                    "commentId": comment_id,
                    "content": content,
                },
            ),
        )
    except Exception:
        raise HTTPException(
            status_code=500,
            detail=response_schema(
                message=utils.error_message.internal_server_error,
                data=None,
            ),
        )

# 댓글 삭제
# 401, 405, 429 검증은 라우터의 Depends에서 처리
async def delete_comment(
    comment_id: int,
    post_id: int,
    current_user: dict = Depends(get_current_user)
):
    # 모든 유효성 검증을 통합 함수로 처리 (400, 422)
    comment_id, post_id = validate_comment_modify_params(comment_id, post_id)

    # 403
    # TODO: 본인이 작성한 댓글이 아닌 경우 권한 없음 : 추후 구현
    # current_user_id = current_user["user_data"]["userId"]
    # if comment_author_id != current_user_id:
    #     raise HTTPException(status_code=403, detail=...)

    # 404
    # TODO: 존재하지 않는 댓글인 경우 : 추후 구현

    try:
        # TODO: 실제 DB에서 댓글 삭제 : 추후 구현
        return JSONResponse(
            status_code=200,
            content=response_schema(
                message=successfully("comment_deleted"),
                data=None,
            ),
        )
    except Exception:
        raise HTTPException(
            status_code=500,
            detail=response_schema(
                message=utils.error_message.internal_server_error,
                data=None,
            ),
        )