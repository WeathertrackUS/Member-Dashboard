import sqlite3


def get_db():
    """Get a connection to the SQLite database.

    Returns:
        conn: A connection to the SQLite database.
    """
    conn = sqlite3.connect('wtus_team_system.db')
    conn.row_factory = sqlite3.Row
    return conn
