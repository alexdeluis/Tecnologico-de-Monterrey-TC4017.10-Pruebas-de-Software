import json
import os

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

    def save_to_file(self):
        file_path = "data/hotels.json"

        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                json.dump([], file)

        with open(file_path, "r") as file:
            try:
                hotels = json.load(file)
            except json.JSONDecodeError:
                print("Invalid JSON format. Resetting file.")
                hotels = []

        hotels.append({
            "hotel_id": self.hotel_id,
            "name": self.name,
            "location": self.location,
            "total_rooms": self.total_rooms,
            "available_rooms": self.available_rooms
        })

        with open(file_path, "w") as file:
            json.dump(hotels, file, indent=4)

    @classmethod
    def load_from_file(cls):
        file_path = "data/hotels.json"

        if not os.path.exists(file_path):
            return []

        try:
            with open(file_path, "r") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print("Invalid JSON format. Returning empty list.")
            return []

        hotels = []
        for item in data:
            try:
                hotel = cls(
                    hotel_id=item["hotel_id"],
                    name=item["name"],
                    location=item["location"],
                    total_rooms=item["total_rooms"]
                )
                hotel.available_rooms = item.get(
                    "available_rooms",
                    hotel.total_rooms
                )
                hotels.append(hotel)
            except (KeyError, ValueError):
                print("Invalid hotel record found. Skipping.")
                continue

        return hotels