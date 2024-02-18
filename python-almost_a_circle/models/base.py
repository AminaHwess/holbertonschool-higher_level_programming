#!/usr/bin/python3
"""
Creating a first class : base.
"""
import json


class Base:
    """
    Class : base.
    """

    __nb_objects = 0
    """
    Private class attribute
    """

    def __init__(self, id=None):
        """
        Class constructor.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of a list of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            with open(filename, mode="w") as f:
                json.dump([], f)
        else:
            mydict = []
            for object in list_objs:
                lss = object.to_dictionary()
                mydict.append(lss)

            with open(filename, mode="w") as fp:
                fp.write(cls.to_json_string(mydict))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
