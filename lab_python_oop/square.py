from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, a, color):
        self._name = "Square"
        super().__init__(a, a, color)

    def repr(self):
        return "It's {2}, color {0}, side length {1}".format(self._value, self._w, self._name)