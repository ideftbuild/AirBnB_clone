#!/usr/bin/env python3
"""
Module: test_review

Unit test for the Review class
"""
from unittest import TestCase
from models.review import Review
from models.place import Place
from models.user import User


class TestReview(TestCase):
    """Test Review class"""

    def test_init_of_attributes(self):
        """Test it class attributes"""

        review = Review()
        place = Place()  # Dependency for place_id
        user = User()  # Dependency for user_id
        review.place_id = place.id
        review.user_id = user.id

        self.assertEqual(review.place_id, place.id)
        self.assertEqual(review.user_id, user.id)
        self.assertIsInstance(review, Review)
        self.assertTrue(hasattr(review, "created_at"))
