from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


# --- Book ---
class BookCreate(BaseModel):
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    isbn: str = Field(..., min_length=10)
    year: Optional[int] = None


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    isbn: str
    year: Optional[int]
    available: bool

    class Config:
        from_attributes = True


# --- Member ---
class MemberCreate(BaseModel):
    name: str = Field(..., min_length=1)
    email: str
    phone: Optional[str] = None


class MemberResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str]

    class Config:
        from_attributes = True


# --- Loan ---
class LoanCreate(BaseModel):
    book_id: int
    member_id: int


class LoanResponse(BaseModel):
    id: int
    book_id: int
    member_id: int
    loan_date: datetime
    return_date: Optional[datetime]
    returned: bool

    class Config:
        from_attributes = True
