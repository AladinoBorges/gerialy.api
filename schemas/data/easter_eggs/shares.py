from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Share(BaseModel):
    name: str
    description: str
    price: float


class ShareCreate(Share):
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = None


class ShareRead(Share):
    id: int
    created_at: datetime
    updated_at: datetime


class ShareUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    updated_at: datetime = datetime.now()


class ShareDelete(BaseModel):
    id: int
