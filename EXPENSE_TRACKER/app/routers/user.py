from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.core.security import hash_password
from app.models.user import User
from app.schemas.user import UserRequest, UserResponse
from app.schemas.api_response import ApiResponse


user_router = APIRouter(
    prefix ="/users"
)

@user_router.post('/', response_model= ApiResponse, status_code = status.HTTP_201_CREATED)
def create_user(user_request : UserRequest, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(
        (User.username == user_request.username) | (User.email == user_request.email)
    ).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username or email already exists"
        )

    new_user = User(
        username = user_request.username,
        email = user_request.email,
        password = hash_password(user_request.password)
    )

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username or email already exists"
        )
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
        data = {"user":[UserResponse.model_validate(User) for User in users]}
    )

@user_router.get("/search", response_model=ApiResponse)
def search_users(username: str, db:Session = Depends(get_db)):
    users = db.query(User).filter(User.username.ilike(f"%{username}%")).all()
    return ApiResponse(
        status = "success",
        message = "Users retrieved successfully",
        data = {"user":[UserResponse.model_validate(User) for User in users]}
    )

@user_router.get("/{user_id}", response_model=ApiResponse)
def get_user_by_id(user_id:int, db:Session=Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return ApiResponse(
        status ="success",
        message ="Expense retrieved successfully",
        data = {"user":UserResponse.model_validate(user)}
    )

@user_router.put("/{user_id}", response_model=ApiResponse)
def update_user(user_id : int , user_request_dto : UserRequest, db: Session= Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    existing_user = db.query(User).filter(
        (User.username == user_request_dto.username) |
        (User.email == user_request_dto.email),
        User.id != user_id
    ).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username or email already exists"
        )

    user.username = user_request_dto.username
    user.email = user_request_dto.email
    user.password = hash_password(user_request_dto.password)

    try:
        db.commit()
        db.refresh(user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username or email already exists"
        )

    return ApiResponse(
        status = "success",
        message ="Expense updated successfully",
        data = {"user":UserResponse.model_validate(user)}
    )
    

@user_router.delete("/{user_id}", response_model=ApiResponse)
def delete_user(user_id:int, db:Session=Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    db.delete(user)
    db.commit()

    return ApiResponse(
        status="success",
        message="user deleted successfully"
    )
