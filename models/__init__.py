#!/usr/bin/env python3

"""
This package initialize models
Create a unique FileStorage instance for the application
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()