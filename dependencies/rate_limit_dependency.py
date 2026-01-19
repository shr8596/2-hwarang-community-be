from fastapi import Request, HTTPException
from utils.response_schema import response_schema
import utils.error_message
import utils.constants
from datetime import datetime, timedelta
from collections import defaultdict

# defaultdict : 없는 키에 접근할 때 자동으로 기본값을 생성해주는 딕셔너리
request_counts = defaultdict(list)


async def rate_limiter(request: Request):
    client_ip = request.client.host
    now = datetime.now()

    # 기록 정리 (시간 윈도우 밖의 요청 제거)
    request_counts[client_ip] = [
        req_time for req_time in request_counts[client_ip]
        if now - req_time < timedelta(seconds=utils.constants.REQUESTS_TIME_WINDOW_SECONDS)
    ]

    # 요청 횟수 확인
    if len(request_counts[client_ip]) >= utils.constants.REQUESTS_MAX_COUNT:  # 429 - 요청 횟수 초과
        raise HTTPException(
            status_code=429,
            detail=response_schema(
                message=utils.error_message.rate_limit_exceeded,
                data=None,
            ),
        )

    # 현재 요청 기록 추가
    request_counts[client_ip].append(now)