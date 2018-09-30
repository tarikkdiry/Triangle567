# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def test_right_triangle_a(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right', '3,4,5 is a Right triangle')

    def test_right_triangle_b(self):
        self.assertEqual(classifyTriangle(9,12,15),'Right','9,12,15 is a Right triangle')

    def test_right_triangle_c(self):
        self.assertEqual(classifyTriangle(9,12,15), 'Right','9,12,15 is a Right triangle')

    def test_equilateral_triangles(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def test_scalene_triangle_a(self):
        self.assertEqual(classifyTriangle(1,2,3), 'Scalene')

    def test_scalene_triangle_b(self):
        self.assertEqual(classifyTriangle(100,200,300), 'InvalidInput')

    def test_isosceles_triangle_a(self):
        self.assertEqual(classifyTriangle(3,15,15), 'Isoceles','9,15,15 is an Isoceles triangle')

    def test_isosceles_triangle_b(self):
        self.assertEqual(classifyTriangle(100,300,300), 'InvalidInput')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

