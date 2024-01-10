#!/usr/bin/python3
""" This module implements the BaseModel class """
import uuid
from datetime import datetime


class BaseModel:
    """ BaseModel implementation """
    def __init__(self, *args, **kwargs):
        """ Setting up initialization for BaseMode class """
        if kwargs:
            del kwargs["__class__"]
            self.__dict__.update(kwargs)
            self.created_at = datetime.fromisoformat(kwargs["created_at"])
            self.updated_at = datetime.fromisoformat(kwargs["updated_at"])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ Informal string representation of BaseModel """
        return "[{}] [{}] {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Updates the the timestamp whenever an update occurs """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing all key/value pairs """
        new_dict = self.__dict__
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
