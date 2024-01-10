#!/usr/bin/python3
""" This module implements the File storage system """
import json
from models import base_model


class FileStorage:
    """
    FileStorage class implementation for storing to and retrieving from files
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary containing all objects """
        return self.__objects

    def new(self, obj):
        """ Adds 'obj' to the dictionary containing all objects """
        key = ".".join([obj.__class__.__name__, obj.id])
        FileStorage.__objects[key] = obj.to_dict()
        self.save()

    def save(self):
        """ Serializes the main object dictionary to a JSON file """
        with open(FileStorage.__file_path, "w") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """ Deserializes JSON file back to the main object dictionary """
        try:
            with open(FileStorage.__file_path) as f:
                FileStorage.__objects = json.load(f)
        except:
            pass
