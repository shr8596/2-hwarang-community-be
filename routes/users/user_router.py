from fastapi import APIRouter
from controllers.users import user_controller

router = APIRouter()


# 회원 정보 조회
@router.get("/me/{user_id}")
def read_user_info(user_id: str):
    return user_controller.get_user_info(user_id)