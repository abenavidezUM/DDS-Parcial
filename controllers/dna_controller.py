from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.dna_service import is_mutant
from repositories.dna_repository import count_mutants, count_humans

router = APIRouter()

class DNAModel(BaseModel):
    dna: list[str]

@router.post("/mutant/")
async def check_mutant(dna_model: DNAModel):
    dna = dna_model.dna
    
    if not dna or not all(len(row) == len(dna) for row in dna):
        raise HTTPException(status_code=400, detail="Invalid DNA matrix. Must be NxN.")
    
    is_mutant_result = await is_mutant(dna)
    
    if is_mutant_result:
        return {"message": "Mutant detected"}
    
    raise HTTPException(status_code=403, detail="Not a mutant")

@router.get("/stats")
async def get_stats():
    count_mutant_dna = await count_mutants()
    count_human_dna = await count_humans()
    
    ratio = count_mutant_dna / count_human_dna if count_human_dna > 0 else 0

    return {
        "count_mutant_dna": count_mutant_dna,
        "count_human_dna": count_human_dna,
        "ratio": ratio
    }
