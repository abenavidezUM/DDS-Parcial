import pytest
import sys
import os
from httpx import AsyncClient

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
from app.main import app



@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Magneto's Mutant Detector!"}

@pytest.mark.asyncio
async def test_mutant_detected():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/mutant/", json={"dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]})
    assert response.status_code == 200
    assert response.json() == {"message": "Mutant detected"}

@pytest.mark.asyncio
async def test_not_mutant():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/mutant/", json={"dna": ["ATGCGA", "CAGTGC", "TTATTT", "AGACGG", "GCGTCA", "TCACTG"]})
    assert response.status_code == 403
    assert response.json() == {"detail": "Not a mutant"}

@pytest.mark.asyncio
async def test_stats():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/stats")
    assert response.status_code == 200
    assert "count_mutant_dna" in response.json()
    assert "count_human_dna" in response.json()
    assert "ratio" in response.json()
