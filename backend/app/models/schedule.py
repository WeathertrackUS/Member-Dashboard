class Schedule:
    def __init__(self, user_id):
        self.user_id = user_id
        self.availability = []  # List to hold available time slots

    def add_availability(self, time_slot):
        """Add a time slot to the user's availability."""
        self.availability.append(time_slot)

    def remove_availability(self, time_slot):
        """Remove a time slot from the user's availability."""
        if time_slot in self.availability:
            self.availability.remove(time_slot)

    def get_availability(self):
        """Return the user's availability."""
        return self.availability

    def clear_availability(self):
        """Clear all availability slots for the user."""
        self.availability.clear()