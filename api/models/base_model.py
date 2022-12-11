from datetime import datetime

from create_app import APP
from sqlalchemy import Boolean, Column, DateTime, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import Session

DATABASE = APP.config["SQLALCHEMY_DATABASE_URI"]

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
        return Column("changer", Integer, nullable=False)


BaseModel = declarative_base(cls=Mixin)
