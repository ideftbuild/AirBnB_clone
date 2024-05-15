#!/bin/usr/env python3
"""A module that contains the tests for the sub classes"""

import unittest
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models.base_model import BaseModel


class Test_SubClasses(unittest.TestCase):
    """Test the sub classes"""

    def test_state(self):
        """Test the  State class"""
        state = State()
        state.name = "Montana"
        self.assertIsInstance(state, State)
        self.assertTrue(hasattr(state, "id"))
        self.assertEqual(state.name, "Montana")
        self.assertEqual(state.__class__.__name__, "State")

    def test_city(self):
        """Test the City class"""

        state = State()
        city = City()
        city.name = "Helena"
        city.state_id = state.id

        self.assertIsInstance(city, City)
        self.assertTrue(hasattr(city, "created_at"))
        self.assertEqual(city.name, "Helena")
        self.assertEqual(city.__class__.__name__, "City")

    def test_amenity(self):
        """Test the Amenity class"""
        amenity = Amenity()
        amenity.name = "Wifi"
        amenity.save()

        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertEqual(amenity.name, "Wifi")
        self.assertEqual(amenity.__class__.__name__, "Amenity")

    def test_review(self):
        """Test the Review class"""
        review = Review()
        place = Place()
        user = User()
        review.place_id = place.id
        review.user_id = user.id

        self.assertEqual(review.place_id, place.id)
        self.assertEqual(review.user_id, user.id)
        self.assertIsInstance(review, Review)
        self.assertTrue(hasattr(review, "created_at"))

    def test_save_method(self):
        """Test the save method"""
        review = Review()
        review.text = "love it"
        old_rev = review.updated_at
        review.save()
        new_rev = review.updated_at

        self.assertNotEqual(old_rev, new_rev)
        self.assertEqual(review.__class__.__name__, "Review")
        self.assertEqual(review.text, "love it")

    def test_to_dict_subclasses(self):
        """Test the to_dict method"""
        usr = User()
        review = Review()
        review.text = "love it"
        review.user_id = usr.id
        review.save()
        review_dict = review.to_dict()

        self.assertEqual(review_dict["__class__"], "Review")
        self.assertEqual(review_dict["text"], "love it")
        self.assertEqual(review_dict["user_id"], usr.id)

    def test_place(self):
        """test the Place class related attributes"""
        usr = User()
        cti = City()
        place = Place()
        bm1 = BaseModel()

        place.user_id = usr.id
        place.city_id = cti.id
        place.description = "My house"
        place.number_rooms = 3
        place.number_bathrooms = 1
        place.max_guest = 2
        place.price_by_night = 50
        place.latitude = 10.5
        place.longitude = 20.5
        place.amenity_ids = [usr.id, cti.id, bm1.id]

        self.assertIsInstance(place, Place)
        self.assertTrue(hasattr(place, "created_at"))
        self.assertEqual(place.user_id, usr.id)
        self.assertEqual(place.city_id, cti.id)
        self.assertEqual(place.description, "My house")
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 2)
        self.assertEqual(place.price_by_night, 50)
        self.assertEqual(place.latitude, 10.5)
        self.assertEqual(place.longitude, 20.5)
        self.assertEqual(place.amenity_ids, [usr.id, cti.id, bm1.id])
