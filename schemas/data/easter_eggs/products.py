from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ProductEasterEgg(BaseModel):
    name: str
    description: str
    price: float


class ProductCreateEasterEgg(ProductEasterEgg):
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = None


class ProductEasterEggRead(ProductEasterEgg):
    id: int
    created_at: datetime
    updated_at: datetime


class ProductUpdateEasterEgg(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    updated_at: datetime = datetime.now()


class ProductDeleteEasterEgg(BaseModel):
    id: int
