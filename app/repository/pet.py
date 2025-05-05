from sqlalchemy.orm import Session
from app.database.models.pet import Pet
from app.database.dtos.pet import PetCreateDTO, PetUpdateDTO

class PetRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_pet(self, dto: PetCreateDTO):
        pet = Pet(**dto.dict())
        self.db.add(pet)
        self.db.commit()
        self.db.refresh(pet)
        return pet

    def get_all(self):
        return self.db.query(Pet).all()

    def get_by_id(self, pet_id: int):
        return self.db.query(Pet).filter(Pet.id == pet_id).first()

    def delete(self, pet_id: int):
        pet = self.get_by_id(pet_id)
        if pet:
            self.db.delete(pet)
            self.db.commit()
        return pet

    def update(self, pet_id: int, dto: PetUpdateDTO):
        pet = self.get_by_id(pet_id)
        if pet:
            for key, value in dto.dict(exclude_unset=True).items():
                setattr(pet, key, value)
            self.db.commit()
            self.db.refresh(pet)
        return pet