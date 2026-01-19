from fastapi import APIRouter


router = APIRouter(prefix="/posts", tags=["posts"])


# 게시글 작성
@router.post("")
def create_post():
    return ""

# 게시글 전체 목록 조회
@router.get("?offset={offset}&limit={limit}")
def read_posts():
    return ""

# 게시글 상세 조회
@router.get("/{post_id}")
def read_post():
    return ""

# 게시글 수정
@router.put("/{post_id}")
def update_post():
    return ""

# 게시글 삭제
@router.delete("/{post_id}")
def delete_post():
    return ""

# 게시글 좋아요 추가
@router.patch("/{post_id}/add-like")
def like_post():
    return ""

# 게시글 좋아요 제거
@router.patch("/{post_id}/remove-like")
def unlike_post():
    return ""