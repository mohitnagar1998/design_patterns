from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print("drawing a circle")


class Rectangle(Shape):
    def draw(self):
        print("drawing a rectangle")


class Hexagon(Shape):
    def draw(self):
        print("drawing a hexagon")


class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()

        elif shape_type == "rectangle":
            return Rectangle()

        elif shape_type == "hexagon":
            return Hexagon()

        else:
            return "unknown shape type"


if __name__ == "__main__":
    factory = ShapeFactory()

    shape1 = factory.create_shape('circle')
    shape2 = factory.create_shape('hexagon')

    shape1.draw()
    shape2.draw()
