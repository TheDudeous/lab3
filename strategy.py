from abc import ABC, abstractmethod 

class PricingStrategy(ABC):
    @abstractmethod
    def apply(self, amount: float):
        pass

class PercentageDiscount(PricingStrategy):
    def __init__(self, percent: float):
        if not (0 <= percent <= 100):
            raise ValueError("Процент скидки должен быть в диапазоне 0..100")
        self.percent = percent

    def apply(self, amount: float):
        return amount * (1 - self.percent / 100)


class FixedDiscount(PricingStrategy):
    def __init__(self, value: float):
        if value < 0:
            raise ValueError("Фиксированная скидка не может быть отрицательной")
        self.value = value

    def apply(self, amount: float):
        return max(0.0, amount - self.value)


class VIPDiscount(PricingStrategy):
    def apply(self, amount: float):
        return amount * 0.8 if amount >= 100 else amount * 0.9

class Seller():
    def __init__(self, strategy: PricingStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PricingStrategy):
        """Позволяет менять стратегию на лету."""
        self._strategy = strategy

    def apply_strategy(self, price):
        return self._strategy.apply(price)