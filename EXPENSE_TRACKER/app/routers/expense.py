from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.models.expense import Expense
from app.schemas.expense import ExpenseRequestDto, ExpenseResponseDto
from app.schemas.api_response import ApiResponse


expense_router = APIRouter(
    prefix= "/expenses",
)


@expense_router.post("/", response_model = ApiResponse)
def create_expense(expense_request_dto: ExpenseRequestDto, db: Session=Depends(get_db)):
    new_expense = Expense(
        title = expense_request_dto.title,
        description = expense_request_dto.description,
        amount = expense_request_dto.amount,
        show = expense_request_dto.show
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    print("new expense is created")
    return ApiResponse(
        status = "success",
        message ="Expense created successfully",
        data={"expense": ExpenseResponseDto.model_validate(new_expense).model_dump(mode="json")}
    )





#get all expenses

#create expenses

#update expenses

#delete expenses