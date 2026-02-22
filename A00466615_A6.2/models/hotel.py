"""
Hotel module.

This module defines the Hotel class and its related
business logic, including persistence and validation.

Author: Alejandro de Luis
"""

import json
import os


class Hotel:
    """
    Represents a hotel entity with room management
    and JSON file persistence capabilities.
    """
    def __init__(self, hotel_id, name, location, total_rooms):
        """
        Initializes a Hotel instance.

        Validates input parameters and ensures
        business rules are satisfied.

        Raises:
            ValueError: If any parameter is invalid.
        """
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

    def reserve_room(self):
        """
        Reserves one room if available.
        Raises ValueError if no rooms are available.
        """
        if self.available_rooms <= 0:
            raise ValueError("No rooms available to reserve")

        self.available_rooms -= 1

    def cancel_reservation(self):
        """
        Cancels a room reservation.
        Increases available_rooms by one.
        Raises:
        ValueError: If there are no reservations to cancel.
        """
        if self.available_rooms >= self.total_rooms:
            raise ValueError("No reservations to cancel")

        self.available_rooms += 1

    def save_to_file(self):
        """
        Saves the hotel instance to a JSON file.
        If the file does not exist, it creates one.
        Handles corrupted JSON content by resetting
        the file content to an empty list.
        """
        file_path = "data/hotels.json"

        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump([], file)

        with open(file_path, "r", encoding="utf-8") as file:
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

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(hotels, file, indent=4)

    @classmethod
    def load_from_file(cls):
        """
        Loads hotel instances from a JSON file.
        Returns:
        list: A list of Hotel objects.
        Handles:
        - Missing file (returns empty list)
        - Corrupted JSON (returns empty list)
        - Invalid records (skips them)
        """
        file_path = "data/hotels.json"

        if not os.path.exists(file_path):
            return []

        try:
            with open(file_path, "r", encoding="utf-8") as file:
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
