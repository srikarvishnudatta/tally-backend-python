from sqlalchemy.orm import Session
from src.database.models.users import User
from passlib.context import CryptContext
from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST
from src.dto.UserDto import CreateUser, LoginUser

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

    async def login_user(self, data: LoginUser):
        user = self.get_user(data.email)
        if not user or not _verify_password(data.password, user.password):
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST, detail="Invalid credentials"
            )
        token = "token"
        return token

    async def create_user(self, data: CreateUser):
        user = self.get_user(data.email)
        if user:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST, detail="Email already exists"
            )
        hashed_pwd = _hash_password(data.password)
        new_user = User(
            email=data.email,
            first_name=data.firstName,
            last_name=data.lastName,
            password=hashed_pwd,
        )
        self._db.add(new_user)
        self._db.commit()
        self._db.refresh(new_user)
        return new_user
