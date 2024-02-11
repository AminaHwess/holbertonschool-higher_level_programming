#!/usr/bin/python3
"""
Class 'Student'
"""


class Student:
    """
    Retrieve dict representation of Student instance
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            if all(type(element) is str for element in attrs):
                return {
                    element: getattr(self, element)
                    for element in attrs
                    if hasattr(self, element)
                }
        else:
            return self.__dict__
