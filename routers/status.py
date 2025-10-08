from fastapi import APIRouter

router = APIRouter(tags=["Status"])


@router.get("/")
def ping():
    return {"hello": "brave new world"}
