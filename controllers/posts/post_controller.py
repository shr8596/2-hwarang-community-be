from fastapi import Request, HTTPException, Depends
from fastapi.responses import JSONResponse
from utils.response_schema import response_schema
from utils.success_message import successfully
import utils.error_message
from utils.validator.request_validator import validate_title, validate_content, validate_post_image_url, validate_post_id, validate_offset, validate_limit
from dependencies.auth_dependency import get_current_user

# 게시글 임시 데이터
post_model = {
    "postId": "1",
    "userId": "1",
    "title": "테스트 게시글",
    "content": "게시글 내용입니다.",
    "postImageUrl": "https://example.com/image.jpg",
    "likeCount": 10,
    "commentCount": 5,
    "viewCount": 100,
    "createdAt": "2026-01-01T00:00:00.000Z",
    "updatedAt": "2026-01-01T00:00:00.000Z",
}

# 게시글 작성
# 401, 405, 429 검증은 라우터의 Depends에서 처리
async def create_post(
    request: Request,
    current_user: dict = Depends(get_current_user)
):
    body = await request.json()

    # 400, 422 - title 검증
    title = validate_title(body.get("title"))

    # 400, 422 - content 검증
    content = validate_content(body.get("content"))

    # 400, 422 - postImageUrl 검증 (선택적)
    post_image_url = body.get("postImageUrl")
    if post_image_url is not None:
        post_image_url = validate_post_image_url(post_image_url)

    # 인증된 사용자 정보
    user_id = current_user["user_data"]["userId"]

    try:
        # TODO: 실제 DB에 게시글 생성 : 추후 구현
        return JSONResponse(
            status_code=201,
            content=response_schema(
                message=successfully("post_created"),
                data={
                    "postId": "1",
                    "userId": user_id,
                    "title": title,
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

# 게시글 전체 목록 조회
# 401, 405, 429 검증은 라우터의 Depends에서 처리
async def read_posts(
    offset: int,
    limit: int,
    current_user: dict = Depends(get_current_user)
):
    # 400, 422 - offset 검증
    offset = validate_offset(offset)

    # 400, 422 - limit 검증
    limit = validate_limit(limit)

    try:
        # TODO: 실제 DB에서 게시글 목록 조회 : 추후 구현
        return JSONResponse(
            status_code=200,
            content=response_schema(
                message=successfully("posts_fetched"),
                data={
                    "posts": [post_model],
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

# 게시글 상세 조회
# 401, 405, 429 검증은 라우터의 Depends에서 처리
async def read_post(
    post_id: int,
    current_user: dict = Depends(get_current_user)
):
    # post_id 검증 (400, 422)
    post_id = validate_post_id(post_id)

    try:
        # TODO: 실제 DB에서 게시글 조회 : 추후 구현
        return JSONResponse(
            status_code=200,
            content=response_schema(
                message=successfully("post_fetched"),
                data=post_model,
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

# 게시글 수정
# 401, 405, 429 검증은 라우터의 Depends에서 처리
async def update_post(
    post_id: int,
    request: Request,
    current_user: dict = Depends(get_current_user)
):
    body = await request.json()

    # 400, 422 - post_id 검증
    post_id = validate_post_id(post_id)

    # 400, 422 - title 검증
    title = validate_title(body.get("title"))

    # 400, 422 - content 검증
    content = validate_content(body.get("content"))

    # 400, 422 - postImageUrl 검증 (선택적)
    post_image_url = body.get("postImageUrl")
    if post_image_url is not None:
        post_image_url = validate_post_image_url(post_image_url)

    # 403
    # TODO: 본인이 작성한 게시글이 아닌 경우 권한 없음 : 추후 구현
    # current_user_id = current_user["user_data"]["userId"]
    # if post_author_id != current_user_id:
    #     raise HTTPException(status_code=403, detail=...)

    # 404
    # TODO: 존재하지 않는 게시글인 경우 : 추후 구현

    try:
        # TODO: 실제 DB에서 게시글 수정 : 추후 구현
        return JSONResponse(
            status_code=200,
            content=response_schema(
                message=successfully("post_updated"),
                data={
                    "postId": post_id,
                    "title": title,
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

# 게시글 삭제
# 401, 405, 429 검증은 라우터의 Depends에서 처리
async def delete_post(
    post_id: int,
    current_user: dict = Depends(get_current_user)
):
    # post_id 검증 (400, 422)
    post_id = validate_post_id(post_id)

    # 403
    # TODO: 본인이 작성한 게시글이 아닌 경우 권한 없음 : 추후 구현
    # current_user_id = current_user["user_data"]["userId"]
    # if post_author_id != current_user_id:
    #     raise HTTPException(status_code=403, detail=...)

    # 404
    # TODO: 존재하지 않는 게시글인 경우 : 추후 구현

    try:
        # TODO: 실제 DB에서 게시글 삭제 : 추후 구현
        return JSONResponse(
            status_code=200,
            content=response_schema(
                message=successfully("post_deleted"),
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

# 게시글 좋아요 추가
# 401, 405, 429 검증은 라우터의 Depends에서 처리
async def like_post(
    post_id: int,
    current_user: dict = Depends(get_current_user)
):
    # post_id 검증 (400, 422)
    post_id = validate_post_id(post_id)

    # 403
    # TODO: 이미 좋아요를 누른 경우 : 추후 구현

    # 404
    # TODO: 존재하지 않는 게시글인 경우 : 추후 구현

    try:
        # TODO: 실제 DB에서 좋아요 추가 : 추후 구현
        return JSONResponse(
            status_code=200,
            content=response_schema(
                message=successfully("like_added"),
                data={"postId": post_id, "likeCount": 11},
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

# 게시글 좋아요 제거
# 401, 405, 429 검증은 라우터의 Depends에서 처리
async def unlike_post(
    post_id: int,
    current_user: dict = Depends(get_current_user)
):
    # post_id 검증 (400, 422)
    post_id = validate_post_id(post_id)

    # 403
    # TODO: 좋아요를 누르지 않은 경우 : 추후 구현

    # 404
    # TODO: 존재하지 않는 게시글인 경우 : 추후 구현

    try:
        # TODO: 실제 DB에서 좋아요 제거 : 추후 구현
        return JSONResponse(
            status_code=200,
            content=response_schema(
                message=successfully("like_removed"),
                data={"postId": post_id, "likeCount": 9},
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