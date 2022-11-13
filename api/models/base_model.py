from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, String, create_engine
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE = "postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}".format(
    **{
        "DB_USER": "postgres",
        "DB_PASS": "nagato8",
        "DB_HOST": "db",
        "DB_PORT": "5432",
        "DB_NAME": "recruit-management",
    }
)

ENGINE = create_engine(DATABASE, echo=True)

session = scoped_session(
    sessionmaker(autoflush=False, bind=ENGINE, autocommit=False, expire_on_commit=False)
)


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
