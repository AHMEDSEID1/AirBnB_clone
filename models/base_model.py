#!/usr/bin/python3
""" Parent Class
"""
import uuid
from datetime import datetime


class BaseModel:
    """Base model class
    """
    def __init__(self, *args, **kwargs):
        """initializes attributes
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        else:
            f = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], f)
                if key != '__class__':
                    setattr(self, key, value)
    def save(self):
        """save def
        """
        self.updated_at = datetime.now()
    def to_dict(self):
        """ to_dict def
        """
        new_dict = {}

        for key, values in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                new_dict[key] = values.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not values:
                    pass
                else:
                    new_dict[key] = values
        new_dict['__class__'] = self.__class__.__name__

        return new_dict
    def __str__(self):
        """ str def
        """
        class_name = "[" + self.__class__.__name__ + "]"
        dct = {k: v for (k, v) in self.__dict__.items() if (not v) is False}
        return class_name + " (" + self.id + ") " + str(dct)
