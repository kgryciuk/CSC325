# Module 6
you can run either of the test files using a command in the terminal like: python -m pytest test_triangle.py or python -m pytest test_acceptance.py



test                        copilot suggested?   kept/edited/rejected        why
test_is_valid_triangle      yes                  edited                      initialy didn't call the is_valid_triangle definition
test_classify_triangle      yes                  rejected                    checked all 3 types of triangle in one
test_equilateral_triangle   no
test_isosceles_triangle     yes                  kept                        followed convention of previously made test_equilateral_triangle
test_scalene_triangle       yes                  kept                        followed convention of previously made test_isosceles_triangle and test_equilateral_triangle
test_right_triangle         yes                  edited                      added test case for non-integer side


Claude code was used to find the way to run the test in the console as just using pytest test_acceptance.py kept on giving errors