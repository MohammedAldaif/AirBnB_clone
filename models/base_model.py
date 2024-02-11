#!/usr / bin / python3
# comment

'''
Module for the BaseModel class
'''

import uuid
from datetime import datetime

class BaseModel:
    """
    Define the attributes and methods for all other classes.
    """


    def __init__(self, *args, **kwargs):
        """
        This method gets executed each time an object of this class is created.
        """
        from models import storage

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ('created_at', 'updated_at'):
                    dt_iso = '%Y-%m-%dT%H:%M:%S.%f'
                    setattr(self, key,
                            datetime.strptime(value,
                            dt_iso))
                else:
                    setattr(self, key, value)


    def __str__(self):
        """
        This method returns a string representation of BaseModel.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"


    def save(self):
        """
        This method updates the attribute updated_at with the current datetime.
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()


    def to_dict(self):
        """
        This method returns a dictionary containing
        all keys / values of __dict__ of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

# Set the module docstring explicitly
__import__("models.base_model").__doc__ = """
This module defines the BaseModel class.
"""
