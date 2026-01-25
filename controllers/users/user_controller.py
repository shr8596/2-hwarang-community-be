from fastapi import Request, HTTPException, Cookie, Depends
from fastapi.responses import JSONResponse
from utils.response_schema import response_schema
from utils.success_message import successfully
import utils.error_message
from utils.validator.request_validator import (
    validate_email, validate_password, validate_user_id, validate_nickname, validate_profile_image_url,
    validate_email_not_duplicate, validate_nickname_not_duplicate, check_login_credentials, check_user_permission, check_user_exists
)
from utils.session_store import session_store
from utils.password import hash_password, verify_password
from dependencies.auth_dependency import get_current_user
from typing import Optional

# 사용자 임시 데이터 (메모리 저장소)
# 실제로는 DB에 저장되어야 함
MOCK_USERS = {
    "test@gmail.com": {
        "userId": "1",
        "email": "test@gmail.com",
        "password": "$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5jtJ3qKJ3q7EK",  # "password123" 해싱
        "userNickname": "startup",
        "profileImageUrl": "http~~~",
        "isWithdrawn": False,
        "createdAt": "2026-01-01T00:00:00.000Z",
        "updatedAt": "2026-01-01T00:00:00.000Z",
    }
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

    # 409 - 이메일 중복 확인
    validate_email_not_duplicate(email, MOCK_USERS)

    # 409 - 닉네임 중복 확인
    validate_nickname_not_duplicate(nickname, MOCK_USERS)

    try:
        # 비밀번호 해싱
        hashed_password = hash_password(password)

        # TODO: 실제 DB에 사용자 생성
        # 임시로 메모리에 저장
        user_id = str(len(MOCK_USERS) + 1)
        MOCK_USERS[email] = {
            "userId": user_id,
            "email": email,
            "password": hashed_password,
            "userNickname": nickname,
            "profileImageUrl": profile_image_url,
            "isWithdrawn": False,
            "createdAt": "2026-01-21T00:00:00.000Z",
            "updatedAt": "2026-01-21T00:00:00.000Z",
        }

        # 세션 생성
        session_id = session_store.create_session(
            user_id=email,
            user_data={
                "userId": user_id,
                "email": email,
                "nickname": nickname,
            }
        )

        # 쿠키에 세션 ID 설정
        response = JSONResponse(
            status_code=201,
            content=response_schema(
                message=successfully("user_created"),
                data={
                    "userId": user_id,
                    "email": email,
                    "nickname": nickname,
                    "sessionId": session_id,  # 세션ID 추가
                },
            ),
        )

        response.set_cookie(
            key="session_id",
            value=session_id,
            httponly=False,
            # domain=None,
            secure=False,  # 개발 환경: False, 프로덕션: True
            samesite="lax",
            max_age=86400,  # 24시간
            path="/",
        )

        # 쿠키 정보 로그 출력
        print(f"\n{'='*80}", flush=True)
        print(f"[쿠키 설정] 회원가입 성공 - FE로 전송할 쿠키 데이터:", flush=True)
        print(f"  - key: session_id", flush=True)
        print(f"  - value: {session_id}", flush=True)
        print(f"  - httponly: False (JavaScript 접근 가능)", flush=True)
        print(f"  - domain: None (현재 도메인만)", flush=True)
        print(f"  - secure: False (HTTP 허용)", flush=True)
        print(f"  - samesite: lax (CSRF 보호)", flush=True)
        print(f"  - max_age: 86400초 (24시간)", flush=True)
        print(f"  - path: / (모든 경로)", flush=True)
        print(f"{'='*80}\n", flush=True)

        return response
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

    # 401 - 사용자 인증 확인 (validator로 이동)
    user = check_login_credentials(email, password, MOCK_USERS, verify_password)

    try:
        # 세션 생성
        session_id = session_store.create_session(
            user_id=email,
            user_data={
                "userId": user["userId"],
                "email": email,
                "nickname": user["userNickname"],
            }
        )

        # 쿠키에 세션 ID 설정
        response = JSONResponse(
            status_code=200,
            content=response_schema(
                message=successfully("logged_in"),
                data={
                    "userId": user["userId"],
                    "email": email,
                    "nickname": user["userNickname"],
                    "sessionId": session_id,  # 세션ID 추가
                },
            ),
        )

        response.set_cookie(
            key="session_id",
            value=session_id,
            httponly=False,
            # domain=None,
            secure=False,  # 개발 환경: False, 프로덕션: True
            samesite="lax",
            max_age=86400,  # 24시간
            path="/",
        )

        # 쿠키 정보 로그 출력
        print(f"\n{'='*80}", flush=True)
        print(f"[쿠키 설정] 로그인 성공 - FE로 전송할 쿠키 데이터:", flush=True)
        print(f"  - key: session_id", flush=True)
        print(f"  - value: {session_id}", flush=True)
        print(f"  - httponly: False (JavaScript 접근 가능)", flush=True)
        print(f"  - domain: None (현재 도메인만)", flush=True)
        print(f"  - secure: False (HTTP 허용)", flush=True)
        print(f"  - samesite: lax (CSRF 보호)", flush=True)
        print(f"  - max_age: 86400초 (24시간)", flush=True)
        print(f"  - path: / (모든 경로)", flush=True)
        print(f"{'='*80}\n", flush=True)

        return response
    except Exception:
        raise HTTPException(
            status_code=500,
            detail=response_schema(
                message=utils.error_message.internal_server_error,
                data=None,
            ),
        )

# 회원 로그아웃
# 405, 429 검증은 라우터의 Depends에서 처리
async def logout_user(session_id: Optional[str] = Cookie(None)):
    # 세션 삭제
    if session_id:
        session_store.delete_session(session_id)

    response = JSONResponse(
        status_code=200,
        content=response_schema(
            message=successfully("logged_out"),
            data=None,
        ),
    )

    # 쿠키 삭제
    response.delete_cookie(key="session_id")

    return response

# 회원 탈퇴
# 401, 405, 429 검증은 라우터의 Depends에서 처리
async def delete_user(
    user_id: int,
    current_user: dict = Depends(get_current_user),
    session_id: Optional[str] = Cookie(None)
):
    # 400, 422 - user_id 검증
    user_id = validate_user_id(user_id)

    # 403 - 본인 확인 (validator로 이동)
    check_user_permission(user_id, current_user)

    try:
        # TODO: 실제 DB에서 사용자 삭제 또는 탈퇴 처리
        # 임시로 MOCK_USERS에서 삭제
        email = current_user["user_id"]
        if email in MOCK_USERS:
            del MOCK_USERS[email]

        # 세션 삭제
        if session_id:
            session_store.delete_session(session_id)

        response = JSONResponse(
            status_code=200,
            content=response_schema(
                message=successfully("account_deleted"),
                data=None,
            ),
        )

        # 쿠키 삭제
        response.delete_cookie(key="session_id")

        return response
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
async def read_user(
    user_id: int,
    current_user: dict = Depends(get_current_user)
):
    # 400, 422 - user_id 검증
    user_id = validate_user_id(user_id)

    # 403 - 본인 확인 (validator로 이동)
    check_user_permission(user_id, current_user)

    try:
        # TODO: 실제 DB에서 사용자 정보 조회
        email = current_user["user_id"]

        # 404 - 사용자 존재 여부 확인 (validator로 이동)
        user = check_user_exists(email, MOCK_USERS)

        return JSONResponse(
            status_code=200,
            content=response_schema(
                message=successfully("user_fetched"),
                data={
                    "userId": user["userId"],
                    "email": user["email"],
                    "userNickname": user["userNickname"],
                    "profileImageUrl": user["profileImageUrl"],
                    "isWithdrawn": user["isWithdrawn"],
                    "createdAt": user["createdAt"],
                    "updatedAt": user["updatedAt"],
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

# 회원 정보 수정(비밀번호)
# 401, 405, 429 검증은 라우터의 Depends에서 처리
async def update_user_password(
    user_id: int,
    request: Request,
    current_user: dict = Depends(get_current_user)
):
    body = await request.json()

    # 400, 422 - user_id 검증
    user_id = validate_user_id(user_id)

    # 400, 422 - 새 비밀번호 검증
    password = validate_password(body.get("password"))

    # 403 - 본인 확인 (validator로 이동)
    check_user_permission(user_id, current_user)

    try:
        # TODO: 실제 DB에서 비밀번호 업데이트
        email = current_user["user_id"]

        # 404 - 사용자 존재 여부 확인 (validator로 이동)
        user = check_user_exists(email, MOCK_USERS)

        # 비밀번호 해싱
        hashed_password = hash_password(password)
        MOCK_USERS[email]["password"] = hashed_password

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
async def update_user_nickname(
    user_id: int,
    request: Request,
    current_user: dict = Depends(get_current_user)
):
    body = await request.json()

    # 400, 422 - user_id 검증
    user_id = validate_user_id(user_id)

    # 400, 422 - 닉네임 검증
    nickname = validate_nickname(body.get("nickname"))

    # 403 - 본인 확인 (validator로 이동)
    check_user_permission(user_id, current_user)

    try:
        # TODO: 실제 DB에서 닉네임 업데이트
        email = current_user["user_id"]

        # 404 - 사용자 존재 여부 확인 (validator로 이동)
        user = check_user_exists(email, MOCK_USERS)

        MOCK_USERS[email]["userNickname"] = nickname

        return JSONResponse(
            status_code=200,
            content=response_schema(
                message=successfully("nickname_updated"),
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

# 회원 정보 수정(프로필 이미지 URL)
# 401, 405, 429 검증은 라우터의 Depends에서 처리
async def update_user_profile_image_url(
    user_id: int,
    request: Request,
    current_user: dict = Depends(get_current_user)
):
    body = await request.json()

    # 400, 422 - user_id 검증
    user_id = validate_user_id(user_id)

    # 400, 422 - 프로필 이미지 URL 검증 (선택적)
    profile_image_url = body.get("profileImageUrl")
    if profile_image_url is not None:
        profile_image_url = validate_profile_image_url(profile_image_url)

    # 403 - 본인 확인 (validator로 이동)
    check_user_permission(user_id, current_user)

    try:
        # TODO: 실제 DB에서 프로필 이미지 URL 업데이트
        email = current_user["user_id"]

        # 404 - 사용자 존재 여부 확인 (validator로 이동)
        user = check_user_exists(email, MOCK_USERS)

        MOCK_USERS[email]["profileImageUrl"] = profile_image_url

        return JSONResponse(
            status_code=200,
            content=response_schema(
                message=successfully("profile_image_url_updated"),
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

# 회원 이메일 중복 확인
# 405, 429 검증은 라우터의 Depends에서 처리
async def check_email_duplicate(request: Request):
    body = await request.json()

    # 400, 422 - 이메일 검증
    email = validate_email(body.get("email"))

    try:
        # 이메일 중복 확인
        is_available = email not in MOCK_USERS
        return JSONResponse(
            status_code=200,
            content=response_schema(
                message=successfully("email_checked"),
                data={
                    "isAvailable": is_available
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

# 회원 닉네임 중복 확인
# 405, 429 검증은 라우터의 Depends에서 처리
async def check_nickname_duplicate(request: Request):
    body = await request.json()

    # 400, 422 - 닉네임 검증
    nickname = validate_nickname(body.get("nickname"))

    try:
        is_available = not any(
            user["userNickname"] == nickname
            for user in MOCK_USERS.values()
        )
        return JSONResponse(
            status_code=200,
            content=response_schema(
                message=successfully("nickname_checked"),
                data={
                    "isAvailable": is_available
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