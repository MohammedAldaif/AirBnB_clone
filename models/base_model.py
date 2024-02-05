#!/usr/bin/python3
"""
Module for BaseModel class
"""
import uuid
from datetime import datetime

class BaseModel:
    """
    the BaseModel class defines common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        create a new instance of BaseModel class
        """
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        this method returns a string representation of the BaseModel instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        this method pdates the attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        this method eturns a dictionary representation of the BaseModel instance
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
