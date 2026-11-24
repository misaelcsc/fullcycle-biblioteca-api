from fastapi import FastAPI
from src.database import engine, Base
from src.routers import books, members, loans
from src.config import settings

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name)

app.include_router(books.router)
app.include_router(members.router)
app.include_router(loans.router)


@app.get("/")
def root():
    return {"message": "Biblioteca API está rodando"}
