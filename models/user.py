#!/usr/bin/env python3

from models.base_model import BaseModel

class User(BaseModel):
    """
    User class that inherits from BaseModel and defines
    public class attributes for the user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new User instance."""
        super().__init__(*args, **kwargs)
