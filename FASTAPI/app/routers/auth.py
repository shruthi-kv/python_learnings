from fastapi import APIRouter

auth_router = APIRouter(prefix='/auth')

@auth_router.post('/login')
def login():
    print("authentication starting....")
    return{
        "message" : "Auhenticated successfully"
    }

@auth_router.post("/register")
def register():
    print("registering the user.....")
    return {
        "message" :"registered the user",
        "status" : 200
    }