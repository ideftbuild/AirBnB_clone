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

   """
    def __init__(self):
        self.id = str(uuid4())
        self.updated_at = datetime.now()
        self.created_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
