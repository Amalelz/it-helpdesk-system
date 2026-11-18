from datetime import datetime

from sqlalchemy import String, func, true
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.models.enums import Role, db_enum


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    role: Mapped[Role] = mapped_column(
        db_enum(Role), default=Role.employee, server_default=Role.employee.value
    )
    is_active: Mapped[bool] = mapped_column(default=True, server_default=true())
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())