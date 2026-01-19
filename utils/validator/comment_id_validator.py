# 댓글 id 유효성 검사 함수
def validate_comment_id(comment_id: int) -> bool:
    if comment_id is None:
        return False

    # 음수 체크
    if comment_id < 0:
        return False

    return True
