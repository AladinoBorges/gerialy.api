from fastapi import APIRouter

status_router = APIRouter(tags=["Status"])


@status_router.get("/")
def ping():
    return {"hello": "brave new world"}
