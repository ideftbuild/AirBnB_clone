#!/usr/bin/env python3
"""Unit Test for FileStorage class

Module: test_file_storage
Class: TestFileStorage
Example:
    `python3 -m unittest tests/test_models/test_engine/test_file_storage.py``

"""

# standard library imports
import os
# related third party imports
from unittest import TestCase
# local imports
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


FileStorage._FileStorage__file_path = 'test_file.json'


class TestFileStorage(TestCase):
    def setUp(self):
        """Create new instance of FileStorage for each test and reset
        __objects attribute to an empty dictionary
        """
        self.storage = FileStorage()
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """Delete the JSON file that is created by a test"""
        json_file = self.storage._FileStorage__file_path
        if os.path.isfile(json_file):
            os.remove(json_file)

    def test_all(self):
        """Test vefies that all returns a dictionary of __objects"""
        self.assertIsInstance(FileStorage().all(), dict)

    def test_new(self):
        """Ensure that it correctly set __objects to the obj instance or
        dictionary, with a key <obj class name>.id
        """
        bm = BaseModel()

        self.storage.new(bm)  # store the object
        key = f'{bm.__class__.__name__}.{bm.id}'
        self.assertTrue(self.storage.all().__contains__(key))
        self.assertEqual(self.storage.all()[key], bm)

    def test_save(self):
        """Test ensures that it saves the data set in the JSON file"""
        bm1 = BaseModel()

        self.storage.new(bm1)
        self.storage.save()

        file = self.storage._FileStorage__file_path
        self.assertTrue(os.path.exists(file))
        self.assertTrue(os.path.getsize(file) > 0)

    def test_reload(self):
        """Test if it correctly deserializes the JSON file to __objects"""

        bm1 = BaseModel()
        self.storage.new(bm1)  # __objects is changed to it previous state

        obj_prev_state = self.storage.all().copy()
        self.storage.save()  # write the object to the file

        bm2 = BaseModel()
        self.storage.new(bm2)
        self.storage.reload()  # override

        self.assertEqual(obj_prev_state.keys(), self.storage.all().keys())
        self.assertIsInstance(self.storage.all(), dict)
