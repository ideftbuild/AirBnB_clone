#!/usr/bin/env python3
"""
Module: test_review

Unit test for the Review class
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test Review class"""
    def test_attributes(self):
        review = Review()
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)
