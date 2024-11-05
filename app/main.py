from fastapi import FastAPI, Response, Depends
from contextlib import asynccontextmanager
from controllers.dna_controller import router as dna_router
from app.database import database
from create_tables import create_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

app.include_router(dna_router)

@app.get("/")
async def root():
    return {"message": "Welcome to Magneto's Mutant Detector!"}

@app.head("/")
async def root_head():
    return Response()
