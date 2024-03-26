import unittest
import penndraw as pd


class SetPenColorErrors(unittest.TestCase):

    def test_set_invalid_color_neg1_0_0(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color(-1, 0, 0)

    def test_set_invalid_color_0_neg1_0(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color(0, -1, 0)

    def test_set_invalid_color_0_0_neg1(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color(0, 0, -1)

    def test_set_invalid_color_0_0_0_neg1(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color(0, 0, 0, -1)

    def test_set_invalid_color_300_0_0(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color(300, 0, 0)

    def test_set_invalid_color_0_300_0(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color(0, 300, 0)

    def test_set_invalid_color_0_0_300(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color(0, 0, 300)

    def test_set_invalid_color_0_0_0_300(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color(0, 0, 0, 300)

    def test_set_invalid_color_2_args(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color(0, 0)

    def test_set_invalid_color_5_args(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color(0, 0, 0, 0, 0)

    def test_set_invalid_color_tuple_2(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color((0, 0))

    def test_set_invalid_color_tuple_5(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color((0, 0, 0, 0, 0))

    def test_set_invalid_color_tuple_neg1_0_0(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color((-1, 0, 0))

    def test_set_invalid_color_tuple_0_neg1_0(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color((0, -1, 0))

    def test_set_invalid_color_tuple_0_0_neg1(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color((0, 0, -1))

    def test_set_invalid_color_tuple_0_0_0_neg1(self):
        with self.assertRaises(ValueError):
            pd.set_pen_color((0, 0, 0, -1))


class AlwaysPasses(unittest.TestCase):

    def test_always_passes(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
