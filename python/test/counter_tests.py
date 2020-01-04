#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
from counter_class import Counter
import unittest

class CounterTests(unittest.TestCase):
    def setUp(self):
        self.counter = Counter()

    def test_starting_value(self):
        self.assertEqual(self.counter.count, 0)
        self.assertEqual(Counter(count = 1000).count, 1000)
        self.assertEqual(Counter(count = -13).count, -13)

    def test_incrementing(self):
        negative = Counter(count = -123)
        for i in range(10):
            self.counter.increment()
            negative.increment()
            self.assertEqual(self.counter.count, i+1)
        self.assertEqual(negative.count, -123+10)

    def test_decrementing(self):
        negative = Counter(count = -999999)
        for i in range(10):
            self.counter.decrement()
            negative.decrement()
            self.assertEqual(self.counter.count, -(i+1))
        self.assertEqual(negative.count, -999999-10)

    def test_resetting(self):
        big = Counter(count = 999999)
        zero = Counter(count = 0)
        neg = Counter(count = -10)
        big.reset()
        zero.reset()
        neg.reset()
        self.counter.reset()

        self.assertEqual(big.count, 0)
        self.assertEqual(zero.count, 0)
        self.assertEqual(neg.count, 0)
        self.assertEqual(self.counter.count, 0)


if __name__ == "__main__":
    unittest.main()
        
