#!/usr/bin/python3
""" This module implements the User class """
from models.base_model import BaseModel


class User(BaseModel):
    """ User class implementation """
    def __init__(self, *args, **kwargs):
        """ Setting up initialization for User class
            *args: Is not been used
        """
        class_attr = ["email", "password", "first_name", "last_name"]
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        if kwargs:
            sub_dict = {k: kwargs[k] for k in class_attr if kwargs.get(k)}
            nargs = {k: v for (k, v) in kwargs.items() if k not in class_attr}
            super().__init__(**nargs)
            self.__dict__.update(sub_dict)
        else:
            super().__init__()
