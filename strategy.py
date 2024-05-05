from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def calculate(self, a, b):
        pass

class GCDStrategy(Strategy):
    def calculate(self, a, b):
        if a < 0 or b < 0:
            raise ValueError("Negative values are not allowed")
        while b != 0:
            a, b = b, a % b
        return a

class LCMStrategy(Strategy):
    def gcd(self, a, b):
        if a < 0 or b < 0:
            raise ValueError("Negative values are not allowed")
        while b != 0:
            a, b = b, a % b
        return a

    def calculate(self, a, b):
        if a < 0 or b < 0:
            raise ValueError("Negative values are not allowed")
        gcd = self.gcd(a, b)
        lcm = (a * b) // gcd
        return lcm
class Context:
    def __init__(self, strategy=None):
        if strategy is None:
            self._strategy = None
        else:
            self.set_strategy(strategy)

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def set_strategy(self, strategy):
        if strategy is None:
            raise ValueError("Strategy cannot be None")
        self._strategy = strategy

    def calculate_strategy(self, a, b):
        if self._strategy is None:
            raise ValueError("No strategy set")
        return self._strategy.calculate(a, b)


if __name__ == "__main__":
    context = Context(GCDStrategy())
    print(f"GCD: {context.calculate_strategy(24, 18)}")

    context = Context(LCMStrategy())
    print(f"LCM: {context.calculate_strategy(24, 18)}")
