from lab_python_oop.figure import GeometryFigure
from lab_python_oop.figcolor import FigureColor


class Rectangle(GeometryFigure, FigureColor):
    def __init__(self, width, height, color):
        self._w = width
        self._h = height
        self._name = "Rectangle"
        super().__init__(color)

    """width prop"""
    @property
    def width(self):
        return self._w

    @width.setter
    def width(self, w):
        self._w = w

    @width.deleter
    def width(self):
        del self._w

    """height prop"""
    @property
    def height(self):
        return self._h

    @height.setter
    def height(self, h):
        self._h = h

    @height.deleter
    def height(self):
        del self._h

    def square(self):
        return self._h * self._w

    def repr(self):
        return "It's {3}, color {0}, width {1}, height {2}".format(self._value, self._w, self._h, self._name)