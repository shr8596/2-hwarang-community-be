from fastapi import Cookie, HTTPException
from typing import Optional
from utils.session_store import session_store
from utils.response_schema import response_schema
import utils.error_message


# 쿠키에서 세션 ID를 읽어 사용자 정보 반환
async def get_current_user(session_id: Optional[str] = Cookie(None)):
    """쿠키 기반 인증 - 세션 ID로 사용자 정보 조회"""

    # 세션 ID가 없는 경우
    if not session_id:
        raise HTTPException(
            status_code=401,
            detail=response_schema(
                message=utils.error_message.unauthorized,
                data=None,
            ),
        )

    # 세션 조회
    session = session_store.get_session(session_id)

    # 유효하지 않은 세션
    if not session:
        raise HTTPException(
            status_code=401,
            detail=response_schema(
                message=utils.error_message.unauthorized,
                data=None,
            ),
        )

    return session
