from datetime import datetime

from pydantic import BaseModel, Field


class UserRequest(BaseModel):
    username : str = Field(..., description="The unique username", min_length=1, max_length=50)
    email : str = Field(..., description="email of the user")
    password : str = Field(..., min_length=8, description="Password for the username")

class UserResponse(BaseModel):
    id: int = Field(..., description="The ID of the user")
    username : str = Field(..., description="The unique username", min_length=1, max_length=50)
    email : str = Field(..., description="email of the user")
    created_at : datetime = Field(..., description="The creation date of the user account")

    model_config={
        "from_attributes" : True
    }