from sqlalchemy.orm import Session

from schemas.data.easter_eggs.products import ProductCreate, ProductUpdate
from schemas.tables.easter_eggs import ProductsTable


def get_all(session: Session, skip: int = 0, limit: int = 20):
    QUERY = session.query(ProductsTable)
    RESULTS = QUERY.offset(skip).limit(limit).all()

    return RESULTS


def get_one(session: Session, id: int):
    RESULT = session.query(ProductsTable).filter(
        ProductsTable.id == id
    ).first()

    return RESULT


def create(session: Session, data: ProductCreate):
    SERIALIZED_DATA = ProductsTable(
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


def update(session: Session, id: int, data: ProductUpdate):
    product = get_one(session=session, id=id)

    if product:
        new_data = data.model_dump(exclude_none=True, exclude_unset=True)

        for key, value in new_data.items():
            product[key] = value

        session.commit()
        session.refresh(product)

    return product


def delete(session: Session, id: int):
    deleted_id = session.query(ProductsTable).filter(
        ProductsTable.id == id
    ).delete()

    return deleted_id
