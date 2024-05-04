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

    def test_gcd_strategy_with_negative_numbers(self):
        context = Context(GCDStrategy())
        self.assertEqual(context.calculate_strategy(-24, 18), 6)
        self.assertEqual(context.calculate_strategy(24, -18), 6)
        self.assertEqual(context.calculate_strategy(-24, -18), 6)

    def test_lcm_strategy_with_negative_numbers(self):
        context = Context(LCMStrategy())
        self.assertEqual(context.calculate_strategy(-24, 18), 72)
        self.assertEqual(context.calculate_strategy(24, -18), 72)
        self.assertEqual(context.calculate_strategy(-24, -18), 72)


if __name__ == '__main__':
    unittest.main()
