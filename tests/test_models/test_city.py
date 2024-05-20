#!/usr/bin/env python3
"""
Module: test_city

Unit test for the City class.
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test City class"""

    def test_attributes(self):
        self.city = City()
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)
