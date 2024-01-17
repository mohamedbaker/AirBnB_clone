#!/usr/bin/python3
""" This module implements the BaseModel class """
import uuid
from datetime import datetime
import models


class BaseModel:
    """ BaseModel implementation """
    __defualts = [0, 0.0, "", []]
    def __init__(self, *args, **kwargs):
        """ Setting up initialization for BaseModel class
            *args: Is not been used
        """
        if kwargs:
            del kwargs["__class__"]
            self.__dict__.update(kwargs)
            self.created_at = datetime.fromisoformat(kwargs["created_at"])
            self.updated_at = datetime.fromisoformat(kwargs["updated_at"])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Informal string representation of BaseModel """
        print_dict = {k: v for (k, v) in self.__dict__.items()
                      if v not in BaseModel.__defualts}
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, print_dict)

    def save(self):
        """ Updates the the timestamp whenever an update occurs """
        self.updated_at = datetime.now()
        models.storage.new(self)

    def to_dict(self):
        """ Returns a dictionary containing all key/value pairs """
        new_dict = {k: v for (k, v) in self.__dict__.items()
                      if v not in BaseModel.__defualts}
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
