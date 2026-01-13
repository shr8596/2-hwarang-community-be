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

# 회원 정보 조회
@router.get("/me/{user_id}")
def read_user_info(user_id: str):
    return user_controller.get_user_info(user_id)