from fastapi import APIRouter

auth_router = APIRouter('/auth')

@auth_router.post('/login')
def login():
    print("authentication starting....")
    return{
        "message" : "Auhenticated successfully"
    }