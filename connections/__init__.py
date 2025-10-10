from sqlalchemy import text
from sqlalchemy.orm import Session

from connections.sql_database import generate_engine
from schemas.data.Enumerators import DatabaseSchemaEnum

DATABASE_ENGINE = generate_engine()


def generate_session():
    with Session(
            autoflush=False,
            autocommit=False,
            bind=DATABASE_ENGINE,
    ) as session:
        yield session


def generate_database_schemas():
    DATABASE_SCHEMAS = [schema.value for schema in DatabaseSchemaEnum]

    with DATABASE_ENGINE.connect() as connection:
        for schema in DATABASE_SCHEMAS:
            connection.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema};"))

        connection.commit()
