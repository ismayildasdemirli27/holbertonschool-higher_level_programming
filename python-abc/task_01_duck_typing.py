#!/usr/bin/env python3
from task_01_duck_typing import Circle, Rectangle, shape_info

# Dairə və düzbucaqlı obyektlərini yaratmaq
circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

# Duck typing vasitəsilə məlumatları çap etmək
print("--- Circle ---")
shape_info(circle)

print("\n--- Rectangle ---")
shape_info(rectangle)
