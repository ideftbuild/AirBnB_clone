"""Initialize the package models
It creates FileStorage instance and read the json string from the file
during initialization
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# import other classes here


classes = {'BaseModel': BaseModel,
           'User': User,
           'State': State,
           'City': City,
           'State': State,
           'Amenity': Amenity,
           'Place': Place,
           'Review': Review,
           # other class name: class
           }

storage = FileStorage()
storage.reload()
