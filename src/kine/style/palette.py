# src/kine/style/palette.py

from typing import Tuple


class Color:
  """Класс цвета Kine с поддержкой RGB и генерации прозрачности (RGBA)."""

  def __init__(self, hex_code: str):
    self.hex = hex_code.strip()

  def to_rgb(self) -> Tuple[int, int, int]:
    """Возвращает RGB кортеж (0-255, 0-255, 0-255)."""
    h = self.hex.lstrip('#')
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))

  def opacity(self, alpha: float) -> str:
    """Возвращает CSS/SVG rgba-строку с нужной прозрачностью (0.0 - 1.0)."""
    r, g, b = self.to_rgb()
    return f"rgba({r}, {g}, {b}, {alpha})"

  def __str__(self) -> str:
    return self.hex


class Palette:
  # НЕОН И КИБЕРПАНК
  ELECTRIC_BLUE = Color('#00D2FF')
  NEON_GREEN = Color('#39FF14')
  CYBER_PURPLE = Color('#9D00FF')
  HOT_PINK = Color('#FF007F')
  LASER_YELLOW = Color('#FFE600')
  PLASMA_ORANGE = Color('#FF5500')
  CYAN = Color('#00FFFF')
  LIME = Color('#BFFF00')

  # ПАСТЕЛЬНЫЕ ТОНА
  PASTEL_BLUE = Color('#89CFF0')
  PASTEL_GREEN = Color('#77DD77')
  PASTEL_PINK = Color('#FFD1DC')
  PASTEL_YELLOW = Color('#FDFD96')
  PASTEL_PURPLE = Color('#B19CD9')
  PASTEL_ORANGE = Color('#FFB347')
  MINT = Color('#98FF98')
  LAVENDER = Color('#E6E6FA')

  # ГРАФИКИ
  GRAPH_RED = Color('#FF4136')
  GRAPH_BLUE = Color('#0074D9')
  GRAPH_GREEN = Color('#2ECC40')
  GRAPH_ORANGE = Color('#FF851B')
  GRAPH_PURPLE = Color('#B10DC9')
  GRAPH_TEAL = Color('#39CCCC')
  GRAPH_GOLD = Color('#FFD700')

  # ФОНЫ И МОНОХРОМ
  PURE_BLACK = Color('#000000')
  DARK_BG = Color('#0D0E15')
  DARK_PANEL = Color('#181A24')
  CHARCOAL = Color('#222222')
  GRAY = Color('#888888')
  LIGHT_GRAY = Color('#DDDDDD')
  PURE_WHITE = Color('#FFFFFF')
  WHITE = PURE_WHITE

  # СТАTУСЫ
  SUCCESS = Color('#28A745')
  WARNING = Color('#FFC107')
  ERROR = Color('#DC3545')
  INFO = Color('#17A2B8')


palette = Palette()