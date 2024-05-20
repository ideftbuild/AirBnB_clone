#!/usr/bin/env python3
"""
Module: test_amenity

Unit test for the Amenity class
"""
import unittest
from models.amenity import Amenity


class TestAmentity(unittest.TestCase):
    """Test Amenity class"""

    def test_attributes(self):
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)
