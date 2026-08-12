# src/kine/core/delta.py

class delta:
    """Динамическая переменная дельта."""

    def __init__(self, name: str, delta_value: float = 0.0, decimals: int = 2):
        self.name = name
        self.value = delta_value
        self.decimals = decimals

    def get_formatted_value(self) -> str:
        return f"{self.value:.{self.decimals}f}"

    def evaluate(self) -> float:
        return float(self.value)

    def __add__(self, other):
        return Expression(
            lambda: self.evaluate() + (other.evaluate() if hasattr(other, 'evaluate') else float(other))
        )

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return Expression(
            lambda: self.evaluate() - (other.evaluate() if hasattr(other, 'evaluate') else float(other))
        )

    def __rsub__(self, other):
        return Expression(
            lambda: (other.evaluate() if hasattr(other, 'evaluate') else float(other)) - self.evaluate()
        )

    def __mul__(self, other):
        return Expression(
            lambda: self.evaluate() * (other.evaluate() if hasattr(other, 'evaluate') else float(other))
        )

    def __rmul__(self, other):
        return self.__mul__(other)


class Expression:
    """Ленивое динамическое математическое выражение."""

    def __init__(self, func, *args, **kwargs):
        self.func = func

    def evaluate(self) -> float:
        return float(self.func())

    def __add__(self, other):
        return Expression(
            lambda: self.evaluate() + (other.evaluate() if hasattr(other, 'evaluate') else float(other))
        )

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return Expression(
            lambda: self.evaluate() - (other.evaluate() if hasattr(other, 'evaluate') else float(other))
        )

    def __rsub__(self, other):
        return Expression(
            lambda: (other.evaluate() if hasattr(other, 'evaluate') else float(other)) - self.evaluate()
        )

    def __mul__(self, other):
        return Expression(
            lambda: self.evaluate() * (other.evaluate() if hasattr(other, 'evaluate') else float(other))
        )

    def __rmul__(self, other):
        return self.__mul__(other)