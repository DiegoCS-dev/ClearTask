from pydantic import BaseModel, Field
from enum import Enum
from datetime import date, datetime
class Status(Enum):
    pending = "pending"
    completed = "completed"
class Priority(Enum):
    low = "low"
    medium = "medium"
    high = "high"
class UpdateTask(BaseModel):
    title: str | None = None
    description: str | None = None
    status: Status | None = None
    priority: Priority | None = None
    due_date: date | None = None
class Task(BaseModel):
    title: str = Field(..., min_length=3)
    description: str | None = None
    status: Status = Status.pending
    priority: Priority | None = None
    due_date: date | None = None
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: Status
    priority: Priority | None
    due_date: date | None
    created_at: datetime
    updated_at: datetime | None
    user_id: int