from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.service.clinic import ClinicService
from app.config.database import get_db
from app.database.dtos.clinic import ClinicCreateDTO, ClinicResponseDTO, ClinicUpdateDTO
from typing import List

router = APIRouter(prefix="/clinics", tags=["Clinics"])

@router.post("/", response_model=ClinicResponseDTO)
def create_clinic(dto: ClinicCreateDTO, db: Session = Depends(get_db)):
    service = ClinicService(db)
    return service.create_clinic(dto)

@router.get("/", response_model=List[ClinicResponseDTO])
def list_clinics(db: Session = Depends(get_db)):
    service = ClinicService(db)
    return service.get_clinics()

@router.get("/{clinic_id}", response_model=ClinicResponseDTO)
def get_clinic(clinic_id: int, db: Session = Depends(get_db)):
    service = ClinicService(db)
    clinic = service.get_clinic(clinic_id)
    if not clinic:
        raise HTTPException(status_code=404, detail="Clinic not found")
    return clinic

@router.put("/{clinic_id}", response_model=ClinicResponseDTO)
def update_clinic(clinic_id: int, dto: ClinicUpdateDTO, db: Session = Depends(get_db)):
    service = ClinicService(db)
    clinic = service.update_clinic(clinic_id, dto)
    if not clinic:
        raise HTTPException(status_code=404, detail="Clinic not found")
    return clinic

@router.delete("/{clinic_id}")
def delete_clinic(clinic_id: int, db: Session = Depends(get_db)):
    service = ClinicService(db)
    clinic = service.delete_clinic(clinic_id)
    if not clinic:
        raise HTTPException(status_code=404, detail="Clinic not found")
    return {"message": "Clinic deleted successfully"}
