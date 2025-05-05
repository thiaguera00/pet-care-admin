from sqlalchemy.orm import Session
from app.database.models.clinic import Clinic
from app.database.dtos.clinic import ClinicCreateDTO, ClinicUpdateDTO

class ClinicRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_clinic(self, clinic_dto: ClinicCreateDTO) -> Clinic:
        clinic = Clinic(**clinic_dto.dict())
        self.db.add(clinic)
        self.db.commit()
        self.db.refresh(clinic)
        return clinic

    def get_all_clinics(self):
        return self.db.query(Clinic).all()

    def get_clinic_by_id(self, clinic_id: int):
        return self.db.query(Clinic).filter(Clinic.id == clinic_id).first()

    def update_clinic(self, clinic_id: int, dto: ClinicCreateDTO):
        clinic = self.get_clinic_by_id(clinic_id)
        if clinic:
            for key, value in dto.dict(exclude_unset=True).items():
                setattr(clinic, key, value)
            self.db.commit()
            self.db.refresh(clinic)
        return clinic

    def delete_clinic(self, clinic_id: int):
        clinic = self.get_clinic_by_id(clinic_id)
        if clinic:
            self.db.delete(clinic)
            self.db.commit()
        return clinic
