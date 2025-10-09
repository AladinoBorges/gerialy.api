from fastapi import HTTPException
from sqlalchemy.orm import Session

from schemas.data.easter_eggs.shares import ShareCreate, ShareUpdate
from schemas.tables.easter_eggs import SharesTable


def get_all(session: Session, skip: int = 0, limit: int = 20):
    QUERY = session.query(SharesTable)
    RESULTS = QUERY.offset(skip).limit(limit).all()

    return RESULTS


def get_one(session: Session, id: int):
    RESULT = session.query(SharesTable).filter(
        SharesTable.id == id
    ).first()

    if not RESULT:
        raise HTTPException(status_code=404, detail='Not found.')

    return RESULT


def create(session: Session, data: ShareCreate):
    SERIALIZED_DATA = SharesTable(
        name=data.name,
        description=data.description,
        price=data.price,
        created_at=data.created_at,
        updated_at=data.updated_at,
    )

    session.add(SERIALIZED_DATA)
    session.commit()
    session.refresh(SERIALIZED_DATA)

    return SERIALIZED_DATA


def update(session: Session, id: int, data: ShareUpdate):
    share = get_one(session=session, id=id)

    if share:
        new_data = data.model_dump(exclude_none=True, exclude_unset=True)

        for key, value in new_data.items():
            share[key] = value

        session.commit()
        session.refresh(share)

    return share


def delete(session: Session, id: int):
    deleted_id = session.query(SharesTable).filter(
        SharesTable.id == id
    ).delete()

    return deleted_id
