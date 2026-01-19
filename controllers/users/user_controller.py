import uuid
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from utils.response_schema import response_schema
from utils.success_message import successfully
import utils.error_message
import utils.constants
from utils.validator.request_validator import validate_email, validate_password, validate_user_id, validate_nickname, validate_profile_image_url

# 사용자 임시 데이터
user_model =  {
    "userId"            : "1",
    "userNickname"      : "startup",
    "email"             : "test@gmail.com",
    "profileImageUrl"   : "http~~~",
    "isWithdrawn"       : "false",
    "createdAt"         : "2026-01-01T00:00:00.000Z",
    "updatedAt"         : "2026-01-01T00:00:00.000Z",
}

# 회원가입
# 405, 429 검증은 라우터의 Depends에서 처리
async def create_user(request: Request):
    body = await request.json()

    # 400, 422 - 이메일 검증
    email = validate_email(body.get("email"))

    # 400, 422 - 비밀번호 검증
    password = validate_password(body.get("password"))

    # 400, 422 - 닉네임 검증
    nickname = validate_nickname(body.get("nickname"))

    # 400, 422 - 프로필 이미지 URL 검증 (선택적)
    profile_image_url = body.get("profileImageUrl")
    if profile_image_url is not None:
        profile_image_url = validate_profile_image_url(profile_image_url)

    # 409
    # TODO: 실제 DB에서 이메일 중복 확인 : 추후 구현

    try:
        # TODO: 실제 DB에 사용자 생성 : 추후 구현
        # 임시 세션 생성
        session_id = str(uuid.uuid4())
        request.session["sessionID"] = session_id
        request.session["email"] = email

        return JSONResponse(
            status_code=201,
            content=response_schema(
                message=successfully("user_created"),
                data={
                    "sessionID": session_id,
                    "email": email,
                    "nickname": nickname,
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

# 회원 로그인
# 405, 429 검증은 라우터의 Depends에서 처리
async def login_user(request: Request):
    body = await request.json()

    # 400, 422 - 이메일 검증
    email = validate_email(body.get("email"))

    # 400, 422 - 비밀번호 검증
    password = validate_password(body.get("password"))

    try:
        # TODO: 실제 DB에서 사용자 인증 및 조회 : 추후 구현
        # 로그인 성공 시 세션 생성
        session_id = str(uuid.uuid4())
        request.session["sessionID"] = session_id
        request.session["email"] = email

        return JSONResponse(
            status_code=200,
            content=response_schema(
                message=successfully("logged_in"),
                data={
                    "sessionID": session_id,
                    "email": email,
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

# 회원 로그아웃
# 401, 405, 429 검증은 라우터의 Depends에서 처리
async def logout_user(request: Request):
    try:
        request.session.clear()
        return JSONResponse(
            status_code=200,
            content=response_schema(
                message=successfully("logged_out"),
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

# 회원 탈퇴
# 401, 405, 429 검증은 라우터의 Depends에서 처리
async def delete_user(user_id: int, request: Request):

    # 400, 422 - user_id 검증
    user_id = validate_user_id(user_id)

    try:
        # TODO: 실제 DB에서 사용자 삭제 : 추후 구현
        request.session.clear()
        return JSONResponse(
            status_code=200,
            content=response_schema(
                message=successfully("account_deleted"),
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

# 회원 정보 조회
# 401, 405, 429 검증은 라우터의 Depends에서 처리
async def read_user(user_id: int, request: Request):

    # 400, 422 - user_id 검증
    user_id = validate_user_id(user_id)

    try:
        # TODO: 실제 DB에서 사용자 정보 조회 : 추후 구현
        return JSONResponse(
            status_code=200,
            content=response_schema(
                message=successfully("user_fetched"),
                data=user_model,
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

# 회원 정보 수정(비밀번호)
# 401, 405, 429 검증은 라우터의 Depends에서 처리
async def update_user_password(user_id: int, request: Request):

    body = await request.json()

    # 400, 422 - user_id 검증
    user_id = validate_user_id(user_id)

    # 400, 422 - 새 비밀번호 검증
    password = validate_password(body.get("password"))

    # 403
    # TODO : 본인이 아닌 다른 사용자의 정보 수정 시도 시 권한 없음 : 추후 구현

    # 404
    # TODO : 존재하지 않는 사용자 또는 탈퇴한 사용자인 경우 : 추후 구현

    try:
        # TODO: 실제 DB에서 비밀번호 업데이트 : 추후 구현
        return JSONResponse(
            status_code=200,
            content=response_schema(
                message=successfully("password_updated"),
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

# 회원 정보 수정(닉네임)
# 401, 405, 429 검증은 라우터의 Depends에서 처리
async def update_user_nickname(user_id: int, request: Request):
    body = await request.json()

    # 400, 422 - user_id 검증
    user_id = validate_user_id(user_id)

    # 400, 422 - 닉네임 검증
    nickname = validate_nickname(body.get("nickname"))

    # 403
    # TODO : 본인이 아닌 다른 사용자의 정보 수정 시도 시 권한 없음 : 추후 구현

    # 404
    # TODO : 존재하지 않는 사용자 또는 탈퇴한 사용자인 경우 : 추후 구현

    try:
        # TODO: 실제 DB에서 닉네임 업데이트 : 추후 구현
        return JSONResponse(
            status_code=200,
            content=response_schema(
                message=successfully("nickname_updated"),
                data={"nickname": nickname},
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

# 회원 정보 수정(프로필 이미지 URL)
# 401, 405, 429 검증은 라우터의 Depends에서 처리
async def update_user_profile_image_url(user_id: int, request: Request):
    body = await request.json()

    # 400, 422 - user_id 검증
    user_id = validate_user_id(user_id)

    # 400, 422 - 프로필 이미지 URL 검증 (선택적)
    profile_image_url = body.get("profileImageUrl")
    if profile_image_url is not None:
        profile_image_url = validate_profile_image_url(profile_image_url)

    # 403
    # TODO : 본인이 아닌 다른 사용자의 정보 수정 시도 시 권한 없음 : 추후 구현

    # 404
    # TODO : 존재하지 않는 사용자 또는 탈퇴한 사용자인 경우 : 추후 구현

    try:
        # TODO: 실제 DB에서 프로필 이미지 URL 업데이트 : 추후 구현
        return JSONResponse(
            status_code=200,
            content=response_schema(
                message=successfully("profile_image_url_updated"),
                data={"profileImageUrl": profile_image_url},
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

# 회원 이메일 중복 확인
# 405, 429 검증은 라우터의 Depends에서 처리
async def check_email_duplicate(request: Request):
    body = await request.json()

    # 400, 422 - 이메일 검증
    email = validate_email(body.get("email"))

    try:
        # TODO: 실제 DB에서 이메일 중복 확인 : 추후 구현
        is_available = True
        return JSONResponse(
            status_code=200,
            content=response_schema(
                message=successfully("email_checked"),
                data={"isAvailable": is_available},
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

# 회원 닉네임 중복 확인
# 405, 429 검증은 라우터의 Depends에서 처리
async def check_nickname_duplicate(request: Request):
    body = await request.json()

    # 400, 422 - 닉네임 검증
    nickname = validate_nickname(body.get("nickname"))

    try:
        # TODO: 실제 DB에서 닉네임 중복 확인 : 추후 구현
        is_available = True
        return JSONResponse(
            status_code=200,
            content=response_schema(
                message=successfully("nickname_checked"),
                data={"isAvailable": is_available},
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