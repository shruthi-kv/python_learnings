from fastapi import FastAPI
from .schemas.api import ApiResponse

app = FastAPI()


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



# @app.get("/", response_model = ApiResponse)
# def home():
#     print("Hello from the root endpoint")
#     response = ApiResponse( message = "Hello from root endpoint", success = True, status ="200")

#     return response

# @app.get('/users')
# def get_users():
#     print("getting all users")
#     return ["user 1", "user 2", "user 3"]