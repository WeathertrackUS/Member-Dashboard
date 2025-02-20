import sqlite3
import unittest
import sys
import os

# Add the project root directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.app.database import get_db

class TestDatabase(unittest.TestCase):
    def test_get_db_connection(self):
        conn = get_db()
        self.assertIsInstance(conn, sqlite3.Connection)
        conn.close()

    def test_get_db_row_factory(self):
        conn = get_db()
        self.assertEqual(conn.row_factory, sqlite3.Row)
        conn.close()

if __name__ == '__main__':
    unittest.main()