from lab_python_oop.figure import GeometryFigure
from lab_python_oop.figcolor import FigureColor
import math


class Circle(GeometryFigure, FigureColor):
    def __init__(self, radius, color):
        self._r = radius
        self._name = "Circle"
        super().__init__(color)

    @property
    def radius(self):
        return self._r

    @radius.setter
    def radius(self, r):
        self._r = r

    @radius.deleter
    def radius(self):
        del self._r

    @property
    def square(self):
        return math.pi * (self._r ** 2)

    def repr(self):
        return "It's {2}, color {0}, radius {1}".format(self._value, self._r, self._name)