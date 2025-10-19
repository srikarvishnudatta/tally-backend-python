from sqlalchemy.orm import Mapped, mapped_column, relationship
import uuid
from ..database import Base
from sqlalchemy import String

from .relationships import user_group_association


def generate_uuid() -> str:
    return str(uuid.uuid4())


class User(Base):
    __tablename__: str = "users"

    id: Mapped[str] = mapped_column(String(50), primary_key=True, default=generate_uuid)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(100), nullable=False)

    groups = relationship(
        "Groups", secondary=user_group_association, back_populates="users"
    )
    expenses = relationship("Expense", back_populates="creator")
