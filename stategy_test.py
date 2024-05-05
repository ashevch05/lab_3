from strategy import GCDStrategy, LCMStrategy, Context
import unittest

class TestStrategies(unittest.TestCase):
    def test_gcd_strategy(self):
        context = Context(GCDStrategy())
        self.assertEqual(context.calculate_strategy(24, 18), 6)
        self.assertEqual(context.calculate_strategy(30, 20), 10)
        self.assertEqual(context.calculate_strategy(0, 10), 10)
        self.assertEqual(context.calculate_strategy(10, 0), 10)

    def test_lcm_strategy(self):
        context = Context(LCMStrategy())
        self.assertEqual(context.calculate_strategy(24, 18), 72)
        self.assertEqual(context.calculate_strategy(12, 16), 48)
        self.assertEqual(context.calculate_strategy(0, 10), 0)
        self.assertEqual(context.calculate_strategy(10, 0), 0)

    def test_gcd_negative_values(self):
        strategy = GCDStrategy()
        with self.assertRaises(ValueError):
            strategy.calculate(-24, 18)
        with self.assertRaises(ValueError):
            strategy.calculate(24, -18)
        with self.assertRaises(ValueError):
            strategy.calculate(-24, -18)

    def test_lcm_negative_values(self):
        strategy = LCMStrategy()
        with self.assertRaises(ValueError):
            strategy.calculate(-24, 18)
        with self.assertRaises(ValueError):
            strategy.calculate(24, -18)
        with self.assertRaises(ValueError):
            strategy.calculate(-24, -18)

    def test_set_null_strategy(self):
        context = Context()
        with self.assertRaises(ValueError):
            context.set_strategy(None)

    def test_calculate_without_strategy(self):
        context = Context()
        with self.assertRaises(ValueError):
            context.calculate_strategy(24, 18)




if __name__ == '__main__':
    unittest.main()
