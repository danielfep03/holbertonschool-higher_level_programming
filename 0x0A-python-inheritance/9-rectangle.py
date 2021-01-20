#!/usr/bin/python3
''' Class Rectangle that inherits from BaseGeometry '''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' Rectangle class '''
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        return self.__width * self.__height

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
