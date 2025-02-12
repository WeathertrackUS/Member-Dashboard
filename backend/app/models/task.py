class Task:
    def __init__(self, title, description, status='Pending', due_date=None, assigned_to=None):
        self.title = title
        self.description = description
        self.status = status
        self.due_date = due_date
        self.assigned_to = assigned_to

    def update_status(self, new_status):
        self.status = new_status

    def assign_to(self, user):
        self.assigned_to = user

    def __repr__(self):
        return f"<Task(title={self.title}, status={self.status}, due_date={self.due_date})>"