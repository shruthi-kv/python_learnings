from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.models.user import User
from app.schemas.user import UserRequest, UserResponse
from app.schemas.api_response import ApiResponse


user_router = APIRouter(
    prefix ="/users"
)

@user_router.post('/', response_model= ApiResponse, status_code = status.HTTP_201_CREATED)
def create_user(user_request : UserRequest, db: Session = Depends(get_db)):
    new_user = User(
        username = user_request.username,
        email = user_request.email,
        password = user_request.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    print("new user is created")
    return ApiResponse(
        status ="success",
        message ="User created successfully",
        data = {
            "user" : UserResponse.model_validate(new_user).model_dump(mode="json")
        }
    )

@user_router.get("/", response_model=ApiResponse)
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()

    return ApiResponse(
        status ="success",
        message="Users retrieved successfully",
        data = {"expenses":[UserResponse.model_validate(User) for User in users]}
    )

@user_router.get("/search", response_model=ApiResponse)
def search_users(username: str, db:Session = Depends(get_db)):
    users = db.query(User).filter(User.username.ilike(f"%{username}%")).all()
    return ApiResponse(
        status = "success",
        message = "Users retrieved successfully",
        data = {"expenses":[UserResponse.model_validate(User) for User in users]}
    )

@user_router.get("/{user_id}", response_model=ApiResponse)
def get_user_by_id(user_id:int, db:Session=Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, default="User not found")
    return ApiResponse(
        status ="success",
        message ="Expense retrieved successfully",
        data = {"expenses":UserResponse.model_validate(user)}
    )

@user_router.put("/{user_id}", response_model=ApiResponse)
def update_user(user_id : int , user_request_dto : UserRequest, db: Session= Depends(get_db)):
    
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, default="User not found")

    user.username = user_request_dto.username
    user.email = user_request_dto.email
    user.password = user_request_dto.password

    db.commit()
    db.refresh(user)

    return ApiResponse(
        status = "success",
        message ="Expense updated successfully",
        data = {"expenses":UserResponse.model_validate(user)}
    )
    

@user_router.delete("/{user_id}", response_model=ApiResponse)
def delete_user(user_id:int, db:Session=Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, default="User not found")

    db.delete(user)
    db.commit()

    return ApiResponse(
        status="success",
        message="user deleted successfully"
    )
