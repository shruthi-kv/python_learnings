from datetime import datetime

from pydantic import BaseModel, Field


class UserRequest(BaseModel):
    username : str = Field(..., description="The unique username", min_length=1, max_length=50)
    email : str = Field(..., description="email of the user")
    password : str = Field(...,descriptio="password for the username")

class UserResponse(BaseModel):
    username : str = Field(..., description="The unique username", min_length=1, max_length=50)
    email : str = Field(..., description="email of the user")
    password : str = Field(...,descriptio="password for the username")
    created_at : datetime = Field(..., description="The creation date of the user account")

    model_config={
        "from_attributes" : True
    }