#!/usr/bin/python3
"""
This module defines the BaseModel class that serves as the base for all other classes.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel defines all common attributes/methods for other classes.

    Public instance attributes:
        id (str): unique identifier generated using uuid.uuid4()
        created_at (datetime): datetime when an instance is created.
        updated_at (datetime): datetime when an instance is created and updated every time the object is changed.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.

        If kwargs is not empty:
            - Each key in kwargs is used as an attribute name,
              except for the key '__class__' which is ignored.
            - For 'created_at' and 'updated_at', convert the string value to a datetime object.
        Otherwise:
            - Create a new id and set created_at and updated_at to the current datetime.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Return the string representation of the BaseModel instance.
        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute 'updated_at'
        with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance.
        - A key '__class__' is added with the class name of the object.
        - 'created_at' and 'updated_at' are converted to string objects in ISO format:
          format: %Y-%m-%dT%H:%M:%S.%f (e.g., 2017-06-14T22:31:03.285259)

        This method is used for serialization/deserialization of BaseModel.
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        if "created_at" in dict_copy:
            dict_copy["created_at"] = self.created_at.isoformat()
        if "updated_at" in dict_copy:
            dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
