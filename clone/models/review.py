#!/usr/bin/python3
"""This module creates a class called Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """This is the class for managing the Review objects"""

    place_id = ""
    user_id = ""
    text = ""
