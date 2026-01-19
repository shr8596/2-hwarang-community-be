from utils import constants


# 프로필 이미지 URL 유효성 검사 함수
def validate_profile_image_url(profile_image_url: str) -> bool:
    # 길이 제한 검사 (최소 1자)
    if len(profile_image_url) < constants.PROFILE_IMAGE_URL_MIN_LENGTH:
        return False

    # 모든 검사를 통과하면 유효한 URL
    return True
