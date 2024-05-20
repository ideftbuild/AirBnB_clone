#!/usr/bin/env python3
from unittest import TestCase
from models.base_model import BaseModel
#from models.engine.file_storage import FileStorage
from datetime import datetime


# FileStorage._FileStorage__file_path = 'test_file.json'


class TestBaseModel(TestCase):
    """Unittest testing for the BaseModel class"""

    # def setUp(self):
    #     """Create new instance of FileStorage for each test and reset
    #     __objects attribute to an empty dictionary
    #     """
    #     self.storage = FileStorage()
    #     self.storage._FileStorage__objects = {}

    # def tearDown(self):
    #     """Delete the JSON file that is created by a test"""
    #     from os import path, remove

    #     json_file = self.storage._FileStorage__file_path
    #     if path.isfile(json_file):
    #         remove(json_file)

    def test_uuid(self):
        """Test if uuid is a string and also unique"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1.id, str)
        self.assertTrue(hasattr(bm2, "id"))
        self.assertNotEqual(bm1.id, bm2.id)

    def test_created_and_updated_at(self):
        """Test the created_at is assigned the current time
            and updated_at is assigned the current time when save() is called
        """
        bm1 = BaseModel()
        self.assertIsInstance(bm1.created_at, datetime)
        self.assertIsInstance(bm1.updated_at, datetime)
        # test if update_at datetime updates after save method is called
        previous = bm1.updated_at
        bm1.save()
        current = bm1.updated_at
        self.assertNotEqual(previous, current)

    def test_when_kwargs_is_passed(self):
        """Test if an instance is created with the key from the dictionary
        as the attribute and the value as it corresponding value

        Note:
            - the key __class__ will not be added as an attribute
            - each value of this dictionary is the value of the attribute name
            - created_at and updated_at are converted to datetime
        """
        bm1 = BaseModel()
        model_dict = {"id": "062d5ee4-2fc8-4a1a-8205-341ce160ea4d",
                      "updated_at": "2024-05-13T11:56:30.092401",
                      "created_at": "2024-05-13T11:56:30.092340",
                      "__class__": "City"}

        bm1 = BaseModel(**model_dict)  # unpack the key and the value
        self.assertTrue(hasattr(bm1, "id"))  # check if id is present
        # should not contain the __class__ key or attribute
        self.assertFalse(bm1.__dict__.__contains__("__class__"))
        self.assertIsInstance(bm1.created_at, datetime)
        self.assertIsInstance(bm1.updated_at, datetime)

    def test_to_dict(self):
        """Test if the to_dict method returns a dictionary"""
        bm1 = BaseModel()
        bm1.name = "model_test"
        bm1.numbers = 11
        bm1.save()
        bm1_dict = bm1.to_dict()
        self.assertIsInstance(bm1_dict, dict)
        self.assertEqual(bm1_dict["name"], "model_test")
        self.assertEqual(bm1_dict["numbers"], 11)
        bm2 = BaseModel()
        bm2_dict = bm2.to_dict()
        self.assertIsInstance(bm2_dict, dict)
        self.assertIsInstance(bm2_dict["created_at"], str)

    def test_update_at_is_updated(self):
        """Verify that 'updated_at' is updated to the current datetime
        when save is called"""
        bm = BaseModel()
        old_updated_at = bm.updated_at
        self.assertTrue(hasattr(bm, 'save'))

        bm.save()
        self.assertNotEqual(bm.updated_at, old_updated_at)
        self.assertGreater(bm.updated_at, old_updated_at)
