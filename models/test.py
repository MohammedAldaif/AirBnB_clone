# models/base_model.py

import uuid
from datetime import datetime

class BaseModel:
    """
    The BaseModel class contains common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.
        """
        # rest of your code...

    def __str__(self):
        """
        Returns a string representation of the BaseModel.
        """
        # rest of your code...

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime.
        """
        # rest of your code...

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__.
        """
        # rest of your code...

# Set the module docstring explicitly
__import__("models.base_model").__doc__ = """
This module defines the BaseModel class.
"""
