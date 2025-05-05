from pydantic import BaseModel
from typing import Optional

class ClinicCreateDTO(BaseModel):
    name: str
    address: str

class ClinicResponseDTO(BaseModel):
    id: int
    name: str
    address: str
    
    class Config:
        orm_mode = True

class ClinicUpdateDTO(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None

