from fastapi import FastAPI
from .schemas.api import ApiResponse

app = FastAPI()

@app.get('/')
def root():
    print("hello from root url")
    return ApiResponse(
        message ="Hello from root URL",
        status = "OK",
        success = True
    )

@app.get("/users")
def get_users():
    print("fetching users")
    return ["Shruthi","Reddy","kv"]

@app.post("/users")
def post_user():
    print("posting user")
    return ApiResponse(
        message = "User added successfully!",
        success = True,
        status = "OK"
    )

@app.put("/users/{user_id}/name/{user_name}")
def update_user(user_id:int,user_name:str):
    print("updating user....")
    print(user_id,user_name,"----are the user_id and user_name")
    return {
        "message" : "Updated the user successfully",
        "user_name" : user_name,
        "user_id" :user_id,
        "status" :"OK",
        "success" : True
    }

@app.get("/users/search")
def searchUser(firstName:str="", lastName:str="", city:str=""):
    print("searching for the user")
    return {
        "message" :"Searched for the user",
        "QueryParams" :[firstName, lastName,city],
        "status" : 200
    }
