from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    print("Hello from the root endpoint")
    return {
        "message" :"Hello from root endpoint!",
        "success" : True,
        "status" : "OK"
    }

@app.get('/users')
def get_users():
    print("getting all users")
    return ["user 1", "user 2", "user 3"]