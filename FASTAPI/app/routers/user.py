from fastapi import APIRouter

user_router = APIRouter(prefix="/users")

@user_router.get('/')
def get_users():
    pass

@user_router.post('/')
def create_users():
    pass

@user_router.put('/')
def update_users():
    pass