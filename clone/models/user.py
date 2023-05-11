#!/usr/bin/python3
"""This module creates a class called User"""
from models.base_model import BaseModel


class User(BaseModel):
    """This is the class for managing the User objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
