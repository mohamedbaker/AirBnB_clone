#!/usr/bin/python3
""" This test module applies unittest to test the file_storage module """
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """ This tests the FileStorage class """

    def setUp(self):
        self.mystorage = FileStorage()

    def test_all(self):
        """ Testing that 'all' function returns a dictionary """
        self.assertIsInstance(self.mystorage.all(), dict)

    def test_new(self):
        """ Testing that a new object has been added to main object dict """
        base1 = BaseModel()
        key = ".".join([base1.__class__.__name__, base1.id])
        self.assertTrue(self.mystorage.all()[key])

    def test_save_reload(self):
        """ Testing the save and reload functions """
        self.mystorage.reload()
        first_len = len(self.mystorage.all())
        base1 = BaseModel()
        self.mystorage.reload()
        sec_len = len(self.mystorage.all())
        self.assertGreater(sec_len, first_len)
