import secrets
from datetime import datetime, timedelta
from typing import Dict, Optional

class SessionStore:
    """메모리 기반 세션 저장소"""

    def __init__(self):
        # 메모리에 세션 저장 {session_id: session_data}
        self._sessions: Dict[str, dict] = {}
        self._session_timeout = timedelta(hours=24)

    def create_session(self, user_id: str, user_data: dict) -> str:
        """새 세션 생성 및 세션 ID 반환"""
        session_id = secrets.token_urlsafe(32)

        self._sessions[session_id] = {
            "user_id": user_id,
            "user_data": user_data,
            "created_at": datetime.now(),
            "last_accessed": datetime.now(),
        }

        return session_id

    def get_session(self, session_id: str) -> Optional[dict]:
        """세션 ID로 세션 데이터 조회"""
        session = self._sessions.get(session_id)

        if not session:
            return None

        # 세션 만료 확인
        if datetime.now() - session["last_accessed"] > self._session_timeout:
            self.delete_session(session_id)
            return None

        # 마지막 접근 시간 업데이트
        session["last_accessed"] = datetime.now()
        return session

    def delete_session(self, session_id: str) -> bool:
        """세션 삭제"""
        if session_id in self._sessions:
            del self._sessions[session_id]
            return True
        return False

    def cleanup_expired_sessions(self):
        """만료된 세션 정리"""
        now = datetime.now()
        expired = [
            sid for sid, session in self._sessions.items()
            if now - session["last_accessed"] > self._session_timeout
        ]

        for sid in expired:
            del self._sessions[sid]

# 전역 세션 저장소 인스턴스
session_store = SessionStore()
