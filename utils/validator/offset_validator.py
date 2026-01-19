# offset 유효성 검사 함수
def validate_offset(offset: int) -> bool:

    # 음수 체크
    if offset < 0:
        return False

    return True