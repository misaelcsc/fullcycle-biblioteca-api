from fastapi import FastAPI
from src.database import engine, Base
from src.routers import books
from src.config import settings

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME)

app.include_router(books.router)


@app.get("/")
def root():
    return {"message": "Biblioteca API está rodando"}
