#!/usr/bin/env python3
"""A module that defines a class called Amenity."""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """A class that inherit from BaseModel.
    
        Public attributes:
        name(str): empty string
        """
    name = ""
    