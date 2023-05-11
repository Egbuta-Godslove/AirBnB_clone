#!/usr/bin/python3
"""This module creates a User called class"""

from models.base_model import BaseModel


class City(BaseModel):
    """This is the class for managing the city objects"""

    state_id = ""
    name = ""
