#!/usr/bin/env python3
"""
Defines the BaseModel class.

Example:
    bm1 = BaseModel()
    >>> print(bm1)  # doctest: +ELLIPSIS
        [BaseModel] (...) {...}
"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """ Defines common attributes and methods for other classes.

    Attributes:
        id (str): A unique identifier for each instance.
        created_at (datetime): Assigned with the current datetime when an
            instance is created.
        updated_at (datetime): Assigned with the current datetime when an
            instance is created and updated whenever the object changes.

    Methods:
        __init__(): Initializes the instance attributes.
        __str__(): Returns a string representation of the instance:
            "[<class name>] (<self.id>) <self.__dict__>".
        save(): Updates the public instance attribute 'updated_at' with the
            current datetime.
        to_dict(): Returns a dictionary containing all keys and values of
            __dict__ of the instance. Includes a key '__class__' with the class
            name, and 'created_at' and 'updated_at' converted to ISO format.

    """
    def __init__(self, *args, **kwargs):
        """Initializes the instance attribute"""
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    # convert from ISO string format to datetime
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        from models import storage
        """Saves the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys and values of __dict__.
        and key __class__ with the class name.
        """
        dict_data = self.__dict__.copy()
        dict_data['updated_at'] = self.updated_at.isoformat()
        dict_data['created_at'] = self.created_at.isoformat()
        dict_data['__class__'] = self.__class__.__name__
        return dict_data
