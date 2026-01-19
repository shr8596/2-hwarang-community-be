from controllers.users import user_controller
from fastapi import APIRouter, Request

router = APIRouter()

# 회원 로그인
@router.post("/login")
async def login(request: Request):
    return await user_controller.login_user(request)

# 회원 로그아웃
@router.delete("/logout")
async def logout(request: Request):
    return await user_controller.logout_user(request)

# 회원 탈퇴
@router.delete("/user/me/{user_id}")
async def withdraw(user_id: str, request: Request):
    return await user_controller.delete_user(user_id, request)

# 회원 정보 조회
@router.get("/user/me/{user_id}")
async def read_user_info(user_id: str, request: Request):
    return await user_controller.read_user(user_id, request)
