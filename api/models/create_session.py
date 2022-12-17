import os

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

# FIXME: 一回一回関数で呼ぶのはイケてないので修正


def get_database() -> str:
    return "postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}".format(
        **{
            "DB_USER": os.environ["POSTGRES_USER"],
            "DB_PASS": os.environ["POSTGRES_PASSWORD"],
            "DB_HOST": os.environ["DB_HOST"],
            "DB_PORT": os.environ["DB_PORT"],
            "DB_NAME": os.environ["POSTGRES_DB"],
        }
    )


def get_engine() -> Engine:
    return create_engine(get_database(), echo=True)


def session() -> Session:
    return Session(autocommit=False, autoflush=True, bind=get_engine())
