import re
from utils import constants


# 비밀번호 유효성 검사 함수
def validate_password(password: str) -> bool:
    # password: str이지만 타입힌트는 강제성이 없으므로 None 체크도 필요
    if password is None:
        return False

    # 기획에는 없지만 공백 없어야
    if " " in password:
        return False

    # 길이 제한 검사
    if len(password) < constants.PASSWORD_MIN_LENGTH or len(password) > constants.PASSWORD_MAX_LENGTH:
        return False

    # 대문자, 소문자, 숫자, 특수문자 각각 1개 이상 필요
    for pattern in constants.PASSWORD_PATTERN:
        if re.search(pattern, password) is None:
            return False

    # 모든 검사를 통과하면 유효한 비밀번호
    return True