from utils import constants


# 게시글 제목 유효성 검사 함수
def validate_title(title: str) -> bool:
    # title: str이지만 타입힌트는 강제성이 없으므로 None 체크도 필요
    if title is None:
        return False

    # 길이 제한 검사
    if len(title) < constants.TITLE_MIN_LENGTH or len(title) > constants.TITLE_MAX_LENGTH:
        return False

    # 모든 검사를 통과하면 유효한 제목
    return True