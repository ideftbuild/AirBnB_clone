#!/usr/bin/env python3
"""
Module: test_state

Unit test for the State class.
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test State class"""

    def test_attributes(self):
        state = State()
        self.assertIsInstance(state.name, str)
