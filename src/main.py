from fastapi import FastAPI
from src.database import engine, Base
from src.routers import books, members, loans
from src.config import settings

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME)

app.include_router(books.router)
app.include_router(members.router)
app.include_router(loans.router)


@app.get("/")
def root():
    return {"message": "Biblioteca API está rodando"}
