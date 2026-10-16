import math
from triangle import is_right_triangle, is_valid_triangle, classify_triangle

def test_is_valid_triangle():
    assert is_valid_triangle(3, 4, 5) == True
    assert is_valid_triangle(1, 1, 2) == False
    assert is_valid_triangle(0, 4, 5) == False

def test_classify_triangle():
    assert classify_triangle(3, 3, 3) == "Equilateral"
    assert classify_triangle(3, 3, 5) == "Isosceles"
    assert classify_triangle(5, 7, 10) == "Scalene"
    assert classify_triangle(3, 4, 5) == "Scalene Right"
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Isosceles Right"
    assert classify_triangle(1, 1, 2) == "Invalid"