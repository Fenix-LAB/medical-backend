from src.config.session import connect_to_db
from contextlib import contextmanager

SessionLocal = connect_to_db()

@contextmanager
def session_scope() -> SessionLocal:
    """Provide a transactional scope around a series of operations."""
    db = None
    try:
        db = SessionLocal()  # create session from SQLAlchemy sessionmaker
        yield db
    finally:
        db.close()