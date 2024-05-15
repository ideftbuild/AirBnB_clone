#!/usr/bin/env python3
"""test for the class User..."""

from unittest import TestCase
from models.user import User


class TestUser(TestCase):
    def test_user_attributes(self):
        """Test default attribute value of the User class"""
        # create a User instance with default attribute values
        usr1 = User()

        # check if the default attributes are correct
        self.assertEqual(usr1.email, "")
        self.assertEqual(usr1.password, "")
        self.assertEqual(usr1.first_name, "")
        self.assertEqual(usr1.last_name, "")

    def test_user_initialization(self):
        """Test initialization of User class with provided arguments"""
        # create a User instance with the provided arguments
        usr1 = User(
            email="test@test.com",
            password="123456",
            first_name="marco",
            last_name="polo",
        )

        # checks if its set correctly
        self.assertEqual(usr1.email, "test@test.com")
        self.assertEqual(usr1.password, "123456")
        self.assertEqual(usr1.first_name, "marco")
        self.assertEqual(usr1.last_name, "polo")
