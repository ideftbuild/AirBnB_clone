"""Initialize the package models
It creates FileStorage instance and read the json string from the file
during initialization
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
# import other classes here


classes = {'BaseModel': BaseModel,
           # other class name: class
           }

storage = FileStorage()
storage.reload()
