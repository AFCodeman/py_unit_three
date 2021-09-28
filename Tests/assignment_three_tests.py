import unittest
import assignment_three


class MyTestCase(unittest.TestCase):
    def test_rectangle_area(self):
        self.assertEqual(24,assignment_three.rectangle_area(4,6))  # add assertion here
        self.assertEqual(49,assignment_three.rectangle_area(7,7))

    def test_cube_area(self):
        self.assertEqual()
        self.assertEqual()


if __name__ == '__main__':
    unittest.main()
