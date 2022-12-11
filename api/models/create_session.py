import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

DATABASE = "postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}".format(
    **{
        "DB_USER": os.environ["POSTGRES_USER"],
        "DB_PASS": os.environ["POSTGRES_PASSWORD"],
        "DB_HOST": os.environ["DB_HOST"],
        "DB_PORT": os.environ["DB_PORT"],
        "DB_NAME": os.environ["POSTGRES_DB"],
    }
)

ENGINE = create_engine(DATABASE, echo=True)


def session() -> Session:
    return Session(autocommit=False, autoflush=True, bind=ENGINE)
