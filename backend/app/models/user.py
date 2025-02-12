class User:
    def __init__(self, user_id, username, email, specialties):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.specialties = specialties  # List of specialties

    def update_email(self, new_email):
        self.email = new_email

    def add_specialty(self, specialty):
        if specialty not in self.specialties:
            self.specialties.append(specialty)

    def remove_specialty(self, specialty):
        if specialty in self.specialties:
            self.specialties.remove(specialty)

    def __repr__(self):
        return f"<User {self.username} (ID: {self.user_id})>"