from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from dependencies.databases import SessionDependency
from models.easter_eggs.shares import get_all

shares_router = APIRouter(tags=["Easter Eggs"], prefix="/easter")


@shares_router.get("/shares")
def get(session: Session = SessionDependency):
    results = get_all(session=session)

    return results
