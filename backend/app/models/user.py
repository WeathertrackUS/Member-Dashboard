import sqlite3
import re
from backend.app.database import db_connection


class User:
    def __init__(self, user_id, username, email, specialties):
        """Initialize a new User object.

        Args:
            user_id (int): The user_id of the user.
            username (string): The username of the user.
            email (string): The email of the user.
            specialties (string/list): The specialties of the user.

        Raises:
            ValueError: Username is required and must be a non-empty string
        """
        if not username or not isinstance(username, str) or username.strip() == '':
            raise ValueError("Username is required and must be a non-empty string")
        # Validate and assign email in one step, removing duplicate assignment
        self.email = self._validate_email(email)
        self.user_id = user_id
        self.username = username
        if not isinstance(specialties, (list, str)):
            raise TypeError("Specialties must be a list or string")
        if isinstance(specialties, list):
            if any(not isinstance(s, str) or not s.strip() for s in specialties):
                raise ValueError("All specialties must be non-empty strings")
        else:  # string case
            if not specialties.strip():
                raise ValueError("Specialty string cannot be empty")
        self.specialties = specialties

    @staticmethod
    def create(username, email, specialties):
        """Create a new user in the database.

        Args:
            username (string): The username of the new user.
            email (string): The email of the new user.
            specialties (string/list): The specialties of the new user.

        Raises:
            ValueError: Username or email already exists

        Returns:
            _type_: A User object representing the new user.
        """
        with db_connection() as db:
            cursor = db.cursor()
            # Check if username or email already exists
            cursor.execute('SELECT 1 FROM users WHERE LOWER(username) = LOWER(?) OR LOWER(email) = LOWER(?)', (username, email))
            if cursor.fetchone():
                raise ValueError("Username or email already exists")

            if not isinstance(specialties, (list, str)):
                raise TypeError("Specialties must be a list or string")
            if isinstance(specialties, list):
                if any(not isinstance(s, str) or not s.strip() for s in specialties):
                    raise ValueError("All specialties must be non-empty strings")
            else:  # string case
                if not specialties.strip():
                    raise ValueError("Specialty string cannot be empty")

            cursor.execute(
                'INSERT INTO users (username, email, specialties) VALUES (?, ?, ?)',
                (username, email, ','.join(specialties))
            )
            user_id = cursor.lastrowid
            return User(user_id, username, email, specialties)

    @staticmethod
    def get_by_id(user_id):
        """Get a user by user_id.

        Args:
            user_id (int): The user_id of the user to retrieve.

        Raises:
            sqlite3.InterfaceError: user_id must be an integer
            ValueError: Invalid user data format

        Returns:
            User: A User object representing the user with the given user_id.
        """
        if not isinstance(user_id, int):
            raise TypeError("user_id must be an integer")
        with db_connection() as db:
            cursor = db.cursor()
            user = cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,)).fetchone()
            if not user:
                raise ValueError(f"No user found with id {user_id}")
            if not user['email'] or not user['email'].strip():
                raise ValueError(f"User {user_id} has invalid email format")
            if not user['username'] or not user['username'].strip():
                raise ValueError(f"User {user_id} has invalid username format")
            specialties = user['specialties'].split(',') if user['specialties'] else []
            return User(
                user['user_id'],
                user['username'],
                user['email'],
                specialties
            )

    @staticmethod
    def _validate_email(email):
        """Validate email format.

        Args:
            email (string): The email to validate.

        Raises:
            ValueError: Email is required and must be a non-empty string
            ValueError: Invalid email format

        Returns:
            email: The validated email.
        """
        if not email or not isinstance(email, str) or email.strip() == '':
            raise ValueError("Email is required and must be a non-empty string")
        # More strict email regex that prevents consecutive dots and other invalid patterns
        pattern = r'^[a-zA-Z0-9]+[a-zA-Z0-9._%+-]*@[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9](\.[a-zA-Z]{2,})+$'
        if not re.match(pattern, email):
            raise ValueError("Invalid email format")
        return email.strip()

    def update_email(self, new_email):
        """Update the user's email.

        Args:
            new_email (string): The new email to assign to the user.

        Raises:
            ValueError: Email already exists
        """
        self._validate_email(new_email)  # Validate new email format
        with db_connection() as db:
            cursor = db.cursor()
            # Check if the new email already exists
            cursor.execute('SELECT 1 FROM users WHERE email = ?', (new_email,))
            if cursor.fetchone():
                raise ValueError("Email already exists")

            cursor.execute(
                'UPDATE users SET email = ? WHERE user_id = ?',
                (new_email, self.user_id)
            )
            self.email = new_email

    def _update_specialties(self):
        """Update the user's specialties in the database.

        Raises:
            sqlite3.OperationalError: Database schema error: specialties column not found
            RuntimeError: User with user_id does not exist
            sqlite3.OperationalError: Specialties contain invalid characters
        """
        invalid_chars = ['\0', '\n']
        for specialty in self.specialties:
            if any(char in specialty for char in invalid_chars):
                raise sqlite3.OperationalError("Specialties contain invalid characters")

        with db_connection() as db:
            cursor = db.cursor()
            try:
                cursor.execute(
                    'UPDATE users SET specialties = ? WHERE user_id = ?',
                    (','.join(self.specialties), self.user_id)
                )
                if cursor.rowcount == 0:
                    cursor.execute('SELECT 1 FROM users WHERE user_id = ?', (self.user_id,))
                    if cursor.fetchone() is None:
                        raise RuntimeError(f"User with user_id {self.user_id} does not exist")
            except sqlite3.OperationalError as e:
                if "no such column" in str(e):
                    raise sqlite3.OperationalError("Database schema error: specialties column not found") from e

    def add_specialty(self, specialty):
        """Add a specialty to the user's specialties.

        Args:
            specialty (string/list): The specialty to add to the user's specialties.

        Raises:
            ValueError: Specialty cannot be empty
        """
        if not isinstance(specialty, str) or not specialty.strip():
            raise ValueError("Specialty cannot be empty")
        if specialty not in self.specialties:
            self.specialties.append(specialty)
            self._update_specialties()

    def remove_specialty(self, specialty):
        """Remove a specialty from the user's specialties.

        Args:
            specialty (string/list): The specialty to remove from the user's specialties.

        Raises:
            ValueError: Specialty cannot be empty
        """
        if not isinstance(specialty, str) or not specialty.strip():
            raise ValueError("Specialty cannot be empty")
        if specialty in self.specialties:
            self.specialties.remove(specialty)
            self._update_specialties()

    def __repr__(self):
        """Return a string representation of the User object.

        Returns:
            User: A string representation of the User object.
        """
        return f"<User {self.user_id}>"
