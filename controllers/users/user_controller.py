from fastapi import HTTPException

# 사용자 임시 데이터
user_model =  {
    "userId"            : "1",
    "userNickname"      : "startup",
    "email"             : "test@gmail.com",
    "profileImageUrl"   : "http~~~",
    "isWithdrawn"       : "false",
    "createdAt"         : "2026-01-01T00:00:00.000Z",
    "updatedAt"         : "2026-01-01T00:00:00.000Z",
}

# 회원가입

# 회원 로그인

# 회원 정보 조회
def get_user_info():

    # do something...

    return {
        "message": "user_fetched_successfully",
        "data": user_model,
    }

# 회원 로그아웃

# 회원 탈퇴

# 회원 정보 조회

# 회원 정보 수정(비밀번호)

# 회원 정보 수정(닉네임)

# 회원 정보 수정(프로필 이미지)

# 회원 이메일 중복 확인

# 회원 닉네임 중복 확인