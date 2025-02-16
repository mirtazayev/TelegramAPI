import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, DeclarativeBase

load_dotenv()


class Base(DeclarativeBase):
    pass


engine = create_engine(os.getenv("DATABASE_URL"), echo=True)

Session = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


def init_db():
    try:
        Base.metadata.create_all(engine)
        return {"message": "Database initialized successfully"}
    except SQLAlchemyError as e:
        raise Exception(f"Database initialization failed: {str(e)}")


def get_db():
    db = Session()
    try:
        yield db
    except SQLAlchemyError as e:
        raise e
    finally:
        db.close()
