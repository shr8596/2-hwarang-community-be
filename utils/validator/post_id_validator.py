# 게시글 id 유효성 검사 함수
def validate_post_id(post_id: int) -> bool:

    # 음수 체크
    if post_id < 0:
        return False

    return True
