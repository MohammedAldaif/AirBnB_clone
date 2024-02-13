#!/usr/bin/python3
"""
Module for the FileStorage class
"""
import sys
import os
import json
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../')
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    this class is for converting instances to a json file
    and converting json file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        convert __objects to json file
        """
        save_dict = {}
        for key, value in FileStorage.__objects.items():
            save_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(save_dict, f)

    def reload(self):
        """
        convert json file to __objects,
        if __objects exists, otherwise do nothing.
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                load_dict = json.load(f)
                for key, value in load_dict.items():
                    class_name, obj_id = key.split('.')
                    cls = eval(class_name)
                    # Convert class name to class object
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            # handles the case where the file is empty or not valid JSON
            print("File is empty or not valid JSON. No objects loaded.")
