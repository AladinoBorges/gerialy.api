from sqlalchemy import Column, DateTime, Float, Integer, String

from schemas.tables import BaseTable


class ProductsTable(BaseTable):
    __tablename__ = "products"
    __table_args__ = {"schema": "easter_eggs"}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)
