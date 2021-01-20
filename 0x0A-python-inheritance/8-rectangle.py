#!/usr/bin/python3
''' Class Rectangle that inherits from BaseGeometry '''


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    ''' New integer_validator method that validates value parameter '''
    def __init__(self, width, height):
        self.integer_validator(width, height)
        self.__width = width
        self.__height = height

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
