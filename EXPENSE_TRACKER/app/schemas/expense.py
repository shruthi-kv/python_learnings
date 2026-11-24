from datetime import datetime

from pydantic import BaseModel, Field

class ExpenseRequestDto(BaseModel):
    title:str = Field(... , description="The title of the expense", min_length=1, max_length=50)
    amount:float = Field(..., description="The amount of the expense")
    description:str = Field(...,description="The description of the expense")
    show : bool = Field(default=True, description="Whether the expense should be shown")

class ExpenseResponseDto(BaseModel):
    id: int = Field(..., description="The ID of the expense")
    title:str = Field(... , description="The title of the expense")
    amount:float = Field(..., description="The amount of the expense")
    description:str = Field(...,description="The description of the expense")
    show : bool = Field(..., description="Whether the expense should be shown")
    created_at : datetime = Field(..., description="The creation date of the expense")

    #to automatically convert the response to json format, below is the code
    model_config={
        "from_attributes" : True
    }