from utils import constants


# 게시글 이미지 URL 유효성 검사 함수
def validate_post_image_url(post_image_url: str) -> bool:

    # 길이 제한 검사 (최소 1자)
    if len(post_image_url) < constants.POST_IMAGE_URL_MIN_LENGTH:
        return False

    # 모든 검사를 통과하면 유효한 URL
    return True
