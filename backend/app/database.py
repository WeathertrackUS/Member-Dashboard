import sqlite3
from contextlib import contextmanager
import logging

logger = logging.getLogger(__name__)


def get_db(db_path='wtus_team_system.db'):
    """Get a connection to the SQLite database.

    Returns:
        conn: A connection to the SQLite database.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


@contextmanager
def db_connection():
    """Create a database connection and commit or rollback changes.

    Raises:
        e: Any exception that occurs during the database transaction.

    Yields:
        conn: A connection to the SQLite database.
    """
    conn = get_db()
    try:
        yield conn
        conn.commit()
    except Exception as e:
        logger.error("Database error: %s", str(e))
        conn.rollback()
        raise e
    finally:
        conn.close()
