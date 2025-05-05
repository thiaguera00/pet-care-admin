from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.dtos.user import UserCreateDTO, UserResponseDTO
from app.service.user import UserService
from app.config.database import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponseDTO)
def create_user(user: UserCreateDTO, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.create_user(user)

@router.get("/", response_model=list[UserResponseDTO])
def list_users(db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_users()
