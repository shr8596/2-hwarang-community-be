from utils import constants


# 닉네임 유효성 검사 함수
def validate_nickname(nickname: str) -> bool:
    # nickname: str이지만 타입힌트는 강제성이 없으므로 None 체크도 필요
    if nickname is None:
        return False

    # 공백 없어야
    if " " in nickname:
        return False

    # 길이 제한 검사
    if len(nickname) < constants.NICKNAME_MIN_LENGTH or len(nickname) > constants.NICKNAME_MAX_LENGTH:
        return False

    # 모든 검사를 통과하면 유효한 닉네임
    return True