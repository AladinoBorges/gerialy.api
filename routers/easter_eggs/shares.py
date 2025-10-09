from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from connections import generate_session
from models.easter_eggs.shares import get_all, get_one

shares_router = APIRouter(tags=["Easter Eggs"], prefix="/easter")


@shares_router.get("/shares")
def get(session: Session = Depends(generate_session)):
    SHARES = get_all(session=session)

    return SHARES


@shares_router.get("/shares/{id}")
def get_by_id(id: int, session: Session = Depends(generate_session)):
    SHARE = get_one(id=id, session=session)

    return SHARE
