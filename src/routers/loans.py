from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, UTC
from src.database import get_db
from src import models, schemas

router = APIRouter(prefix="/loans", tags=["loans"])


@router.post("/", response_model=schemas.LoanResponse, status_code=201)
def create_loan(loan: schemas.LoanCreate, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == loan.book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    if not book.available:
        raise HTTPException(status_code=400, detail="Livro já emprestado")

    member = db.query(models.Member).filter(models.Member.id == loan.member_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Membro não encontrado")

    db_loan = models.Loan(book_id=loan.book_id, member_id=loan.member_id)
    book.available = False
    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)
    return db_loan


@router.post("/{loan_id}/return", response_model=schemas.LoanResponse)
def return_loan(loan_id: int, db: Session = Depends(get_db)):
    loan = db.query(models.Loan).filter(models.Loan.id == loan_id).first()
    if not loan:
        raise HTTPException(status_code=404, detail="Empréstimo não encontrado")
    if loan.returned:
        raise HTTPException(status_code=400, detail="Livro já devolvido")

    loan.returned = True
    loan.return_date = datetime.now(UTC)
    loan.book.available = True
    db.commit()
    db.refresh(loan)
    return loan


@router.get("/", response_model=list[schemas.LoanResponse])
def list_loans(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Loan).offset(skip).limit(limit).all()


@router.get("/{loan_id}", response_model=schemas.LoanResponse)
def get_loan(loan_id: int, db: Session = Depends(get_db)):
    loan = db.query(models.Loan).filter(models.Loan.id == loan_id).first()
    if not loan:
        raise HTTPException(status_code=404, detail="Empréstimo não encontrado")
    return loan