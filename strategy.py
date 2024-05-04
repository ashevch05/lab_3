from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def calculate(self, a, b):
        pass

class GCDStrategy(Strategy):
    def calculate(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

class LCMStrategy(Strategy):
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def calculate(self, a, b):
        gcd = self.gcd(a, b)
        lcm = (a * b) // gcd
        return lcm

class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def set_strategy(self, strategy):
        self._strategy = strategy

    def calculate_strategy(self, a, b):
        return self._strategy.calculate(a, b)


if __name__ == "__main__":
    context = Context(GCDStrategy())
    print(f"Найбільший спільний дільник: {context.calculate_strategy(24, 18)}")

    context = Context(LCMStrategy())
    print(f"Найменше спільне кратне: {context.calculate_strategy(24, 18)}")
