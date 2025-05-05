from sqlalchemy.orm import Session
from app.database.models.user import User
from app.database.dtos.user import UserCreateDTO
from app.utils.security import hash_password

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_users(self):
        return self.db.query(User).all()

    def create_user(self, user_dto: UserCreateDTO):
        user = User(
            name=user_dto.name,
            email=user_dto.email,
            password=hash_password(user_dto.password),
            role=user_dto.role
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
