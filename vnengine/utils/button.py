import pygame
from typing import Optional, Tuple
from pygame.font import Font
from pygame.surface import Surface
from typing import List

__all__: List[str] = []

class _Button:
    """
    A class representing a button in a graphical user interface.

    Attributes:
        x (int): The x-coordinate of the button.
        y (int): The y-coordinate of the button.
        text (str): The text displayed on the button.
        color (tuple): The default color of the button in RGB format.
        hover_color (tuple): The color of the button when the mouse hovers over it, in RGB format.
        font (pygame.font.Font): The font used for the button text.
        scenario (str): The scenario in which the button is used ('menu', 'scene', or 'choice').
        rect (tuple): The rectangular area occupied by the button.
    """

    def __init__(self, x: int, y: int, text: Optional[str] = None, color: Tuple[int, int, int] = (110, 110, 110),
                 hover_color: Tuple[int, int, int] = (220, 220, 220), font: Optional[Font] = None,
                 scenario: str = 'menu') -> None:
        """
        Initializes a Button object.

        Args:
            x (int): The x-coordinate of the button.
            y (int): The y-coordinate of the button.
            text (str, optional): The text displayed on the button. Defaults to None.
            color (tuple, optional): The default color of the button in RGB format. Defaults to (110, 110, 110).
            hover_color (tuple, optional): The color of the button when hovered over in RGB format. Defaults to (220, 220, 220).
            font (pygame.font.Font, optional): The font used for the button text. Defaults to None.
            scenario (str, optional): The scenario in which the button is used. Defaults to 'menu'.
        """
        self.x = x
        self.y = y
        self.text = text
        self.default_color = color
        self.hover_color = hover_color
        self.font = font if font else pygame.font.Font(None, x // 25)
        self.scenario = scenario
        self.rect = (x, y)

    def draw(self, screen: Surface) -> None:
        """
        Draw the button on the screen.

        Args:
            screen (pygame.Surface): The surface on which the button is drawn.
        """
        # Check if the mouse is hovering over the text
        if self.is_over(pygame.mouse.get_pos()):
            text_color = self.hover_color
        else:
            text_color = self.default_color
        if self.scenario == 'menu':
            text = self.font.render(self.text, True, text_color)
            screen.blit(text, (self.x, self.y))
        elif self.scenario == 'scene':
            text = self.font.render(self.text, True, text_color)
            screen.blit(text, (self.x, self.y))
        elif self.scenario == 'choice':
            button_width: int = self.font.size(self.text)[0] + 20
            button_height: int = self.font.size(self.text)[1] + 10
            button_rect = pygame.Rect(self.x - button_width / 2, self.y - button_height / 2, button_width, button_height)
            pygame.draw.rect(screen, (0, 0, 0), button_rect)
            text = self.font.render(self.text, True, text_color)
            text_rect = text.get_rect(center=(self.x, self.y))
            screen.blit(text, text_rect)
            self.rect = button_rect[:2]

    def is_over(self, pos: Tuple[int, int]) -> bool:
        """
        Check if the given position is over the button. Used to check if the mouse is on the button.

        Args:
            pos (tuple): The position to check in (x, y) format.

        Returns:
            bool: True if the position is over the button, False otherwise.
        """
        # Pos is the mouse position
        additional_x: int = 0
        additional_y: int = 0
        if self.scenario == 'choice':
            (x, y) = self.rect
            additional_x = 20
            additional_y = 10
        else:
            x: int = self.x
            y: int = self.y

        if x < pos[0] < x + self.font.size(self.text)[0] + additional_x:
            if y < pos[1] < y + self.font.size(self.text)[1] + additional_y:
                return True
        return False