# python에서 변경되지않는 상수는 대문자 + snake_case로 작성하는게 관례

# 이메일
EMAIL_MIN_LENGTH = 5
EMAIL_MAX_LENGTH = 50
EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# 비밀번호
PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 20
PASSWORD_PATTERN = [
    r'[A-Z]',                   # 대문자
    r'[a-z]',                   # 소문자
    r'[0-9]',                   # 숫자
    r'[!@#$%^&*(),.?":{}|<>]',  # 특수문자
]

# 닉네임
NICKNAME_MIN_LENGTH = 1
NICKNAME_MAX_LENGTH = 10

# 게시글 제목
TITLE_MIN_LENGTH = 1
TITLE_MAX_LENGTH = 26

# 게시글 내용
CONTENT_MIN_LENGTH = 1

# 게시글 이미지 URL
POST_IMAGE_URL_MIN_LENGTH = 1

# 프로필 이미지 URL
PROFILE_IMAGE_URL_MIN_LENGTH = 1

# HTTP 메서드
HTTP_METHOD_GET = "GET"
HTTP_METHOD_POST = "POST"
HTTP_METHOD_PATCH = "PATCH"
HTTP_METHOD_PUT = "PUT"
HTTP_METHOD_DELETE = "DELETE"

# 요청 횟수 제한
REQUESTS_MAX_COUNT = 5
REQUESTS_TIME_WINDOW_SECONDS = 60