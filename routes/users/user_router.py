from fastapi import APIRouter
from controllers.users import user_controller

router = APIRouter(prefix="/users")


# 특정 사용자 상세 조회
@router.get("/me/{user_id}")
def get_user_info(user_id: str):
    return user_controller.get_user_info(user_id)