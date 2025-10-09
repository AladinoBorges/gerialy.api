from contextlib import asynccontextmanager

from fastapi import FastAPI

from connections import DATABASE_ENGINE, generate_database_schemas
from routers import status
from schemas.tables import BaseTable, easter_eggs


@asynccontextmanager
async def lifespan(app: FastAPI):
    generate_database_schemas()
    BaseTable.metadata.create_all(bind=DATABASE_ENGINE)

    yield

    DATABASE_ENGINE.dispose()


main_app = FastAPI(lifespan=lifespan)
main_app.include_router(status.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(main_app, host="0.0.0.0", port=8000)
