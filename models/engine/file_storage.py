#!/usr/bin/env python3
"""
FileStorage module for serializing and deserializing instances to/from a JSON file.
"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.
    
    Attributes:
        __file_path (str): Path to the JSON file for storage.
        __objects (dict): Dictionary that stores all objects by <class name>.id.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to __objects.
        
        Args:
            obj (BaseModel): The object to add.
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)  # Fixed incorrect name access
            FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        json_object = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(json_object, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the file exists).
        """
        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                    json_object = json.load(f)

                for key, value in json_object.items():
                    class_name = value["__class__"]
                    if class_name == "BaseModel":
                        obj = BaseModel(**value)
                        FileStorage.__objects[key] = obj
            except Exception:
                pass
