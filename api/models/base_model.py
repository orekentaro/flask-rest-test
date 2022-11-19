import os
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, String, create_engine
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import Session, scoped_session

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


class Mixin(object):
    @declared_attr
    def is_delete(cls):
        return Column("is_delete", Boolean, default=False, nullable=False)

    @declared_attr
    def create_time(cls):
        return Column("cleate_time", DateTime, default=datetime.now(), nullable=False)

    @declared_attr
    def update_time(cls):
        return Column(
            "update_time",
            DateTime,
            default=datetime.now(),
            onupdate=datetime.now(),
            nullable=False,
        )

    @declared_attr
    def changer(cls):
        return Column("changer", String(200), nullable=False)


BaseModel = declarative_base(cls=Mixin)
