#!/usr/bin/env python3
"""
Module: test_place

Unit test for the Place class.
"""
from unittest import TestCase
from models.place import Place


class TestPlace(TestCase):
    """Test Place class"""

    def test_attributes(self):
        """Test it class attributes"""
        place = Place()
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
        self.assertEqual(place.user_id, '')
        self.assertEqual(place.city_id, '')
        self.assertEqual(place.description, "My house")
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 2)
        self.assertEqual(place.price_by_night, 50)
        self.assertEqual(place.latitude, 10.5)
        self.assertEqual(place.longitude, 20.5)
        self.assertEqual(place.amenity_ids, [])
