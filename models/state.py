#!/usr/bin/python3
"""
Class State inherits from BaseModel
"""


import uuid
from models.base_model import BaseModel
import datetime


class State(BaseModel):
    """
    Class State definition
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Instantiation
        """
        super().__init__(*args, **kwargs)
