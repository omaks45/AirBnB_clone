#!/usr/bin/python3
"""A script that contains base model"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:

    """This is a class in which other classes will inherit from"""
    def __init__(self, args, kwargs):
        """initializes attribute instances
        Args:
            -*args: list of arguments
            -**kwargs: dict of key-values arguments
        """
        if kwargs is not none and kwargs != {}:
            for keys in kwargs:
                if keys == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif keys == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[keys] = kwargs[keys]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns string representation"""
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        mine_dict = self.__dict__.copy()
        mine_dict["created_at"] = mine_dict["created_at"].isformat()
        mine_dict["updated_at"] = my_dict["updated_at"].isformat()
        return mine_dict
