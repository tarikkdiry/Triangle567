# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classifyTriangle(new_a, new_b, new_c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.

    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'

      BEWARE: there may be a bug or two in this code
    """

    # require that the input values be >= 0 and <= 200
    if new_a > 200 or new_b > 200 or new_c > 200:
        return 'InvalidInput'

    if new_a <= 0 or new_b <= 0 or new_c <= 0:
        return 'InvalidInput'

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(new_a, int) and isinstance(new_b, int) and isinstance(new_c, int)):
        return 'InvalidInput'

    # # This information was not in the requirements spec but
    # # is important for correctness
    # # the sum of any two sides must be strictly less than the third side
    # # of the specified shape is not a triangle
    # if (a >= (b - c)) or (b >= (a - c)) or (c >= (a + b)):
    #     return 'NotATriangle'
    # ACCORDING TO THE TRIANGLE INEQUALITY THEOREM,
    # THE SUM OF ANY TWO SIDES MUST BE GREATER THAN THE THIRD

    # now we know that we have a valid triangle
    return_statement = ""
    if new_a == new_b and new_b == new_c:
        return_statement = 'Equilateral'
    elif ((new_a ** 2) + (new_b ** 2)) == (new_c ** 2):
        return_statement = 'Right'
    elif ((new_a != new_b) and (new_b != new_c)):
        return_statement = 'Scalene'
    else:
        return return_statement
