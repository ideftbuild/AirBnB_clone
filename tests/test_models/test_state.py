#!/usr/bin/env python3
"""
Module: test_state

Unit test for the State class.
"""
from unittest import TestCase
from models.state import State


class TestState(TestCase):
    """Test State class"""

    def test_init_of_attributes(self):
        """Test it class attributes"""

        state = State()
        state.name = "Montana"
        self.assertIsInstance(state, State)
        self.assertTrue(hasattr(state, "id"))
        self.assertEqual(state.name, "Montana")
        self.assertEqual(state.__class__.__name__, "State")
