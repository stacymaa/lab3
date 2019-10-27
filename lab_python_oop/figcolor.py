class FigureColor(object):

    def __init__(self, col):
        """Constructor of figure class"""
        FigureColor._value = col

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    @value.deleter
    def value(self):
        del self._value