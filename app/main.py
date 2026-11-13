from fastapi import FastAPI
from app.core.db import Base, engine
from app.api import farms

app = FastAPI(title="BMF Listing Service")
app.include_router(farms.router)

@app.on_event("startup")
def init_db():
    Base.metadata.create_all(bind=engine)   # replaced by Alembic migrations later

@app.get("/healthz")
def healthz():
    return {"status": "ok"}