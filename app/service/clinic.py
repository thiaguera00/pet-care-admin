from sqlalchemy.orm import Session
from app.repository.clinic import ClinicRepository
from app.database.dtos.clinic import ClinicCreateDTO, ClinicUpdateDTO

class ClinicService:
    def __init__(self, db: Session):
        self.repo = ClinicRepository(db)

    def create_clinic(self, dto: ClinicCreateDTO):
        return self.repo.create_clinic(dto)

    def get_clinics(self):
        return self.repo.get_all_clinics()

    def get_clinic(self, clinic_id: int):
        return self.repo.get_clinic_by_id(clinic_id)

    def update_clinic(self, clinic_id: int, dto: ClinicUpdateDTO):
        return self.repo.update_clinic(clinic_id, dto)

    def delete_clinic(self, clinic_id: int):
        return self.repo.delete_clinic(clinic_id)
