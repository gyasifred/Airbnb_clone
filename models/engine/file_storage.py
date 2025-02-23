#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """ This class helps us serialize and deserialize our objects into/from JSON file """

    __file_path = "file.json"
    __objects = {}

    CLASSES = {
        "BaseModel": BaseModel,
        "User": User,
    }

    def all(self):
        """Returns the __objects dictionary."""
        return self.__objects

    def new(self, obj):
        """Sets a new object into the __objects dictionary."""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Serializes the __objects dictionary to a JSON file."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file into the __objects dictionary."""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                try:
                    deserialized_objects = json.load(file)
                    for key, values in deserialized_objects.items():
                        class_name = values["__class__"]
                        if class_name in self.CLASSES:
                            cls = self.CLASSES[class_name]
                            instance = cls(**values)
                            self.__objects[key] = instance
                except Exception as e:
                    pass
