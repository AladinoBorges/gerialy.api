from sqlalchemy import (JSON, Boolean, Column, DateTime, Float, ForeignKey,
                        Index, Integer, String)
from sqlalchemy.orm import relationship

from schemas.data.Enumerators import DatabaseSchemaEnum
from schemas.tables import BaseTable


class StatusTable(BaseTable):
    __tablename__ = "status"
    __table_args__ = {"schema": DatabaseSchemaEnum.easter_eggs.value}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    users = relationship("UserTable", back_populates="status")
    subscriptions = relationship("SubscriptionTable", back_populates="status")
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=True)


class UserTable(BaseTable):
    __tablename__ = "users"
    __table_args__ = {"schema": DatabaseSchemaEnum.easter_eggs.value}

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    status_id = Column(
        Integer,
        ForeignKey(f"{DatabaseSchemaEnum.easter_eggs.value}.status.id"),
        nullable=False,
        index=True,
    )
    status = relationship("StatusTable", back_populates="users")
    subscriptions = relationship(
        "SubscriptionTable",
        back_populates="user"
    )
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=True)


class ShareTable(BaseTable):
    __tablename__ = "shares"
    __table_args__ = {"schema": DatabaseSchemaEnum.easter_eggs.value}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    is_recurring = Column(Boolean, default=False, nullable=False)
    gateway_id = Column(String, nullable=False, unique=True)
    gateway_provider = Column(String, nullable=False)
    metadata = Column(JSON, nullable=True)
    subscriptions = relationship(
        "SubscriptionTable",
        back_populates="share"
    )
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=True)


class SubscriptionTable(BaseTable):
    __tablename__ = "subscriptions"
    __table_args__ = {"schema": DatabaseSchemaEnum.easter_eggs.value}

    id = Column(Integer, primary_key=True, index=True)
    share_id = Column(Integer, ForeignKey("easter_eggs.shares.id"), index=True)
    share = relationship("ShareTable", back_populates="subscriptions")
    user_id = Column(
        Integer,
        ForeignKey("easter_eggs.users.id"),
        nullable=False,
        index=True
    )
    user = relationship("UserTable", back_populates="subscriptions")
    status_id = Column(
        Integer,
        ForeignKey(f"{DatabaseSchemaEnum.easter_eggs.value}.status.id"),
        nullable=False,
        index=True,
    )
    status = relationship("StatusTable", back_populates="subscriptions")
    price_at_subscription = Column(Float, nullable=False)
    invoice_url = Column(String, nullable=True)
    started_at = Column(DateTime(timezone=True), nullable=False)
    expires_at = Column(DateTime(timezone=True), nullable=False)
    canceled_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=True)
