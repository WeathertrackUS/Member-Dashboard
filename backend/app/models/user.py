import sqlite3
from backend.app.database import get_db


class User:
    def __init__(self, user_id, username, email, specialties):
        """Initialize a User object.

        Args:
            user_id (int): The user's ID.
            username (string): The user's username.
            email (string): The user's email address.
            specialties (string/list): The user's specialties.

        Raises:
            ValueError: If username or email is empty or not a string.
        """
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
        """Create a new user.

        Args:
            username (string): The user's username.
            email (string): The user's email address.
            specialties (string/list): The user's specialties.

        Returns:
            User: The newly created user's information.
        """
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            'INSERT INTO users (username, email, specialties) VALUES (?, ?, ?)',
            (username, email, ','.join(specialties))
        )
        db.commit()
        user_id = cursor.lastrowid
        return User(user_id, username, email, specialties)

    @staticmethod
    def get_by_id(user_id):
        """Get a user by their ID.

        Args:
            user_id (int): The user's ID.

        Raises:
            sqlite3.InterfaceError: If user_id is not an integer.

        Returns:
            None: If no user is found with the given ID.
            User: The user information if found.
        """
        if not isinstance(user_id, int):
            raise sqlite3.InterfaceError("user_id must be an integer")
        db = get_db()
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
        """Update the user's email address.

        Args:
            new_email (string): The new email address.
        """
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            'UPDATE users SET email = ? WHERE user_id = ?',
            (new_email, self.user_id)
        )
        db.commit()
        self.email = new_email

    def _update_specialties(self):
        """Helper method to update specialties in database."""
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT 1 FROM users WHERE user_id = ?', (self.user_id,))
        if cursor.fetchone() is None:
            raise RuntimeError(f"User with user_id {self.user_id} does not exist")
        try:
            cursor.execute(
                'UPDATE users SET specialties = ? WHERE user_id = ?',
                (','.join(self.specialties), self.user_id)
            )
            db.commit()
        except sqlite3.Error as e:
            db.rollback()
            raise RuntimeError(f"Failed to update specialties: {str(e)}")

    def add_specialty(self, specialty):
        """Add a specialty to the user's profile.

        Args:
            specialty (string/list): The specialty to add.

        Raises:
            ValueError: If specialty is empty or not a string.
        """
        if not specialty or specialty == '':
            raise ValueError("Specialty cannot be empty")
        if specialty not in self.specialties:
            self.specialties.append(specialty)
            self._update_specialties()

    def remove_specialty(self, specialty):
        """Remove a specialty from the user's profile.

        Args:
            specialty (string/list): The specialty to remove.

        Raises:
            ValueError: If specialty is empty or not a string.
        """
        if not specialty or specialty == '':
            raise ValueError("Specialty cannot be empty")
        if specialty in self.specialties:
            self.specialties.remove(specialty)
            self._update_specialties()

    def __repr__(self):
        """Return a string representation of the User object.

        Returns:
            user_id: The user's ID.
        """
        return f"<User {self.user_id}>"
