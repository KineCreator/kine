# src/kine/objects/formula.py

from typing import Union
from kine.style.palette import Color, palette


class Formula_delta:
  """Объект динамической формулы Kine, генерирующий LaTeX-код для MP4."""

  def __init__(
      self,
      variable,
      target_func,
      template: str,
      color: Union[Color, str] = palette.WHITE,
      display_mode: bool = True,
  ):
    self.variable = variable
    self.target_func = target_func
    self.template = template
    self.color = color
    self.display_mode = display_mode

  def _get_func_value(self) -> float:
    if hasattr(self.target_func, "evaluate") and callable(
        getattr(self.target_func, "evaluate")
    ):
      return self.target_func.evaluate()
    elif callable(self.target_func):
      return self.target_func(self.variable.value)
    return float(self.target_func)

  def to_latex(self) -> str:
    """Генерирует чистую LaTeX-строку."""
    x_val = self.variable.get_formatted_value()
    func_val = f"{self._get_func_value():.{self.variable.decimals}f}"

    latex_body = self.template.replace("{x}", str(x_val))
    latex_body = latex_body.replace("{Alpha.Function}", str(func_val))
    latex_body = latex_body.replace("{Alpha}", str(func_val))

    return f"${latex_body}$"

  def render_text(self) -> str:
    return self.to_latex()