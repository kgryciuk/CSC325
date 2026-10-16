import math

def is_valid_triangle(a,b,c):
    if(a<=0 or b<=0 or c<=0):
        return False
    return a + b > c and b + c > a and c + a > b

def classify_triangle(a,b,c):
    if not is_valid_triangle(a, b, c):
        return "Invalid"
    if(a==b and b==c):
        return "Equilateral"
    elif(a==b or b==c or c==a):
        if is_right_triangle(a, b, c):
            return "Isosceles Right"
        return "Isosceles"
    else:
        if is_right_triangle(a, b, c):
            return "Scalene Right"
        return "Scalene"

def is_right_triangle(a,b,c):
    if not is_valid_triangle(a, b, c):
        return False
    sides = sorted((a, b, c))
    return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2, rel_tol=1e-9, abs_tol=1e-9)