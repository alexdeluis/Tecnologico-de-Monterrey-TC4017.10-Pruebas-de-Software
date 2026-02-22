class Hotel:
    def __init__(self, hotel_id, name, location, total_rooms):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.total_rooms = total_rooms
        self.available_rooms = total_rooms