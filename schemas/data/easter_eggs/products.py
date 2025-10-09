from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Product(BaseModel):
    name: str
    description: str
    price: float


class ProductCreate(Product):
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = None


class ProductRead(Product):
    id: int
    created_at: datetime
    updated_at: datetime


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    updated_at: datetime = datetime.now()


class ProductDelete(BaseModel):
    id: int
