def shape_info(shape):
    """Prints the area and perimeter of a given shape."""
    try:
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}")
    except AttributeError:
        pass
