#!/usr/bin/env python3
"""A module that defines a class called User."""

from .base_model import BaseModel


class User(BaseModel):
    """a class User that inherits from BaseModel.

    Public attributes:
        email (str): The email address of the user, default to an empty string.
        password (str): The password of the user, default to an empty string.
        first_name (str): The first name of the user,
        default to an empty string.
        last_name (str): last name of the user, default to an empty string.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
