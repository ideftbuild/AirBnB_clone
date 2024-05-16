#!/usr/bin/env python3
"""A module that defines a class called State."""

from .base_model import BaseModel


class State(BaseModel):
    """A class that inherit from BaseModel.

    Public attributes:
    name(str): the name of the state, default to empty string
    """

    name = ""
