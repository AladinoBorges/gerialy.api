from fastapi import FastAPI

from routers import status

app = FastAPI()

app.include_router(status.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
