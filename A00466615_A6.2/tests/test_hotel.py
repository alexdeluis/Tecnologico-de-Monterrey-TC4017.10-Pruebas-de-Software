import unittest
from models.hotel import Hotel

import json
import os

class TestHotel(unittest.TestCase):

    def test_create_valid_hotel(self):
        hotel = Hotel(
            hotel_id="H001",
            name="Grand Hotel",
            location="Mexico City",
            total_rooms=100
        )

        self.assertEqual(hotel.hotel_id, "H001")
        self.assertEqual(hotel.name, "Grand Hotel")
        self.assertEqual(hotel.location, "Mexico City")
        self.assertEqual(hotel.total_rooms, 100)
        self.assertEqual(hotel.available_rooms, 100)

    def test_create_hotel_with_zero_rooms_should_fail(self):
        with self.assertRaises(ValueError):
            Hotel(
                hotel_id="H002",
                name="Invalid Hotel",
                location="Nowhere",
                total_rooms=0
        )
            
    def test_create_hotel_with_empty_id_should_fail(self):
        with self.assertRaises(ValueError):
            Hotel(
                hotel_id="",
                name="Grand Hotel",
                location="Mexico City",
                total_rooms=100
            )

    def test_create_hotel_with_empty_name_should_fail(self):
        with self.assertRaises(ValueError):
            Hotel(
                hotel_id="H003",
                name="",
                location="Mexico City",
                total_rooms=100
            )

    def test_create_hotel_with_empty_location_should_fail(self):
        with self.assertRaises(ValueError):
            Hotel(
                hotel_id="H004",
                name="Grand Hotel",
                location="",
                total_rooms=100
            )

    def test_create_hotel_with_non_integer_rooms_should_fail(self):
        with self.assertRaises(ValueError):
            Hotel(
                hotel_id="H005",
                name="Grand Hotel",
                location="Mexico City",
                total_rooms="100"
            )

    def test_create_hotel_with_negative_rooms_should_fail(self):
        with self.assertRaises(ValueError):
            Hotel(
                hotel_id="H006",
                name="Grand Hotel",
                location="Mexico City",
                total_rooms=-10
            )

    def test_reserve_room_should_reduce_available_rooms(self):
        hotel = Hotel(
            hotel_id="H010",
            name="Grand Hotel",
            location="Mexico City",
            total_rooms=5
        )

        hotel.reserve_room()
        self.assertEqual(hotel.available_rooms, 4)

    def test_reserve_room_when_no_rooms_available_should_fail(self):
        hotel = Hotel(
            hotel_id="H011",
            name="Grand Hotel",
            location="Mexico City",
            total_rooms=1
        )

        hotel.reserve_room()

        with self.assertRaises(ValueError):
            hotel.reserve_room()

    def test_cancel_reservation_should_increase_available_rooms(self):
        hotel = Hotel(
            hotel_id="H020",
            name="Grand Hotel",
            location="Mexico City",
            total_rooms=5
        )

        hotel.reserve_room()
        hotel.cancel_reservation()

        self.assertEqual(hotel.available_rooms, 5)

    def test_cancel_reservation_when_all_rooms_available_should_fail(self):
        hotel = Hotel(
            hotel_id="H021",
            name="Grand Hotel",
            location="Mexico City",
            total_rooms=3
        )

        with self.assertRaises(ValueError):
            hotel.cancel_reservation()

    def test_save_hotel_to_file(self):
        hotel = Hotel(
            hotel_id="H100",
            name="Save Test Hotel",
            location="Monterrey",
            total_rooms=10
        )

        hotel.save_to_file()

        with open("data/hotels.json", "r") as file:
            data = json.load(file)

        self.assertTrue(any(h["hotel_id"] == "H100" for h in data))

    def test_load_hotels_from_file(self):
        hotel = Hotel(
            hotel_id="H200",
            name="Load Test Hotel",
            location="Guadalajara",
            total_rooms=8
        )

        hotel.save_to_file()

        hotels = Hotel.load_from_file()

        self.assertTrue(any(h.hotel_id == "H200" for h in hotels))

if __name__ == "__main__":
    unittest.main()