# src/kine/core/alpha.py

import math as _math
from kine.core.delta import Expression


def _wrap_math_func(func, val):
  """Вспомогательная функция для ленивого вычисления математических функций."""
  if hasattr(val, "evaluate") and callable(getattr(val, "evaluate")):
    return Expression(lambda: func(val.evaluate()))
  elif callable(val):
    return Expression(lambda: func(val()))
  else:
    return float(func(val))


def sin(x):
  return _wrap_math_func(_math.sin, x)


def cos(x):
  return _wrap_math_func(_math.cos, x)


def tan(x):
  return _wrap_math_func(_math.tan, x)


def tg(x):
  return tan(x)


def ctg(x):
  return Expression(lambda: 1.0 / _math.tan(x.evaluate() if hasattr(x, "evaluate") else float(x)))


def asin(x):
  return _wrap_math_func(_math.asin, x)


def acos(x):
  return _wrap_math_func(_math.acos, x)


def atan(x):
  return _wrap_math_func(_math.atan, x)


def arcsin(x):
  return asin(x)


def arccos(x):
  return acos(x)


def arctan(x):
  return atan(x)


def arctg(x):
  return atan(x)


def actg(x):
  return ctg(x)


def arcctg(x):
  return Expression(lambda: _math.atan(1.0 / (x.evaluate() if hasattr(x, "evaluate") else float(x))))


def sqrt(x):
  return _wrap_math_func(_math.sqrt, x)


class Scope:

  def __init__(self):
    self._store = {}

  def __setattr__(self, name, value):
    if name.startswith("_"):
      super().__setattr__(name, value)
    else:
      self._store[name] = value

  def __getattr__(self, name):
    if name in self._store:
      return self._store[name]
    raise AttributeError(
        f"В пространстве функций не найдена зависимость '{name}'"
    )


class FunctionSpace(Scope):
  pass


class AlphaSpace(Scope):
  pass