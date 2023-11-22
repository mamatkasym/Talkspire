from sqlalchemy.orm import Session

from src.core.security import verify_password
from src.models.user import User


class UserRepository:

    def get_by_email(self, db: Session, email):
        return db.query(User).filter(User.email == email).first()

    def authenticate(self, db: Session, *, email: str, password: str):
        user = self.get_by_email(db, email)
        if not user:
            return None

        if not verify_password(password, user.password):
            return None

        return user


user_repository = UserRepository()
