from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src import models, schemas

router = APIRouter(prefix="/members", tags=["members"])


@router.post("/", response_model=schemas.MemberResponse, status_code=201)
def create_member(member: schemas.MemberCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Member).filter(models.Member.email == member.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")
    db_member = models.Member(**member.model_dump())
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member


@router.get("/", response_model=list[schemas.MemberResponse])
def list_members(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Member).offset(skip).limit(limit).all()


@router.get("/{member_id}", response_model=schemas.MemberResponse)
def get_member(member_id: int, db: Session = Depends(get_db)):
    member = db.query(models.Member).filter(models.Member.id == member_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Membro não encontrado")
    return members