'''
Prototype where lenses and objects have positions and
can be added into collections to get a final output after passing through all lenses
'''

import lenses


class Lens:
    def __init__(self, _focal_length, _position):
        self.focal_length = _focal_length




class Object:
    def __init__(self, _position, _height):
        self.position = _position
        self.height = _height

    # def __init__(self, _position):
    #     self.position = _position
    #     self.height = 1


if __name__ == "__main__":
    l = Lens(5)
    o = Object(15, 5)
    print(l.focal_length)