import enum
from datetime import datetime
from sqlalchemy import Column, Integer, String, Double, DateTime, func, ForeignKey, Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column

from ..database import Base


class ExpenseType(enum.Enum):
    PERSONAL = "personal"
    GROUP = "group"
    SETTLEMENT = "settlement"
    INCOME = "income"


class Expense(Base):
    __tablename__: str = "expense"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    expense_name: Mapped[str] = mapped_column(String(50), nullable=False)
    amount: Mapped[float] = mapped_column(Double, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    group_id: Mapped[int] = mapped_column(Integer, ForeignKey("groups.id"))
    group = relationship("Groups", back_populates="expenses")

    created_by = Column(String, ForeignKey("users.id"))
    creator = relationship("User", back_populates="expenses")

    expense_type: Mapped[Enum] = mapped_column(
        Enum(ExpenseType), nullable=False, default=ExpenseType.GROUP
    )
