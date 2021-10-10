# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    '''Tests for triangle.py'''

    def test_right_triangle_a(self):
        '''Tests a 3,4,5 triangle'''
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def test_right_triangle_b(self):
        '''Tests a 3,4,5 triangle in a different order'''
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def test_equilateral_triangles(self):
        '''Tests an equilateral triangle'''
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def test_isoceles_trangles(self):
        '''Tests an isoceles triangle'''
        self.assertEqual(classify_triangle(5,3,5), 'Isoceles', '1,2,1, should be isoceles')

    def test_scalene_trangles(self):
        '''Tests a scalene triangle'''
        self.assertEqual(classify_triangle(7,12,15), 'Scalene', '1,2,4, should be scalene')

    def test_not_a_triangle(self):
        '''Tests a not triangle input'''
        self.assertEqual(classify_triangle(1,2,3), 'NotATriangle', '1,2,3, is not a triangle')

    # All below added for coverage
    def test_too_long(self):
        '''Tests an input that is too long'''
        self.assertEqual(classify_triangle(1,2,300), 'InvalidInput',\
             'All inputs can be at most 200')

    def test_too_short(self):
        '''Tests if input is greater than 0'''
        self.assertEqual(classify_triangle(1,2,0), 'InvalidInput',\
             'All sides of the triangle must be greater than 0')

    def test_int(self):
        '''Tests nonint inputs'''
        self.assertEqual(classify_triangle(1.1,2.2,3.3), 'InvalidInput', 'All inputs must be ints')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
