import unittest
from backend.app.models.user import User
from backend.app.database import get_db
import sqlite3

class TestUser(unittest.TestCase):
    def setUp(self):
        self.db = get_db()
        self.db.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT, email TEXT, specialties TEXT)')
        self.db.commit()

    def tearDown(self):
        self.db.execute('DROP TABLE users')
        self.db.commit()

    def test_create_user(self):
        user = User.create(username='testuser', email='test@example.com', specialties=['python', 'django'])
        self.assertIsNotNone(user.user_id)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.specialties, ['python', 'django'])

    def test_get_user_by_id(self):
        user = User.create(username='testuser', email='test@example.com', specialties=['python', 'django'])
        fetched_user = User.get_by_id(user.user_id)
        self.assertIsNotNone(fetched_user)
        self.assertEqual(fetched_user.user_id, user.user_id)
        self.assertEqual(fetched_user.username, 'testuser')
        self.assertEqual(fetched_user.email, 'test@example.com')
        self.assertEqual(fetched_user.specialties, ['python', 'django'])

    def test_update_email(self):
        user = User.create(username='testuser', email='test@example.com', specialties=['python', 'django'])
        user.update_email('newemail@example.com')
        self.assertEqual(user.email, 'newemail@example.com')
        fetched_user = User.get_by_id(user.user_id)
        self.assertEqual(fetched_user.email, 'newemail@example.com')

    def test_add_specialty(self):
        user = User.create(username='testuser', email='test@example.com', specialties=['python', 'django'])
        user.add_specialty('flask')
        self.assertIn('flask', user.specialties)
        fetched_user = User.get_by_id(user.user_id)
        self.assertIn('flask', fetched_user.specialties)

    def test_remove_specialty(self):
        user = User.create(username='testuser', email='test@example.com', specialties=['python', 'django'])
        user.remove_specialty('django')
        self.assertNotIn('django', user.specialties)
        fetched_user = User.get_by_id(user.user_id)
        self.assertNotIn('django', fetched_user.specialties)

    def test_get_user_by_id_not_found(self):
        user = User.get_by_id(9999)  # Assuming 9999 is a non-existent user_id
        self.assertIsNone(user)

    def test_get_user_by_id_invalid_id(self):
        with self.assertRaises(sqlite3.InterfaceError):
            User.get_by_id('invalid_id')  # Passing a string instead of an integer

    def test_get_user_by_id_none(self):
        with self.assertRaises(sqlite3.InterfaceError):
            User.get_by_id(None)  # Passing None instead of an integer

    def test_get_user_by_id_float(self):
        with self.assertRaises(sqlite3.InterfaceError):
            User.get_by_id(1.5)  # Passing a float instead of an integer

    def test_get_user_by_id_list(self):
        with self.assertRaises(sqlite3.InterfaceError):
            User.get_by_id([1, 2, 3])  # Passing a list instead of an integer

    def test_get_user_by_id_dict(self):
        with self.assertRaises(sqlite3.InterfaceError):
            User.get_by_id({'id': 1})  # Passing a dictionary instead of an integer
            
    def test_init_valid_user(self):
        user = User(1, "testuser", "test@example.com", ["python"])
        self.assertEqual(user.user_id, 1)
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.specialties, ["python"])

    def test_init_empty_username(self):
        with self.assertRaises(ValueError):
            User(1, "", "test@example.com", ["python"])

    def test_init_none_username(self):
        with self.assertRaises(ValueError):
            User(1, None, "test@example.com", ["python"])

    def test_init_whitespace_username(self):
        with self.assertRaises(ValueError):
            User(1, "   ", "test@example.com", ["python"])

    def test_init_invalid_username_type(self):
        with self.assertRaises(ValueError):
            User(1, 123, "test@example.com", ["python"])

    def test_init_empty_email(self):
        with self.assertRaises(ValueError):
            User(1, "testuser", "", ["python"])

    def test_init_none_email(self):
        with self.assertRaises(ValueError):
            User(1, "testuser", None, ["python"])
            
    def test_init_whitespace_email(self):
        with self.assertRaises(ValueError):
            User(1, "testuser", "   ", ["python"])

    def test_init_invalid_email_type(self):
        with self.assertRaises(ValueError):
            User(1, "testuser", 123, ["python"])


if __name__ == '__main__':
    unittest.main()