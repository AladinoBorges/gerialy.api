from sqlalchemy.orm import Session

from connections.sql_database import generate_engine

DATABASE_ENGINE = generate_engine()


def generate_session():
    with Session(
            autoflush=False,
            autocommit=False,
            bind=DATABASE_ENGINE,
    ) as session:
        yield session
