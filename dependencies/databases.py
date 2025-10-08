from typing import Annotated

from fastapi import Depends
from sqlalchemy import Session

from connections import generate_session

SessionDependency = Annotated[Session, Depends(generate_session)]
