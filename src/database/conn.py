from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base
from ..entity.user import User

engine = create_engine("sqlite:///cashier.db", echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Factory pattern to get db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine, tables=[User.__table__]) 