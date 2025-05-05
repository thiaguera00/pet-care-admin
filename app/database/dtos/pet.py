from pydantic import BaseModel, Field
from typing import Optional

class PetCreateDTO(BaseModel):
    name: str
    species: str
    breed: Optional[str] = None
    age: Optional[int] = None
    clinic_id: Optional[int] = None

class PetResponseDTO(BaseModel):
    id: int
    name: str
    species: str
    breed: Optional[str] = None
    age: Optional[int] = None
    clinic_id: Optional[int] = None

    class Config:
        orm_mode = True

class PetUpdateDTO(BaseModel):
    name: Optional[str] = None
    species: Optional[str] = None
    breed: Optional[str] = None
    age: Optional[int] = None
    clinic_id: Optional[int] = None