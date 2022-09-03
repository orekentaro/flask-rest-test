from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

DATABASE = 'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'.format(**{
    'DB_USER': 'postgres',
    'DB_PASS': 'nagato8',
    'DB_HOST': 'recruit-management-db',
    'DB_PORT': '5432',
    'DB_NAME': 'recruit-management'
})

ENGINE = create_engine(
    DATABASE,
    echo=True
)

session = scoped_session(
    sessionmaker(
        autoflush=False,
        bind=ENGINE,
        autocommit=False,
        expire_on_commit=False
    )
)

Base = declarative_base()
