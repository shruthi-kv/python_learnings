from pydantic import BaseModel, Field

class UserDTO(BaseModel):
    firstName : str = Field(..., max_length=100, min_length=2)
    lastName : str
    age : int
    city: str
    isActive : bool = True