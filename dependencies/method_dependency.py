from fastapi import Request, HTTPException
from utils.response_schema import response_schema
import utils.error_message
import utils.constants

# 팩토리 패턴(Factory Pattern):
# 동일한 구조를 가진 여러 객체(함수)를 생성하는 패턴
# - 객체 생성 로직을 한 곳에 집중시켜 코드 중복을 제거
# - 새로운 객체 추가 시 기존 코드 수정 없이 확장 가능
def _create_method_checker(allowed_method: str):
    def method_checker(request: Request):
        if request.method != allowed_method:
            raise HTTPException(
                status_code=405,
                detail=response_schema(
                    message=utils.error_message.http_method_not_supported,
                    data=None,
                ),
            )
    return method_checker

require_post    = _create_method_checker(utils.constants.HTTP_METHOD_POST)
require_get     = _create_method_checker(utils.constants.HTTP_METHOD_GET)
require_patch   = _create_method_checker(utils.constants.HTTP_METHOD_PATCH)
require_delete  = _create_method_checker(utils.constants.HTTP_METHOD_DELETE)