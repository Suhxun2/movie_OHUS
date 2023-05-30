# CRUD
#  - CREATE : 생성
#  - READ   : 조회
#  - UPDATE : 수정
#  - DELETE : 삭제

from db.connection import conn


# 리뷰 저장(MongoDB)
def add_review(data):
    collection = conn()
    collection.insert_one(date)  # Review 저장


# 리뷰 조회(MongoDB)
def get_reviews():
    pass