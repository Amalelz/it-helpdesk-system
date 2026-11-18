import enum

from sqlalchemy import Enum as SAEnum


class Role(str, enum.Enum):
    employee = "employee"
    agent = "agent"
    admin = "admin"


class Priority(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"


class Status(str, enum.Enum):
    open = "open"
    in_progress = "in_progress"
    resolved = "resolved"
    closed = "closed"


class HistoryAction(str, enum.Enum):
    created = "created"
    status_changed = "status_changed"
    assigned = "assigned"
    reopened = "reopened"


def db_enum(enum_cls):
    """Store the lowercase values in MySQL, matching schema.sql."""
    return SAEnum(enum_cls, values_callable=lambda e: [m.value for m in e])