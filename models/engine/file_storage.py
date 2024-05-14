#!/usr/bin/env python3
""" A module that defines a class called FileStorage """

import json
import os
import importlib


class FileStorage:
    """ A class that serializes and deserializes instances to and from
            
            Private Attributes:
                __file_path: string - path to the JSON file
                __objects: dictionary - empty but will store all objects by <obj class name>.id
            
            Methods:
                all(): returns the dictionary __objects
                new(self, obj): sets in __objects the obj with key <obj class name>.id
                save(self): serializes __objects to the JSON file (path: __file_path)
                reload(self): deserializes the JSON file to __objects
            """


    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects 
            Return:
                dict: a dictionary of all objects"""
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    cls_name, obj_id = key.split('.')
                    module_name = cls_name.lower()
                    module_dynamically = \
                        importlib.import_module("models." + module_name)
                    class_obj = getattr(module_dynamically, cls_name)
                    instance_obj = class_obj(**value)
                    self.__objects[key] = instance_obj
