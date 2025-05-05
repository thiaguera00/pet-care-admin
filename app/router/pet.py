from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.dtos.pet import PetCreateDTO, PetResponseDTO, PetUpdateDTO
from app.service.pet import PetService
from app.config.database import get_db
from typing import List

router = APIRouter(prefix="/pets", tags=["Pets"])

@router.post("/", response_model=PetResponseDTO)
def create_pet(dto: PetCreateDTO, db: Session = Depends(get_db)):
    service = PetService(db)
    return service.create_pet(dto)

@router.get("/", response_model=List[PetResponseDTO])
def list_pets(db: Session = Depends(get_db)):
    service = PetService(db)
    return service.list_pets()

@router.get("/{pet_id}", response_model=PetResponseDTO)
def get_pet(pet_id: int, db: Session = Depends(get_db)):
    service = PetService(db)
    pet = service.get_pet(pet_id)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet

@router.put("/{pet_id}", response_model=PetResponseDTO)
def update_pet(pet_id: int, dto: PetUpdateDTO, db: Session = Depends(get_db)):
    service = PetService(db)
    pet = service.update_pet(pet_id, dto)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet

@router.delete("/{pet_id}")
def delete_pet(pet_id: int, db: Session = Depends(get_db)):
    service = PetService(db)
    pet = service.delete_pet(pet_id)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    return {"message": "Pet deleted"}