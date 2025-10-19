from datetime import datetime
from sqlalchemy import Integer, String, DateTime, func
from sqlalchemy.orm import relationship, Mapped, mapped_column

from ..database import Base
from .relationships import user_group_association


class Groups(Base):
    __tablename__: str = "groups"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    group_name: Mapped[str] = mapped_column(String(50), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    modified_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    users = relationship(
        "User", secondary=user_group_association, back_populates="groups"
    )

    expenses = relationship(
        "Expense", back_populates="group", cascade="all, delete-orphan"
    )
