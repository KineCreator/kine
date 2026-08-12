# src/kine/math.py

from typing import Union
from kine.animation.timeline import timeline
from kine.core.alpha import (
    AlphaSpace,
    FunctionSpace,
    Scope,
    acos,
    actg,
    arcctg,
    arccos,
    arcsin,
    arctan,
    arctg,
    asin,
    atan,
    cos,
    ctg,
    sin,
    sqrt,
    tan,
    tg,
)
from kine.core.delta import Expression, delta
from kine.objects.formula import Formula_delta
from kine.objects.text import Text
from kine.style.palette import Color, palette

Alpha = FunctionSpace


def type(
    content: str,
    color: Union[Color, str] = palette.WHITE,
    size: int = 24,
) -> Text:
  """Создает и выводит рендерируемый объект текста в сцене."""
  text_obj = Text(content=content, color=color, size=size)
  print(text_obj.render())
  return text_obj