# main.py
from kine import math


def Test():
  x = math.delta("x", delta_value=0.0, decimals=2)

  space = math.Alpha()
  space.Function = math.sin(x) + math.cos(2 * x)

  formula = math.Formula_delta(
      variable=x,
      target_func=space.Function,
      template=r"f({x}) = \sin({x}) + \cos(2 \cdot {x}) = {Alpha.Function}",
      color=math.palette.ELECTRIC_BLUE,
  )

  # Используем math.type вместо print()
  math.type("🎬 НАЧАЛО СЦЕНЫ", color=math.palette.NEON_GREEN, size=32)

  math.timeline.reveal(formula, duration_seconds=1.5)
  math.timeline.hold(1.0)
  math.timeline.shift_delta(x, destination=3.14, duration_seconds=3.0)
  math.timeline.reveal(formula, duration_seconds=1.0)

  math.type("🏁 КОНЕЦ СЦЕНЫ", color=math.palette.HOT_PINK, size=28)