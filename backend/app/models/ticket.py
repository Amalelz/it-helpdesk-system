from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.enums import Priority, Status, db_enum


class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(150))
    description: Mapped[str] = mapped_column(Text)
    priority: Mapped[Priority] = mapped_column(
        db_enum(Priority),
        default=Priority.medium,
        server_default=Priority.medium.value,
        index=True,
    )
    status: Mapped[Status] = mapped_column(
        db_enum(Status),
        default=Status.open,
        server_default=Status.open.value,
        index=True,
    )
    category_id: Mapped[int | None] = mapped_column(ForeignKey("categories.id"))
    created_by: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    assigned_to: Mapped[int | None] = mapped_column(ForeignKey("users.id"), index=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), index=True)
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )
    resolved_at: Mapped[datetime | None]

    creator: Mapped["User"] = relationship(foreign_keys=[created_by])
    assignee: Mapped[Optional["User"]] = relationship(foreign_keys=[assigned_to])
    category: Mapped[Optional["Category"]] = relationship()
    comments: Mapped[list["Comment"]] = relationship(
        back_populates="ticket", cascade="all, delete-orphan", passive_deletes=True
    )
    history: Mapped[list["TicketHistory"]] = relationship(
        back_populates="ticket", cascade="all, delete-orphan", passive_deletes=True
    )