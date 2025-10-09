from contextlib import asynccontextmanager

from fastapi import FastAPI

from connections import DATABASE_ENGINE, generate_database_schemas
from routers import shares_router, status_router
from schemas.tables import BaseTable, easter_eggs


@asynccontextmanager
async def lifespan(app: FastAPI):
    generate_database_schemas()
    BaseTable.metadata.create_all(bind=DATABASE_ENGINE)

    yield

    DATABASE_ENGINE.dispose()


API = FastAPI(
    lifespan=lifespan,
    docs_url="/documentation",
    version="0.0.1",
    redoc_url=None,
    title="gerialy",
    summary="",
    terms_of_service="http://example.com/terms",
    license_info={
        "name": "GNU GPL v3.0",
        "url": "https://www.gnu.org/licenses/gpl-3.0.html"
    }
)

# PUBLIC ROUTES
API.include_router(status_router)

# EASTER EGGS ROUTES
API.include_router(shares_router)

# TODO: MARKETPLACE ROUTES

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(API, host="0.0.0.0", port=8000)
