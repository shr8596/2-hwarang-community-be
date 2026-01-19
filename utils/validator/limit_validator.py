# limit 유효성 검사 함수
def validate_limit(limit: int) -> bool:

    # 음수 체크
    if limit < 0:
        return False

    return True
