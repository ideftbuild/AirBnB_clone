#!/usr/bin/env python3
"""
Module: test_place

Unit test for the Place class.
"""
import unittest
from models.place import Place
from models.city import City
from models.user import User


class TestPlace(unittest.TestCase):
    """Test Place class"""

    def test_init_of_attributes(self):
        """Test it class attributes"""
        # Dependency for user_id
        user = User()
        # Dependency for city_id
        city = City()
        place = Place()
        place.user_id = user.id
        place.city_id = city.id
        place.description = "My house"
        place.number_rooms = 3
        place.number_bathrooms = 1
        place.max_guest = 2
        place.price_by_night = 50
        place.latitude = 10.5
        place.longitude = 20.5
        place.amenity_ids = []

        self.assertIsInstance(place, Place)
        self.assertTrue(hasattr(place, "created_at"))
        self.assertEqual(place.user_id, user.id)
        self.assertEqual(place.city_id, city.id)
        self.assertEqual(place.description, "My house")
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 2)
        self.assertEqual(place.price_by_night, 50)
        self.assertEqual(place.latitude, 10.5)
        self.assertEqual(place.longitude, 20.5)
        self.assertEqual(place.amenity_ids, [])