class Hotel:
    def __init__(self, hotel_id, name, location, total_rooms):

        # If hotel_id is "" or None, exception and the object is not created
        if not hotel_id:
            raise ValueError("Hotel ID cannot be empty")

        if not name:
            raise ValueError("Hotel name cannot be empty")

        if not location:
            raise ValueError("Hotel location cannot be empty")

        # We validate type
        if not isinstance(total_rooms, int):
            raise ValueError("Total rooms must be an integer")

        # We validate business logic
        if total_rooms <= 0:
            raise ValueError("Total rooms must be greater than zero")

        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.total_rooms = total_rooms
        self.available_rooms = total_rooms

    def reserve_room(self):
        if self.available_rooms <= 0:
            raise ValueError("No rooms available to reserve")

        self.available_rooms -= 1

    def cancel_reservation(self):
        if self.available_rooms >= self.total_rooms:
            raise ValueError("No reservations to cancel")

        self.available_rooms += 1