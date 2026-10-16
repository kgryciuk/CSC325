# Module 6
How to Run: You can run either of the test files using a command in the terminal like: python -m pytest test_triangle.py or python -m pytest test_acceptance.py

Equivalence classes/ Boundries: The files make sure that the values of any sides of the triangle are positive numbers and no zeros

Copilot review log:
test                        copilot suggested?   kept/edited/rejected        why
test_is_valid_triangle      yes                  edited                      initialy didn't call the is_valid_triangle definition
test_classify_triangle      yes                  rejected                    checked all 3 types of triangle in one
test_equilateral_triangle   no
test_isosceles_triangle     yes                  kept                        followed convention of previously made test_equilateral_triangle
test_scalene_triangle       yes                  kept                        followed convention of previously made test_isosceles_triangle and test_equilateral_triangle
test_right_triangle         yes                  edited                      added test case for non-integer side

Acceptance Criteria: Make sure that the 3 lengths entered will give a valid triangle, see what type of valid triangle will be made, see if this triangle has a right angle 

AI Usage: Claude code was used to find the way to run the test in the console as just using pytest test_acceptance.py kept on giving errors