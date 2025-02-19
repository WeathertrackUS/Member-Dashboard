import sqlite3
from contextlib import contextmanager


def get_db():
    """Get a connection to the SQLite database.

    Returns:
        conn: A connection to the SQLite database.
    """
    conn = sqlite3.connect('wtus_team_system.db')
    conn.row_factory = sqlite3.Row
    return conn


@contextmanager
def db_connection():
    """Context manager for database connections.

    Yields:
        conn: A connection to the SQLite database.
    """
    conn = get_db()
    try:
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()
