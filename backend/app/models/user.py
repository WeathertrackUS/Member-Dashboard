import sqlite3
from backend.app.database import db_connection

class User:
    def __init__(self, user_id, username, email, specialties):
        if not username or not isinstance(username, str) or username.strip() == '':
            raise ValueError("Username is required and must be a non-empty string")
        if not email or not isinstance(email, str) or email.strip() == '':
            raise ValueError("Email is required and must be a non-empty string")
        self.user_id = user_id
        self.username = username
        self.email = email
        self.specialties = specialties

    @staticmethod
    def create(username, email, specialties):
        with db_connection() as db:
            cursor = db.cursor()
            cursor.execute(
                'INSERT INTO users (username, email, specialties) VALUES (?, ?, ?)',
                (username, email, ','.join(specialties))
            )
            user_id = cursor.lastrowid
            return User(user_id, username, email, specialties)

    @staticmethod
    def get_by_id(user_id):
        if not isinstance(user_id, int):
            raise sqlite3.InterfaceError("user_id must be an integer")
        with db_connection() as db:
            cursor = db.cursor()
            user = cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,)).fetchone()
            if user:
                return User(
                    user['user_id'],
                    user['username'],
                    user['email'],
                    user['specialties'].split(',')
                )
            return None

    def update_email(self, new_email):
        with db_connection() as db:
            cursor = db.cursor()
            cursor.execute(
                'UPDATE users SET email = ? WHERE user_id = ?',
                (new_email, self.user_id)
            )
            self.email = new_email

    def _update_specialties(self):
        with db_connection() as db:
            cursor = db.cursor()
            cursor.execute('SELECT 1 FROM users WHERE user_id = ?', (self.user_id,))
            if cursor.fetchone() is None:
                raise RuntimeError(f"User with user_id {self.user_id} does not exist")
            cursor.execute(
                'UPDATE users SET specialties = ? WHERE user_id = ?',
                (','.join(self.specialties), self.user_id)
            )

    def add_specialty(self, specialty):
        if not specialty or specialty == '':
            raise ValueError("Specialty cannot be empty")
        if specialty not in self.specialties:
            self.specialties.append(specialty)
            self._update_specialties()

    def remove_specialty(self, specialty):
        if not specialty or specialty == '':
            raise ValueError("Specialty cannot be empty")
        if specialty in self.specialties:
            self.specialties.remove(specialty)
            self._update_specialties()

    def __repr__(self):
        return f"<User {self.user_id}>"