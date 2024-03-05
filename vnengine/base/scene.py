from typing import Dict
from vnengine.base.choice import _Choice
from typing import List

__all__: List[str] = []

class _Scene:
    """
    Represents a scene in the game.

    Attributes:
        character_text (str): The text spoken by the character in the scene.
        background_display_img (str): The image file path for the background display.
        choices (Dict[str, _Choice]): A dictionary of choices available in the scene.
    """

    def __init__(self, character_text: str, image: str, scene_number: int) -> None:
        """
        Initializes a Scene.

        Args:
            character_text (str): The text spoken by the character in the scene.
            image (str): The image file path for the background display.
            scene_number (int): The number of the scene created
        """
        self.character_text: str = character_text
        self.background_display_img: str = image
        self.scene_number: int = scene_number
        self.choices: Dict[str, _Choice] = {}
        
    def add_choice(self, choice_text: str, go_to_scene: str) -> None:
        """
        Adds a choice to a scene. Choices are shown in the order in which they were created.

        Args:
            choice_text (str): The text of the choice.
            go_to_scene (str): The name of the scene to go to when the choice is selected.
        """
        self.choices[go_to_scene] = _Choice(choice_text)