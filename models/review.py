#!/usr/bin/env python3
"""A module that defines a class called Place."""

from models.base_model import BaseModel


class Review(BaseModel):
    """A class that inerit from BaseModel.

    Public attributes:
    place_id(str): empty string: it will be the Place.id
    user_id(str): empty string: it will be the User.id
    text(str): empty string
    """

    place_id = ""  # Place.id
    user_id = ""  # User.id
    text = ""
