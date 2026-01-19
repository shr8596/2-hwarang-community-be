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