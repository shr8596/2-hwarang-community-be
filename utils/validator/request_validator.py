from fastapi import HTTPException
from utils.response_schema import response_schema
import utils.error_message
from utils.validator import email_validator, password_validator, nickname_validator, title_validator, content_validator, post_image_url_validator, profile_image_url_validator, user_id_validator, post_id_validator, comment_id_validator, offset_validator, limit_validator


def validate_email(email: str) -> str:
    if email is None: # 400 - 이메일 누락
        raise HTTPException(
            status_code=400,
            detail=response_schema(
                message=utils.error_message.missing_required_field,
                data=None,
            ),
        )
    if not isinstance(email, str): # 400 - 이메일 자료형 안맞음
        raise HTTPException(
            status_code=400,
            detail=response_schema(
                message=utils.error_message.invalid_input("parameter"),
                data=None,
            ),
        )
    if not email_validator.validate_email(email): # 422 - 이메일 형식 잘못됨
        raise HTTPException(
            status_code=422,
            detail=response_schema(
                message=utils.error_message.invalid_input_format("email"),
                data=None,
            ),
        )
    return email

def validate_password(password: str) -> str:
    if password is None: # 400 - 비밀번호 누락
        raise HTTPException(
            status_code=400,
            detail=response_schema(
                message=utils.error_message.missing_required_field,
                data=None,
            ),
        )
    if not isinstance(password, str): # 400 - 비밀번호 자료형 안맞음
        raise HTTPException(
            status_code=400,
            detail=response_schema(
                message=utils.error_message.invalid_input("parameter"),
                data=None,
            ),
        )
    if not password_validator.validate_password(password): # 422 - 비밀번호 형식 잘못됨
        raise HTTPException(
            status_code=422,
            detail=response_schema(
                message=utils.error_message.invalid_input_format("password"),
                data=None,
            ),
        )
    return password

def validate_user_id(user_id: int) -> int:
    if user_id is None: # 400 - user_id 누락
        raise HTTPException(
            status_code=400,
            detail=response_schema(
                message=utils.error_message.missing_required_field,
                data=None,
            ),
        )
    if not isinstance(user_id, int): # 400 - user_id 자료형 안맞음
        raise HTTPException(
            status_code=400,
            detail=response_schema(
                message=utils.error_message.invalid_input("parameter"),
                data=None,
            ),
        )
    if not user_id_validator.validate_user_id(user_id): # 422 - user_id 형식 잘못됨
        raise HTTPException(
            status_code=422,
            detail=response_schema(
                message=utils.error_message.invalid_input_format("user_id"),
                data=None,
            ),
        )
    return user_id

def validate_nickname(nickname: str) -> str:
    if nickname is None: # 400 - 닉네임 누락
        raise HTTPException(
            status_code=400,
            detail=response_schema(
                message=utils.error_message.missing_required_field,
                data=None,
            ),
        )
    if not isinstance(nickname, str): # 400 - 닉네임 자료형 안맞음
        raise HTTPException(
            status_code=400,
            detail=response_schema(
                message=utils.error_message.invalid_input("parameter"),
                data=None,
            ),
        )
    if not nickname_validator.validate_nickname(nickname): # 422 - 닉네임 형식 잘못됨
        raise HTTPException(
            status_code=422,
            detail=response_schema(
                message=utils.error_message.invalid_input_format("nickname"),
                data=None,
            ),
        )
    return nickname

def validate_profile_image_url(profile_image_url: str) -> str:
    if profile_image_url is None: # 400 - 프로필 이미지 URL 누락
        raise HTTPException(
            status_code=400,
            detail=response_schema(
                message=utils.error_message.missing_required_field,
                data=None,
            ),
        )
    if not isinstance(profile_image_url, str): # 400 - 프로필 이미지 URL 자료형 안맞음
        raise HTTPException(
            status_code=400,
            detail=response_schema(
                message=utils.error_message.invalid_input("parameter"),
                data=None,
            ),
        )
    if not profile_image_url_validator.validate_profile_image_url(profile_image_url): # 422 - 프로필 이미지 URL 형식 잘못됨
        raise HTTPException(
            status_code=422,
            detail=response_schema(
                message=utils.error_message.invalid_input_format("profile_image_url"),
                data=None,
            ),
        )
    return profile_image_url

def validate_title(title: str) -> str:
    if title is None: # 400 - 제목 누락
        raise HTTPException(
            status_code=400,
            detail=response_schema(
                message=utils.error_message.missing_required_field,
                data=None,
            ),
        )
    if not isinstance(title, str): # 400 - 제목 자료형 안맞음
        raise HTTPException(
            status_code=400,
            detail=response_schema(
                message=utils.error_message.invalid_input("parameter"),
                data=None,
            ),
        )
    if not title_validator.validate_title(title): # 422 - 제목 형식 잘못됨 (길이 제한)
        raise HTTPException(
            status_code=422,
            detail=response_schema(
                message=utils.error_message.invalid_input_format("title"),
                data=None,
            ),
        )
    return title

def validate_content(content: str) -> str:
    if content is None: # 400 - 내용 누락
        raise HTTPException(
            status_code=400,
            detail=response_schema(
                message=utils.error_message.missing_required_field,
                data=None,
            ),
        )
    if not isinstance(content, str): # 400 - 내용 자료형 안맞음
        raise HTTPException(
            status_code=400,
            detail=response_schema(
                message=utils.error_message.invalid_input("parameter"),
                data=None,
            ),
        )
    if not content_validator.validate_content(content): # 422 - 내용 형식 잘못됨 (길이 제한)
        raise HTTPException(
            status_code=422,
            detail=response_schema(
                message=utils.error_message.invalid_input_format("content"),
                data=None,
            ),
        )
    return content

def validate_post_image_url(post_image_url: str) -> str:
    if post_image_url is None: # 400 - 이미지 URL 누락
        raise HTTPException(
            status_code=400,
            detail=response_schema(
                message=utils.error_message.missing_required_field,
                data=None,
            ),
        )
    if not isinstance(post_image_url, str): # 400 - 이미지 URL 자료형 안맞음
        raise HTTPException(
            status_code=400,
            detail=response_schema(
                message=utils.error_message.invalid_input("parameter"),
                data=None,
            ),
        )
    if not post_image_url_validator.validate_post_image_url(post_image_url): # 422 - 이미지 URL 형식 잘못됨
        raise HTTPException(
            status_code=422,
            detail=response_schema(
                message=utils.error_message.invalid_input_format("post_image_url"),
                data=None,
            ),
        )
    return post_image_url

def validate_post_id(post_id: int) -> int:
    if post_id is None: # 400 - post_id 누락
        raise HTTPException(
            status_code=400,
            detail=response_schema(
                message=utils.error_message.missing_required_field,
                data=None,
            ),
        )
    if not isinstance(post_id, int): # 400 - post_id 자료형 안맞음
        raise HTTPException(
            status_code=400,
            detail=response_schema(
                message=utils.error_message.invalid_input("parameter"),
                data=None,
            ),
        )
    if not post_id_validator.validate_post_id(post_id): # 422 - post_id 형식 잘못됨
        raise HTTPException(
            status_code=422,
            detail=response_schema(
                message=utils.error_message.invalid_input_format("post_id"),
                data=None,
            ),
        )
    return post_id

def validate_comment_id(comment_id: int) -> int:
    if comment_id is None: # 400 - comment_id 누락
        raise HTTPException(
            status_code=400,
            detail=response_schema(
                message=utils.error_message.missing_required_field,
                data=None,
            ),
        )
    if not isinstance(comment_id, int): # 400 - comment_id 자료형 안맞음
        raise HTTPException(
            status_code=400,
            detail=response_schema(
                message=utils.error_message.invalid_input("parameter"),
                data=None,
            ),
        )
    if not comment_id_validator.validate_comment_id(comment_id): # 422 - comment_id 형식 잘못됨
        raise HTTPException(
            status_code=422,
            detail=response_schema(
                message=utils.error_message.invalid_input_format("comment_id"),
                data=None,
            ),
        )
    return comment_id

def validate_offset(offset: int) -> int:
    if not isinstance(offset, int): # 400 - offset 자료형 안맞음
        raise HTTPException(
            status_code=400,
            detail=response_schema(
                message=utils.error_message.invalid_input("parameter"),
                data=None,
            ),
        )
    if not offset_validator.validate_offset(offset): # 422 - offset 형식 잘못됨
        raise HTTPException(
            status_code=422,
            detail=response_schema(
                message=utils.error_message.invalid_input_format("offset"),
                data=None,
            ),
        )
    return offset

def validate_limit(limit: int) -> int:
    if not isinstance(limit, int): # 400 - limit 자료형 안맞음
        raise HTTPException(
            status_code=400,
            detail=response_schema(
                message=utils.error_message.invalid_input("parameter"),
                data=None,
            ),
        )
    if not limit_validator.validate_limit(limit): # 422 - limit 형식 잘못됨
        raise HTTPException(
            status_code=422,
            detail=response_schema(
                message=utils.error_message.invalid_input_format("limit"),
                data=None,
            ),
        )
    return limit
