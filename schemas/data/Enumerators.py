from enum import Enum


class DatabaseSchemaEnum(Enum):
    marketplace = "marketplace"
    easter_eggs = "easter_eggs"


class SharedStatusEnum(Enum):
    active = "active"
    inactive = "inactive"


class UserStatusEnum(SharedStatusEnum):
    banned = "banned"
    deleted = "deleted"


class SubscriptionStatusEnum(SharedStatusEnum):
    trial = "trial"
    canceled = "canceled"
