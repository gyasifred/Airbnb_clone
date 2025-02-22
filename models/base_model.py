#!/usr/bin/python3
"""
This module defines the BaseModel class that serves as the base for all other classes.
"""

import uuid
from datetime import datetime


class BaseModel:
    """BaseModel defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        from models import storage 

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    try:
                        setattr(self, key, datetime.fromisoformat(value))
                    except ValueError:
                        raise ValueError(
                            f"Invalid date format for {key}: {value}")
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Return string representation of BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at with current datetime and save to storage."""
        from models import storage  

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return dictionary representation of BaseModel."""
        return {
            **self.__dict__,
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat() if hasattr(self, "created_at") else None,
            "updated_at": self.updated_at.isoformat() if hasattr(self, "updated_at") else None,
        }
