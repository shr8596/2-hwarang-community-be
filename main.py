from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routes import api_router

app = FastAPI()

# CORS 설정(필수 미들웨어)
# 각다른 도메인에서 실행되는 프론트엔드(React, Vue 등)가 이 API를 호출할 수 있도록 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",      # React 기본 포트
        "http://localhost:5173",      # Vite 기본 포트
        "http://localhost:8080",      # Vue 기본 포트
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:8080",
    ],
    allow_credentials=True,           # 쿠키/인증 정보 허용
    allow_methods=["*"],              # 모든 HTTP 메서드 허용 (GET, POST, PUT, DELETE 등)
    allow_headers=["*"],              # 모든 헤더 허용 (Authorization, Content-Type 등)
)

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)