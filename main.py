from contextlib import asynccontextmanager

from fastapi import FastAPI

from connections import DATABASE_ENGINE
from routers import status


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

    DATABASE_ENGINE.dispose()


main_app = FastAPI(lifespan=lifespan)
main_app.include_router(status.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(main_app, host="0.0.0.0", port=8000)
