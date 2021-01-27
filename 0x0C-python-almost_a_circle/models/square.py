#!/usr/bin/python3
''' Module to create a Square '''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''Class to create a Square'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Str Method'''
        return str(('[Square] ({:d}) {:d}/{:d} - {:d}'
                    .format(self.id, self.x, self.y, self.width)))

    def update(self, *args, **kwargs):
        '''Updates the square attributes'''
        my_list = ['id', 'size', 'x', 'y']
        if args and args[0]:
            for item in range(len(args)):
                setattr(self, my_list[item], args[item])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''Return a dictionary representation'''
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, s):
        self.width = s
        self.height = s
