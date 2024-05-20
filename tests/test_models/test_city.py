#!/usr/bin/env python3
"""
Module: test_city

Unit test for the City class.
"""
import unittest
from models.city import City
from models.state import State


class TestCity(unittest.TestCase):
    """Test City class"""

    def test_init_of_attributes(self):
        """Test it class attributes"""

        state = State()  # Dependency for state_id
        city = City()
        city.name = "Helena"
        city.state_id = state.id

        self.assertIsInstance(city, City)
        self.assertTrue(hasattr(city, "created_at"))
        self.assertEqual(city.name, "Helena")
        self.assertEqual(city.__class__.__name__, "City")
