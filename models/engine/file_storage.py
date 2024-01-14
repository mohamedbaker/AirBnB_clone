#!/usr/bin/python3
""" This module implements the File storage system """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        FileStorage.__objects[key] = obj
        self.save()

    def save(self):
        """ Serializes the main object dictionary to a JSON file """
        with open(FileStorage.__file_path, "w") as f:
            dict_save = {k: v.to_dict()
                         for (k, v) in FileStorage.__objects.items()}
            json.dump(dict_save, f)

    def reload(self):
        """ Deserializes JSON file back to the main object dictionary """
        dict_load = {}
        try:
            with open(FileStorage.__file_path) as f:
                dict_load = json.load(f)
        except FileNotFoundError:
            pass
        FileStorage.__objects = {k: eval(k[:k.find(".")] + "(**v)")
                                 for (k, v) in dict_load.items()}
