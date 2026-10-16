import math
from triangle import is_valid_triangle, classify_triangle, is_right_triangle

def test_is_valid_triangle():
    assert is_valid_triangle(3, 4, 5) == True
    assert is_valid_triangle(1, 1, 2) == False

def test_equilateral_triangle():
    assert classify_triangle(3, 3, 3) == "Equilateral"

def test_isosceles_triangle():
    assert classify_triangle(3, 3, 5) == "Isosceles"

def test_scalene_triangle():
    assert classify_triangle(5, 7, 10) == "Scalene"

def test_right_triangle():
    assert is_right_triangle(3, 4, 5) == True
    assert is_right_triangle(5, 5, 5* math.sqrt(2)) == True
    assert is_right_triangle(3, 3, 3) == False