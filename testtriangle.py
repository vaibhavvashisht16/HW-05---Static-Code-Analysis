import unittest
from triangle_updated import classify_triangle

class MyTestCase(unittest.TestCase):
    def test_invalid_input(self):
        self.assertEqual(classify_triangle(-2, 1, 4), 'InvalidInput', '-2,1,4 is a Not a Invalid input')

    def test_invalid_input1(self):
        self.assertEqual(classify_triangle(200,400,300), 'InvalidInput', '200,400,300 is Not a Invalid input')

    def test_not_triangle2(self):
        self.assertNotEqual(classify_triangle(3, 1.5, 1.5), "Equilateral", "Should be Not a Triangle")

    def testInvalidInput3(self):
        self.assertEqual(classify_triangle(0,0,0), 'InvalidInput', '0,0,0 is Not a Invalid input')

    def testNotaTriangle1(self):
        self.assertEqual(classify_triangle(1, 10, 12), "NotATriangle", "Should be Not a Triangle")

    def testNotaTriangle2(self):
        self.assertNotEqual(classify_triangle(3, 1.5, 1.5), "Equilateral", "Should be Not a Triangle")

    def testNotaTriangle3(self):
        self.assertNotEqual(classify_triangle(1, 1, 2), "Isosceles", "Should be Not a Triangle")

    def testNotaTriangle4(self):
        self.assertNotEqual(classify_triangle(1, 4, 6), "Scalene", "Should be Not a Triangle")

    def testNotaTriangle5(self):
        self.assertNotEqual(classify_triangle(4, 2, 6), "Right", "Should be Not a Triangle")

    def testRightTriangleA1(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Right', '3, 4, 5 should be Right Triangle')

    def testRightTriangleA2(self):
        self.assertNotEqual(classify_triangle(12, 13, 5), "Isosceles", "Should be Right")

    def testRightTriangleA3(self):
        self.assertNotEqual(classify_triangle(10, 6, 8), "Equilateral", "Should be Right")

    def testRightTriangleA4(self):
        self.assertNotEqual(classify_triangle(4, 3, 5), "NotATriangle", "Should be Right")

    def testRightTriangle5(self):
        self.assertNotEqual(classify_triangle(12, 13, 5), "Scalene", "Should be Right")

    def testIsoscelesTriangle1(self):
        self.assertEqual(classify_triangle(3, 3, 5), 'Isosceles', '5,3,4 is a Isosceles triangle')

    def testIsoscelesTriangle2(self):
        self.assertNotEqual(classify_triangle(4, 2, 2), "Scalene", "Should be Isosceles")

    def testIsoscelesTriangle4(self):
        self.assertNotEqual(classify_triangle(5, 9, 5), 'Right', 'Should be Isosceles')

    def testIsoscelesTriangle3(self):
        self.assertNotEqual(classify_triangle(5, 5, 3), "Equilateral", "Should be Isosceles")

    def testScaleneTriangle(self):
        self.assertEqual(classify_triangle(3, 10, 12), "Scalene", "Should be Scalene")

    def testScaleneTriangle1(self):
        self.assertNotEqual(classify_triangle(1, 3, 2), "Isosceles", "Should be Scalene")

    def testScaleneTriangle2(self):
        self.assertNotEqual(classify_triangle(3, 4, 1.5), "Equilateral", "Should be Scalene")

    def testScaleneTriangle3(self):
        self.assertNotEqual(classify_triangle(4, 2, 6), "Right", "Should be Scalene")

    def testScaleneTriangle4(self):
        self.assertNotEqual(classify_triangle(3, 4, 7), "Not a Triangle", "Should be Scalene")

    def testEquilateralTriangle1(self):
        self.assertEqual(classify_triangle(1, 1, 1), "Equilateral", "Should be Equilateral")

    def testEquilateralTriangle2(self):
        self.assertNotEqual(classify_triangle(6, 6, 6), "Right", "Should be Equilateral")

    def testEquilateralTriangle3(self):
        self.assertNotEqual(classify_triangle(1.5, 1.5, 1.5), "NotATriangle", "Should be Equilateral")


if __name__ == '__main__':
    unittest.main()
