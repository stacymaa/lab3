from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    r = Rectangle(3, 2, "blue")
    c = Circle(5, "green")
    s = Square(5, "red")
    print(r.repr())
    print(c.repr())
    print(s.repr())


if name == "__main__":
    main()