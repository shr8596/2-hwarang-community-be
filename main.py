from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routes import api_router

app = FastAPI()

# CORS 설정 (먼저 추가)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 요청 로깅 미들웨어 (나중에 추가)
@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"\n{'='*80}", flush=True)
    print(f"[요청] {request.method} {request.url.path}", flush=True)
    print(f"클라이언트: {request.client.host}", flush=True)
    print(f"{'='*80}\n", flush=True)

    response = await call_next(request)

    print(f"[응답] {request.method} {request.url.path} → {response.status_code}\n", flush=True)
    return response


# 헬스체크 엔드포인트
@app.get("/api/health")
async def health_check():
    return {"status": "ok", "message": "BE server is running"}

app.include_router(api_router)

if __name__ == "__main__":
    print("서버 시작: http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
