from os import getenv

from sqlalchemy import URL, Engine, create_engine


def generate_engine() -> Engine:
    URL_OBJECT = URL.create(
        drivername=getenv("DATABASE_DRIVER"),
        username=getenv("DATABASE_USERNAME"),
        password=getenv("DATABASE_PASSWORD"),
        host=getenv("DATABASE_HOST"),
        port=getenv("DATABASE_PORT"),
        database=getenv("DATABASE_NAME"),
    )

    return create_engine(
        url=URL_OBJECT,
        echo=True,
        pool_pre_ping=True,
        pool_recycle=3600
    )
