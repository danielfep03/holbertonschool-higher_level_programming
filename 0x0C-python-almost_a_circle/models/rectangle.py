#!/usr/bin/python3
'''  '''


from models.base import Base

class Rectangle(Base):
    '''Class for drawing a rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.y = y
        self.x = x
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if type(w) is int:
            self.__width = w
        else:
            raise TypeError('width must be an integer')
        if w <= 0:
            raise ValueError('width must be > 0')

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if type(h) is int:
            self.__height = h
        else:
            raise TypeError('height must be an integer')
        if h <= 0:
            raise ValueError('height must be > 0')

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is int:
            self.__x = x
        else:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is int:
            self.__y = y
        else:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
