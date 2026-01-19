import uuid
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from utils.response_schema import response_schema
from utils.success_message import successfully
import utils.error_message
from utils.validator import nickname_validator
from utils.validator.request_validator import validate_email, validate_password, validate_user_id

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

# 회원 로그인
async def login_user(request: Request):
    body = await request.json()
    session_id = request.session.get("sessionID")

    # 400, 422 - 이메일 검증
    email = validate_email(body.get("email"))

    # 400, 422 - 비밀번호 검증
    password = validate_password(body.get("password"))

    # 401
    if session_id is None:
        raise HTTPException(
            status_code=401,
            detail=response_schema(
                message=utils.error_message.authentication_required,
                data=None,
            ),
        )

    # 405
    if request.method != "POST":  # HTTP 메서드 지원 안됨
        raise HTTPException(
            status_code=405,
            detail=response_schema(
                message=utils.error_message.http_method_not_supported,
                data=None,
            ),
        )

    # 429
    # TODO : 로그인 시도 횟수, 시간 등으로 제한 필요

    try:
        session_id = request.session.get("sessionID")
        if not session_id:
            session_id = str(uuid.uuid4())
            request.session["sessionID"] = session_id
            request.session["email"] = email
        return JSONResponse(
            status_code = 200,
            content = response_schema(
                message = successfully("logged_in"),
                data = {
                    "sessionID": session_id,
                    "email": email,
                },
            ),
        )
    except Exception:
        raise HTTPException(
            status_code = 500,
            detail = response_schema(
                message = utils.error_message.internal_server_error,
                data = None,
            ),
        )

# 회원 로그아웃
async def logout_user(request: Request):
    session_id = request.session.get("sessionID")

    # 401
    if session_id is None: # 인증 필요
        raise HTTPException(
            status_code=401,
            detail=response_schema(
                message=utils.error_message.authentication_required,
                data=None,
            ),
        )

    # 405
    if request.method != "DELETE": # HTTP 메서드 지원 안됨
        raise HTTPException(
            status_code=405,
            detail=response_schema(
                message=utils.error_message.http_method_not_supported,
                data=None,
            ),
        )

    # 429
    # TODO : 로그아웃 시도 횟수, 시간 등으로 제한 필요

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
async def delete_user(user_id: str, request: Request):
    session_id = request.session.get("sessionID")

    # 400, 422 - user_id 검증 (숫자인지 확인)
    validate_user_id(user_id)

    # 401
    if session_id is None:  # 인증 필요
        raise HTTPException(
            status_code=401,
            detail=response_schema(
                message=utils.error_message.authentication_required,
                data=None,
            ),
        )

    # 405
    if request.method != "DELETE":  # HTTP 메서드 지원 안됨
        raise HTTPException(
            status_code=405,
            detail=response_schema(
                message=utils.error_message.http_method_not_supported,
                data=None,
            ),
        )

    # 429
    # TODO : 회원 탈퇴 시도 횟수, 시간 등으로 제한 필요

    try:
        # TODO: 실제 DB에서 사용자 삭제는 추후 구현
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
async def read_user(user_id: str, request: Request):
    session_id = request.session.get("sessionID")

    # 400, 422 - user_id 검증 (숫자인지 확인)
    validate_user_id(user_id)

    # 401
    if session_id is None:  # 인증 필요
        raise HTTPException(
            status_code=401,
            detail=response_schema(
                message=utils.error_message.authentication_required,
                data=None,
            ),
        )

    # 405
    if request.method != "GET":  # HTTP 메서드 지원 안됨
        raise HTTPException(
            status_code=405,
            detail=response_schema(
                message=utils.error_message.http_method_not_supported,
                data=None,
            ),
        )

    # 429
    # TODO : 회원 정보 조회 시도 횟수, 시간 등으로 제한 필요

    try:
        # TODO: 실제 DB에서 사용자 정보 조회는 추후 구현
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
# TODO: 구현 필요

# 회원 정보 수정(닉네임)
# TODO: 구현 필요

# 회원 정보 수정(프로필 이미지)
# TODO: 구현 필요

# 회원 이메일 중복 확인
# TODO: 구현 필요

# 회원 닉네임 중복 확인
# TODO: 구현 필요