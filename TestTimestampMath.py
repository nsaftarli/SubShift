import unittest
from SubFix import *
import numpy as np

class TestTimestampMath(unittest.TestCase):

    def test_subtract_thousands(self):
        ts1 = np.array([0, 0, 5, 1])
        ts2 = np.array([0, 0, 0, 2])
        res = np.array([0, 0, 4, 999])
        print(subtract_thousands(ts1, ts2))
        self.assertTrue(np.array_equal(subtract_thousands(ts1, ts2), res))

    def test_ms_conversion(self):
        ts = np.array([2, 4, 58, 727])
        self.assertEqual(convert_to_ms(ts), 7498727)

    def test_ts_concersion(self):
        ms = 7498727
        ts = [2, 4, 58, 727]
        print(convert_to_ts(ms))
        self.assertTrue(np.array_equal(convert_to_ts(ms), ts))


if __name__ == '__main__':
    unittest.main()