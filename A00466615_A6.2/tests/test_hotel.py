import unittest
from models.hotel import Hotel


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


if __name__ == "__main__":
    unittest.main()