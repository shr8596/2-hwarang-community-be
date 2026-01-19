from controllers.users import user_controller
from fastapi import APIRouter, Request, Depends
from dependencies.auth_dependency import get_current_session
from dependencies.rate_limit_dependency import rate_limiter
from dependencies.method_dependency import require_post, require_get, require_patch, require_delete

router = APIRouter()

# Depends로 라우터 호출 전 405, 401, 429 에러 처리
# 405: require_* (method_dependency)
# 401: get_current_session (auth_dependency)
# 429: rate_limiter (rate_limit_dependency)

# 회원가입
@router.post("/signup", dependencies=[Depends(require_post), Depends(rate_limiter)])
async def signup(request: Request):
    return await user_controller.create_user(request)

# 회원 로그인
@router.post("/login", dependencies=[Depends(require_post), Depends(rate_limiter)])
async def login(request: Request):
    return await user_controller.login_user(request)

# 회원 로그아웃
@router.delete("/logout", dependencies=[Depends(require_delete), Depends(get_current_session), Depends(rate_limiter)])
async def logout(request: Request):
    return await user_controller.logout_user(request)

# 회원 탈퇴
@router.delete("/me/{user_id}", dependencies=[Depends(require_delete), Depends(get_current_session), Depends(rate_limiter)])
async def withdraw(user_id: str, request: Request):
    return await user_controller.delete_user(user_id, request)

# 회원 정보 조회
@router.get("/me/{user_id}", dependencies=[Depends(require_get), Depends(get_current_session), Depends(rate_limiter)])
async def read_user_info(user_id: str, request: Request):
    return await user_controller.read_user(user_id, request)

# 회원 정보 수정(비밀번호)
@router.patch("/me/password/{user_id}", dependencies=[Depends(require_patch), Depends(get_current_session), Depends(rate_limiter)])
async def update_password(user_id: str, request: Request):
    return await user_controller.update_user_password(user_id, request)

# 회원 정보 수정(닉네임)
@router.patch("/me/nickname/{user_id}", dependencies=[Depends(require_patch), Depends(get_current_session), Depends(rate_limiter)])
async def update_nickname(user_id: str, request: Request):
    return await user_controller.update_user_nickname(user_id, request)

# 회원 정보 수정(프로필 이미지 URL)
@router.patch("/me/profile-image-url/{user_id}", dependencies=[Depends(require_patch), Depends(get_current_session), Depends(rate_limiter)])
async def update_profile_image_url(user_id: str, request: Request):
    return await user_controller.update_user_profile_image_url(user_id, request)


