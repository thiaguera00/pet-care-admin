from sqlalchemy.orm import Session
from app.database.dtos.pet import PetUpdateDTO, PetCreateDTO
from app.repository.pet import PetRepository

class PetService:
    def __init__(self, db: Session):
        self.repo = PetRepository(db)

    def create_pet(self, dto: PetCreateDTO):
        return self.repo.create_pet(dto)

    def list_pets(self):
        return self.repo.get_all()

    def get_pet(self, pet_id: int):
        return self.repo.get_by_id(pet_id)

    def delete_pet(self, pet_id: int):
        return self.repo.delete(pet_id)

    def update_pet(self, pet_id: int, dto: PetUpdateDTO):
        return self.repo.update(pet_id, dto)
