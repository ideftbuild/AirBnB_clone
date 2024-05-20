#!/usr/bin/env python3
"""A module that defines a class called FileStorage"""

import json


class FileStorage:
    """A class that serializes and deserializes instances to and from

    Private Attributes:
        __file_path: string - path to the JSON file
        __objects: dictionary - empty but will store all objects
        by <obj class name>.id

    Methods:
        all(): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with
        key <obj class name>.id
        save(self): serializes __objects to the JSON
        file (path: __file_path)
        reload(self): deserializes the JSON file to __objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects
        Return:
            dict: a dictionary of all objects"""
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w', encoding='UTF-8') as file:
            objs_dict = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(objs_dict, file)

    def reload(self):
        """Deserializes the structured JSON data set to instances"""
        from models import classes
        from os.path import isfile

        if isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='UTF-8') as file:
                try:
                    objs_dict = json.load(file)
                    # convert dictionary to instance and update self.__objects
                    self.__objects = {}
                    for k, v in objs_dict.items():
                        class_name = v['__class__']
                        if class_name in classes:
                            self.__objects[k] = classes[class_name](**v)
                except json.JSONDecodeError:  # file is not in JSON format
                    pass
