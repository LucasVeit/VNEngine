from typing import List
from vnengine.base.scene import _Scene
import warnings
from vnengine.utils.game import _Game
import os

class Story:
    """
    Represents the story with its scenes and choices.

    Attributes:
        starting_background (str): The path of the starting menu background image.
        scenes (dict): A dictionary containing the scenes of the story.
    """

    def __init__(self):
        """
        Initializes a new instance of the Story class.
        """
        self.starting_background: str = None # starting menu background image
        self.scenes: dict = {}
        self.scenes_names: List[str] = []
        self.languages: List[str] = ['pt', 'en']
        self.language: str = 'pt'
        self.resolution: str = 'hd'
        self.number_scenes: int = 0
    
    def set_languages(self, languages: List[str]) -> None:
        """
        Set the languages available for narration.
        
        Args:
            languages (list): A list of language codes representing the available languages.
                Availables: ['de', 'en', 'es', 'fr', 'pt'].
        """
        self.languages = languages
        
    def set_initial_language(self, language: str) -> None:
        """
        Set the initial language for the story.

        Parameters:
        language (str): The language to set.
            Availables: 'de', 'en', 'es', 'fr', 'pt'.

        Returns:
        None
        """
        self.language = language
    
    def set_resolution(self, resolution: str) -> None:
        """
        Set the resolution of the story.

        Args:
            resolution: A String with the choosen resolution.
                Availables: 'hd', 'fullhd', '4k'.

        Returns:
            None
        """
        self.resolution = resolution
        
    def add_starting_background(self, image: str) -> None:
        """
        Adds the starting menu background image to the story.

        Args:
            image (str): The path of the starting menu background image.
        """
        self.starting_background = image

    def add_scene(self, scene_name: str, character_text: str, image: str) -> None:
        """
        Adds a new scene to the story.

        Args:
            scene_name (str): The name of the scene.
            character_text (str): The text spoken by the character in the scene.
            image (str): The path of the image displayed as the background of the scene.
        """
        self.scenes[scene_name] = _Scene(character_text, image, len(self.scenes_names))
        self.scenes_names.append(scene_name)

    def add_choice(self, current_scene_name: str, choice_text: str, go_to_scene: str) -> None:
        """
        Adds a choice to a scene.

        Args:
            current_scene_name (str): The name of the current scene.
            choice_text (str): The text of the choice.
            go_to_scene (str): The name of the scene to go to when the choice is selected.
        """
        self.scenes[current_scene_name].add_choice(choice_text, go_to_scene)
        
    def validatePathing(self) -> None:
        """
        Validates the pathing of the story by checking if all scenes are reachable from a choice.
        Raises a ValueError if a scene is not defined in the story.
        Issues a warning if a scene is not reachable from any choice.
        """
        if len(self.scenes_names) == 0:
            raise ValueError("There are no scenes defined for the visual novel.")
            
        reachable: List[bool] = [False] * len(self.scenes_names)
                
        stack: List[_Scene] = [self.scenes[self.scenes_names[0]]] 
        
        current: _Scene = None
        
        while stack:
            current = stack.pop()
            reachable[current.scene_number] = True
            
            for s in current.choices.keys():
                if not s in self.scenes_names:
                    raise ValueError(f"Scene {s} is not defined in the story. Define this scene so it can be used in a choice.")
                
                if not self.scenes[s] in stack and not reachable[self.scenes_names.index(s)]:
                    stack.append(self.scenes[s])

        for idx, s  in enumerate(reachable):
            if s == False:
                warnings.warn(f"Scene {self.scenes_names[idx]} is not reachable from any choice")
                            
    def run(self) -> None:
        """
        Runs the game with the scenes and choices defined.
        """
        
        if not self.language in self.languages:
            raise ValueError(f"The language {self.language} is not on the available languages defined. Add this languages to the languages available.")
        
        for scene in self.scenes.values():
            if not os.path.exists(scene.background_display_img):
                raise ValueError(f"Image on Scene {self.scenes_names[scene.scene_number]} was not found. Check the Path.")
            
        self.validatePathing()
        
        game = _Game(self)
        
        game.run()




