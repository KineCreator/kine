# src/kine/objects/text.py

from typing import Union
from kine.style.palette import Color, palette


class Text:
    """
    Объект текста Kine.

    Если content содержит LaTeX-команды,
    Timeline автоматически отрисует его как формулу.
    """

    def __init__(
        self,
        content: str,
        color: Union[Color, str] = palette.WHITE,
        size: int = 24,
    ):
        self.content = content
        self.color = color
        self.size = size

    def render_text(self) -> str:
        return self.content

    def render(self) -> str:
        color_hex = str(self.color)
        return (
            f"[Text size={self.size}px "
            f"color='{color_hex}']: {self.content}"
        )