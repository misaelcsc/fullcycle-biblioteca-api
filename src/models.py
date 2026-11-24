from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, UTC
from src.database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    author = Column(String, nullable=False)
    isbn = Column(String, unique=True, index=True, nullable=False)
    year = Column(Integer, nullable=True)
    available = Column(Boolean, default=True)

    loans = relationship("Loan", back_populates="book")


class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=True)

    loans = relationship("Loan", back_populates="member")


class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    member_id = Column(Integer, ForeignKey("members.id"), nullable=False)
    loan_date = Column(DateTime, default=lambda: datetime.now(UTC))

    return_date = Column(DateTime, nullable=True)
    returned = Column(Boolean, default=False)

    book = relationship("Book", back_populates="loans")
    member = relationship("Member", back_populates="loans")
