from sqlalchemy.orm import Session
from src.database.models.users import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def _hash_password(password: str) -> str:
    return pwd_context.hash(password)


def _verify_password(password: str, hashed_pwd: str) -> bool:
    return pwd_context.verify(password, hashed_pwd)


class AuthService:
    def __init__(self, db: Session) -> None:
        self._db: Session = db

    def get_user(self, email: str) -> User | None:
        return self._db.query(User).filter(User.email == email).first()

    async def login_user(self):
        pass
