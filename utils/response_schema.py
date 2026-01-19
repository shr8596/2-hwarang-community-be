from typing import Any


# API 응답 시 JSONResponse(성공), HTTPException(실패)에서 공통된 응답 스키마를 정의
def response_schema(message: str, data: Any = None) -> dict:
    return {
        "message"   : message,
        "data"      : data,
    }