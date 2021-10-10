# HW05_Static_Code_Analysis
#### Author
Mathieu Nagle
#### Summary
I used pylint as my Static Code analyzer and coverage.py as my coverage tool.
#### Detailed results, if any:
Here is the pylint outout for the Triangles.py code.

![](Images/Pylint%20Before.PNG)

I made most of the changes it suggested but I didn't understand what the issue was with the a, b, c variables. I also didn't think there was anything I could do about the return statements.

![](Images/Pylint%20After.PNG)

Here is the pylint outout for the TestTriangles.py code.

![](Images/Pylint%20Test%20Before.PNG)

I was able to make all the changes it requested for this code.

![](Images/Pylint%20Test%20After.PNG)

Here was my coverage output before making changes. It was already above 80% but I decided to add more tests cases just to test the software.

![](Images/Coverage%20Before.PNG)

These are the test cases I added:

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
Here is my coverage after adding the new test cases.

![](Images/Coverage%20After.PNG)
