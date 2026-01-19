from utils import constants


# 게시글 내용 유효성 검사 함수
def validate_content(content: str) -> bool:
    # content: str이지만 타입힌트는 강제성이 없으므로 None 체크도 필요
    if content is None:
        return False

    # 길이 제한 검사 (최소 1자)
    if len(content) < constants.CONTENT_MIN_LENGTH:
        return False

    # 모든 검사를 통과하면 유효한 내용
    return True
