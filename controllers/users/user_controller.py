import uuid
from fastapi import Request, HTTPException, Response
from fastapi.responses import JSONResponse

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
    email = body.get("email")
    password = body.get("password")

    # 필수값 검증
    if not email or not password:
        raise HTTPException(status_code=400, detail="email_or_password_required")

    # 세션 생성
    session_id = request.session.get("sessionID")
    if not session_id:
        session_id = str(uuid.uuid4())
        request.session["sessionID"] = session_id
        request.session["email"] = email

    return JSONResponse(
        status_code=200,
        content={"session_id": session_id, "email": email}
    )

# 회원 로그아웃
async def logout_user(request: Request):
    try:
        request.session.clear()
        return Response(status_code=204)
    except Exception:
        raise HTTPException(status_code=500, detail="logout_failed")

# 회원 탈퇴
# TODO: 구현 필요

# 회원 정보 조회
def get_user_info(user_id: str):
    # do something...
    return {
        "message": "user_fetched_successfully",
        "user_id" : user_id,
        "data": user_model,
    }

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