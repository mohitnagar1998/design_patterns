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

    _shape_registry = {
        "circle": Circle,
        "rectangle": Rectangle,
        "hexagon": Hexagon
    }

    def create_shape(self, shape_type):
        shape_class = self._shape_registry.get(shape_type.lower())
        if not shape_class:
            raise ValueError(f"unknown shape type {shape_type}")
        return shape_class()


if __name__ == "__main__":
    factory = ShapeFactory()

    shape1 = factory.create_shape('circle')
    shape2 = factory.create_shape('hexagon')

    shape1.draw()
    shape2.draw()
