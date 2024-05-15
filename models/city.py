#!/usr/bin/env python3
"""A module that define a class called City"""

from models.base_model import BaseModel


class City(BaseModel):
    """A class that inherit from BaseModel.

    Public attributes:
    state_id(str): the id of the State class(State.id),
    default to empty string
    name(str): the name, default to empty string
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
