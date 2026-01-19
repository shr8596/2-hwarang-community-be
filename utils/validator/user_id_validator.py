# 사용자 id 유효성 검사 함수
def validate_user_id(user_id: int) -> bool:

    # 음수 체크
    if user_id < 0:
        return False

    return True
