import pygame
from typing import Optional, Tuple
from pygame.font import Font
from pygame.surface import Surface
from typing import List

__all__: List[str] = []

class _Dialogue:
    def __init__(self, x: int, y: int, width: int, height: int, text: Optional[str] = None, color: Tuple[int, int, int] = (255, 255, 255), font: Optional[Font] = None):
        """
        Initialize a dialogue box.

        Args:
            x (int): The x-coordinate of the top-left corner of the dialogue box.
            y (int): The y-coordinate of the top-left corner of the dialogue box.
            width (int): The width of the dialogue box.
            height (int): The height of the dialogue box.
            text (str, optional): The text to be displayed in the dialogue box. Defaults to None.
            color (tuple, optional): The color of the text in RGB format. Defaults to (255, 255, 255).
            font (pygame.font.Font, optional): The font used for the text. Defaults to None, which uses the default font with size 24.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.font = font if font else pygame.font.Font(None, 24)

    def draw(self, screen: Surface) -> None:
        """
        Draw the dialogue box on the screen.

        Args:
            screen (pygame.Surface): The surface to draw the dialogue box on.
        """
        # Draw text in the dialogue box
        if self.text:
            lines = self.text.split('\n')
            x_offset: int = self.x + 10
            y_offset: int = self.y + 10
            for line in lines:
                text: str = self.font.render(line, True, self.color)
                screen.blit(text, (x_offset, y_offset))
                y_offset += text.get_height() + 5