from pydantic import BaseModel, EmailStr

class UserCreateDTO(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str

class UserResponseDTO(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str

    class Config:
        orm_mode = True