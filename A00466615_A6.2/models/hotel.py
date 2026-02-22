class Hotel:
    def __init__(self, hotel_id, name, location, total_rooms):

        if not hotel_id:
            raise ValueError("Hotel ID cannot be empty")

        if not name:
            raise ValueError("Hotel name cannot be empty")

        if not location:
            raise ValueError("Hotel location cannot be empty")

        if not isinstance(total_rooms, int):
            raise ValueError("Total rooms must be an integer")

        if total_rooms <= 0:
            raise ValueError("Total rooms must be greater than zero")

        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.total_rooms = total_rooms
        self.available_rooms = total_rooms