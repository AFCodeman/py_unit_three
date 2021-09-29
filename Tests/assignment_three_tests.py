import unittest
from assignment_three import rectangle_area
from assignment_three import surface_area


class MyTestCase(unittest.TestCase):
    def test_rectangle_area(self):
        self.assertEqual(24,rectangle_area(4,6))  # add assertion here
        self.assertEqual(49,rectangle_area(7,7))

    def test_surface_area(self):
        self.assertEqual(22,surface_area(1,2,3))
        self.assertEqual(40,surface_area(4,2,2))


if __name__ == '__main__':
    unittest.main()
