#!/usr/bin/python3
""" This test module applies unittest to test the base_model moudule """
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ This tests the BaseModel class """

    def test_init(self):
        """ Testing the initialization process of BaseModel class """
        base1 = BaseModel()
        self.assertIsInstance(uuid.UUID(base1.id), uuid.UUID)
        self.assertIsInstance(base1.created_at, datetime)
        self.assertIsInstance(base1.updated_at, datetime)

    def test_time(self):
        """ Tests the consistency of the time """
        base1 = BaseModel()
        self.assertLessEqual(base1.created_at, base1.updated_at)

    def test_save(self):
        """ Testing that saves updated the object """
        base1 = BaseModel()
        create_now = base1.created_at
        update_now = base1.updated_at

        base1.save()
        self.assertNotEqual(update_now, base1.updated_at)
        self.assertEqual(create_now, base1.created_at)
