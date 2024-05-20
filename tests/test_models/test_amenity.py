#!/usr/bin/env python3
"""
Module: test_amenity

Unit test for the Amenity class
"""
from unittest import TestCase
from models.amenity import Amenity


class TestAmenity(TestCase):
    """Test The Amenity class"""

    def test_init_of_attributes(self):
        """Test it class attributes"""

        amenity = Amenity()
        amenity.name = "Wifi"

        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertEqual(amenity.name, "Wifi")
        self.assertEqual(amenity.__class__.__name__, "Amenity")
