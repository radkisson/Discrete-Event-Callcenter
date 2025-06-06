import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import stats


class StatsCompatibilityTests(unittest.TestCase):
    def setUp(self):
        self.data = stats.load_results('results.txt')
        self.n = len(self.data) // 21

    def _old_compute(self, offset):
        metrics = []
        for i in range(7):
            total = 0.0
            with open('results.txt', 'r') as fh:
                count = 0
                for line in fh:
                    if count % 21 == offset + i:
                        total += float(line.strip())
                    count += 1
            metrics.append(total / self.n)
        return tuple(metrics)

    def test_low(self):
        expected = self._old_compute(0)
        result = stats.low(self.n, self.data)
        for a, b in zip(expected, result):
            self.assertAlmostEqual(a, b)

    def test_med(self):
        expected = self._old_compute(7)
        result = stats.med(self.n, self.data)
        for a, b in zip(expected, result):
            self.assertAlmostEqual(a, b)

    def test_hi(self):
        expected = self._old_compute(14)
        result = stats.hi(self.n, self.data)
        for a, b in zip(expected, result):
            self.assertAlmostEqual(a, b)


if __name__ == '__main__':
    unittest.main()
