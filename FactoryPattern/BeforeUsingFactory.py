class Circle:
    def draw(self):
        print("drawing a circle")


class Square:
    def draw(self):
        print("drawing a square")


def draw_shape(shape_type: str):
    # Hardcoded object creation using if/elif
    if shape_type == "circle":
        shape = Circle()
    elif shape_type == "square":
        shape = Square()
    else:
        print("Invalid shape type")
        return

    # Client code directly uses concrete class
    shape.draw()


if __name__ == "__main__":
    draw_shape("circle")
    draw_shape("square")
    draw_shape("triangle")  # invalid
