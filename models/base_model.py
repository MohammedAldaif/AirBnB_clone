#!/usr / bin / python3
#comment

'''
Module for the BaseModel class
'''


import uuid
from datetime import datetime

class BaseModel:
    """
    define the attributes and methods for all other classes
    """


    def __init__(self, *args, **kwargs):
        """
        this method got executed each time an object of this class is created
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
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self , key ,
                            datetime.strptime(value , ' % Y - % m
                            - % dT % H : % M : % S. % f'))
                else:
                    setattr(self, key, value)


    def __str__(self):
        """
        this method returns a string representation of BaseModel
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__))


    def save(self):
        """
    this method updates the attribute updated_at with the current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()


    def to_dict(self):
        """
        this method returns a dictionary containing
        all keys / values of __dict__ of the instance
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
