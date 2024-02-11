#!/usr/bin/python3
"""
Test for BaseModel class
"""

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../')
from models.base_model import BaseModel
class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class
    """
    def test_attributes(self):
        """
        Test the attributes of BaseModel
        """
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_str(self):
        """
        Test the __str__ method of BaseModel
        """
        my_model = BaseModel()
        string = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), string)

    def test_save(self):
        """
        Test the save method of BaseModel
        """
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of BaseModel
        """
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertEqual(my_model_dict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(my_model_dict['updated_at'], my_model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
