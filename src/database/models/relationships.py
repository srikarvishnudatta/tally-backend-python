from sqlalchemy import Table, Column, Integer, ForeignKey, String
from ..database import Base

user_group_association = Table(
    "user_groups",
    Base.metadata,
    Column("user_id", String, ForeignKey("users.id"), primary_key=True),
    Column("group_id", Integer, ForeignKey("groups.id"), primary_key=True),
)
