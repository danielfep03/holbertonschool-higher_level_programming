#!/usr/bin/python3
''' Define a Rectangle Class'''


class Rectangle:
    '''Rectangle class with public class attribute'''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        if self.height == 0 or self.width == 0:
            return("")
        else:
            return ((str(self.print_symbol) * self.width + "\n") * self.height).strip() 

    def __repr__(self):
        return("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def area(self):
        if self.height == 0 or self.width == 0:
            return 0
        return self.height * self.width

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height * 2) + (self.width * 2)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
