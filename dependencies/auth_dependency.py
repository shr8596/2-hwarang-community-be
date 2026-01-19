from fastapi import Request, HTTPException
from utils.response_schema import response_schema
import utils.error_message


# 현재 세션을 가져오는 의존성
async def get_current_session(request: Request) -> str:
    session_id = request.session.get("sessionID")
    if session_id is None:
        raise HTTPException(
            status_code=401,
            detail=response_schema(
                message=utils.error_message.authentication_required,
                data=None,
            ),
        )
    return session_id