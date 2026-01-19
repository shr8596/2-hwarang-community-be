import re
from utils import constants


# 이메일 유효성 검사 함수
def validate_email(email: str) -> bool:
    # email: str이지만 타입힌트는 강제성이 없으므로 None 체크도 필요
    if email is None:
        return False

    # 기획에는 없지만 공백 없어야 + 길이 제한도 임의로 설정
    if " " in email:
        return False
    if len(email) < constants.EMAIL_MIN_LENGTH or len(email) > constants.EMAIL_MAX_LENGTH:
        return False

    # 이메일 형식 필요
    if not re.match(constants.EMAIL_PATTERN, email):
        return False

    # 모든 검사를 통과하면 유효한 이메일
    return True