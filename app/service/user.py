from sqlalchemy.orm import Session
from app.database.dtos.user import UserCreateDTO
from app.repository.user import UserRepository

class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def get_users(self):
        return self.repo.get_all_users()

    def create_user(self, user_dto: UserCreateDTO):
        return self.repo.create_user(user_dto)
