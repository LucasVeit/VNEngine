import pygame
from vnengine.utils.button import _Button
from vnengine.utils.dialogue import _Dialogue
from googletrans import Translator
import os

__all__ = []
class _Game:
    """
    Represents the game instance for the visual novel engine. Is the class responsible for the interaction with the pygame and running the game loop.

    Attributes:
        story (Story): The story object containing the game's narrative.
        languages (List[str]): The list of available languages in the game.
        language (str): The current chosen language of the game.
        resolution (Dict[str, Tuple[int, int]]): The available screen resolutions.
        languages_names (Dict[str, str]): The keyword for the translation tool and the original name of the language.
        translator (Translator): The translator object for language translation.
        FPS (int): The frames per second for the game.
        side_bar_x (int): The initial width of the side bar on the screen.
        side_bar_y (int): The initial height of the side bar on the screen.
        font (Font): The font object for text rendering.
        screen (Surface): The game screen surface.
        buttons (List[_Button]): The list of buttons in the game.
        scene_buttons (List[_Button]): The list of buttons available in the scenes.
        scenes_stack (List[int]): The stack of visited scenes in the game.
        rescale_image_menu (Tuple[int, int]): The scaled size of the menu background image.
        rescale_image_game (Tuple[int, int]): The scaled size of the game background image.
    """

    def __init__(self, story):
        """
        Initializes a new instance of the _Game class.

        Args:
            story (Story): The story object containing the game's narrative.
        """
        self.story = story
        self.languages = story.languages
        self.language = story.language
        self.resolution = {'hd': (1280, 720), 'fullhd': (1920, 1080), '4k': (3840, 2160)}
        self.languages_names = {'pt': 'Português', 'en': 'Inglês', 'fr': 'Francês', 'es': 'Espanhol', 'de': 'Alemão'}
        self.translator = Translator()
        
        pygame.init()
        
        # Constants
        self.res_chosen = story.resolution
        self.FPS = 60
        
        self.side_bar_x = self.resolution[self.res_chosen][0] // 5
        self.side_bar_y = self.resolution[self.res_chosen][1] // 4
        
        font_size = 32
        
        self.font = pygame.font.Font(None, font_size)
    
        # Screen
        self.screen = pygame.display.set_mode(self.resolution[self.res_chosen], pygame.FULLSCREEN)
        
        # Utils
        self.buttons = []
        
        self.scene_buttons = []
        
        self.scenes_stack = []
        
        self.scenarios = {'game': self.game_display, 'choice': self.choice_display, 'start': self.menu_display, 'language': self.language_display}
    
        infoObject = pygame.display.Info()
        screen_width = infoObject.current_w
        screen_height = infoObject.current_h
        
        self.rescale_image_menu = (screen_width - self.side_bar_x, screen_height)
        self.rescale_image_game = (screen_width, screen_height - self.side_bar_y)
        
    def load_scenes_stack(self) -> None:
        """
        Load the scenes stack from the 'save.txt' file.

        The scenes stack is a list of integers representing the scenes that have been visited in the game.
        Each integer corresponds to a specific scene.

        Args:
            None

        Returns:
            None
        """
        with open("save.txt", "r") as file:
            scenes_list_str = file.read().strip('[]').split(', ')
            self.scenes_stack = [int(scene) for scene in scenes_list_str]
    
    def checkButtonsColor(self, pos) -> None:
        """
        Checks the color of the buttons based on the given position. Used to highlight the button that the mouse is over.

        Args:
            pos (tuple): The position of the mouse cursor.

        Returns:
            None
        """
        for button in self.buttons:
            if button.is_over(pos):
                button.color = button.hover_color
            else:
                button.color = button.default_color
            
            button.draw(self.screen)
            
    def create_scene_buttons(self) -> None:  
        """
        Creates the buttons available in the scenes.

        Args:
            None

        Returns:
            None
        """
        self.scene_buttons = []
        starter_value = 50         
        y_position = self.resolution[self.res_chosen][1] - (self.font.size('')[1] + 10)
        
        self.scene_buttons.append(_Button((self.resolution[self.res_chosen][0] // 2) - 50, y_position, self.translator.translate('Menu', src='pt', dest=self.language).text, font = self.font, color=(150, 150, 150), hover_color=(220, 220, 220)))
        starter_value += 50
        self.scene_buttons.append(_Button((self.resolution[self.res_chosen][0] // 2) + 50, y_position, self.translator.translate('Voltar Cena', src='pt', dest=self.language).text, font = self.font, color=(150, 150, 150), hover_color=(220, 220, 220)))
             
    def starting_menu(self) -> None:     
        """
        Displays the starting menu of the game with buttons for starting a new game, continuing a game,
        changing the language, and closing the game.

        Args:
            None

        Returns:
            None
        """
        self.buttons = []   
        starter_value = 150
        self.buttons.append(_Button(25, starter_value, self.translator.translate('Iniciar Jogo', src='pt', dest=self.language).text, font = self.font))
        starter_value += 50
        self.buttons.append(_Button(25, starter_value, self.translator.translate('Continuar Jogo', src='pt', dest=self.language).text, font = self.font))
        starter_value += 50
        self.buttons.append(_Button(25, starter_value, self.translator.translate('Idioma', src='pt', dest=self.language).text, font = self.font))
        starter_value += 50
        self.buttons.append(_Button(25, starter_value, self.translator.translate('Fechar Jogo', src='pt', dest=self.language).text, font = self.font))
        
        background = pygame.image.load(self.story.starting_background).convert()
        self.background = pygame.transform.scale(background, self.rescale_image_menu)
    
    def starting_scene(self) -> None:
        """
        Initializes the current scene of the game.

        This method sets the text, background image, and scene buttons.

        Args:
            None

        Returns:
            None
        """
        self.text = _Dialogue(50, (self.resolution[self.res_chosen][1] - self.side_bar_y) + 25, 200, 200,  self.translator.translate(self.story.scenes[self.current_scene].character_text, src='pt', dest=self.language).text)
        
        background = pygame.image.load(self.story.scenes[self.current_scene].background_display_img).convert()
        self.background = pygame.transform.scale(background, self.rescale_image_game)
        
        self.create_scene_buttons()

    def starting_choice(self) -> None:
        """
        Creates buttons for the available choices on the current scene in the game.

        Args:
            None

        Returns:
            None
        """
        starter_value: int = 100
        self.buttons = []
        for choice in self.story.scenes[self.current_scene].choices.values():
            self.buttons.append(_Button((self.resolution[self.res_chosen][0]//2), starter_value, self.translator.translate(choice.choice_text, src='pt', dest=self.language).text, font = self.font, scenario = 'choice'))
            starter_value += 50
            
    def starting_language(self) -> None:
        """
        Initializes the language screen buttons.

        This method creates buttons for each language in the `languages` list.

        Args:
            None

        Returns:
            None
        """
        starter_value = 100
        self.buttons = []
        
        for language in self.languages:
            self.buttons.append(_Button(25, starter_value, self.translator.translate(self.languages_names[language], src='pt', dest=language).text, font = self.font))
            starter_value += 50


    def draw_menu(self) -> None:
        """
        Draws the menu on the screen.

        Args:
            None

        Returns:
            None
        """
        self.screen.fill((20, 20, 20)) 
        self.screen.blit(self.background, (self.side_bar_x, 0))
        
        for button in self.buttons:
            button.draw(self.screen)
            
    def draw_scene(self) -> None:
        """
        Draws the current scene on the screen.

        This method draws the background image, scene title, character text and buttons on the screen.

        Args:
            None

        Returns:
            None
        """
        self.screen.fill((20, 20, 20)) 
        self.screen.blit(self.background, (0, 0))
                
        self.text.draw(self.screen)

        scene_title = self.current_scene
        title_font = pygame.font.Font(None, 48)
        if self.background.get_at((0, 0)) == (255, 255, 255) or sum(self.background.get_at((self.resolution[self.res_chosen][0] // 2, 25))) > 600:
            title_text = title_font.render(scene_title, True, (0, 0, 0))
        else:
            title_text = title_font.render(scene_title, True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(self.resolution[self.res_chosen][0] // 2, 25))
        self.screen.blit(title_text, title_rect)
        
        for button in self.scene_buttons:
            button.draw(self.screen)
        
    def draw_choice(self) -> None:
        """
        Draws the available choices on the game screen.

        Args:
            None

        Returns:
            None
        """
        self.screen.fill((20, 20, 20)) 
        self.screen.blit(self.background, (0, 0))
        
        for button in self.buttons:
            button.draw(self.screen)
                
        for button in self.scene_buttons:
            button.draw(self.screen)
            
        self.text.draw(self.screen)

        scene_title = self.current_scene
        title_font = pygame.font.Font(None, 48)
        if self.background.get_at((0, 0)) == (255, 255, 255) or sum(self.background.get_at((self.resolution[self.res_chosen][0] // 2, 25))) > 600:
            title_text = title_font.render(scene_title, True, (0, 0, 0))
        else:
            title_text = title_font.render(scene_title, True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(self.resolution[self.res_chosen][0] // 2, 25))
        self.screen.blit(title_text, title_rect)
        
    def draw_languages(self) -> None:
        """
        Draws the languages buttons on the screen.

        Args:
            None

        Returns:
            None
        """
        self.screen.fill((20, 20, 20)) 
        self.screen.blit(self.background, (self.side_bar_x, 0))
        
        for button in self.buttons:
            button.draw(self.screen)
        
    def menu_display(self, event) -> None:
        """
        Runs the loop display of the menu and handle user input events.

        Args:
            event (pygame.event.Event): The event object representing the user input event.

        Returns:
            None
        """
        self.draw_menu()
        
        pos = pygame.mouse.get_pos()
            
        if event.type == pygame.MOUSEMOTION:
            self.checkButtonsColor(pos)
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            for idx, button in enumerate(self.buttons):
                if button.is_over(pos):
                    # start game
                    if idx == 0:
                        self.scene = 'game'
                        self.scenes_stack = [0]
                        with open("save.txt", "w") as file:
                            file.write(str(self.scenes_stack))
                            
                        self.current_scene = self.story.scenes_names[self.scenes_stack[-1]]
                        self.starting_scene()
                        self.draw_scene()
                    # continue game
                    elif idx == 1:
                        self.scene = 'game'
                        self.load_scenes_stack()
                        self.current_scene = self.story.scenes_names[self.scenes_stack[-1]]
                        self.starting_scene()
                        self.draw_scene()
                    # choose language
                    elif idx == 2:
                        self.scene = 'language'
                        self.starting_language()
                        self.draw_languages()
                    elif idx == 3:
                        self.running = False
                        
    def game_display(self, event) -> None:
        """
        Runs the loop display of the game scene for the current scene and handle user input.

        Args:
            event (pygame.event.Event): The event triggering the display.

        Returns:
            None
        """
        self.draw_scene()

        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            b = False
            for idx, button in enumerate(self.scene_buttons):
                if button.is_over(pos):
                    if idx == 0:
                        self.scene = 'start'
                        self.starting_menu()
                        self.draw_menu()
                    elif idx == 1:
                        if len(self.scenes_stack) > 1:
                            self.scenes_stack.pop()
                            self.current_scene = self.story.scenes_names[self.scenes_stack[-1]]

                            with open("save.txt", "w") as file:
                                file.write(str(self.scenes_stack))

                        self.starting_scene()
                        self.draw_scene()
                    b = True
            if not b:
                self.scene = 'choice'
                self.starting_choice()
                self.draw_choice()
                                
    def choice_display(self, event: pygame.event.Event) -> None:
        """
        Runs the loop display of the choices for the current scene and handle user input.

        Args:
            event (pygame.event.Event): The event object representing the user's input.

        Returns:
            None
        """
        self.draw_choice()
        pos = pygame.mouse.get_pos()
                    
        if event.type == pygame.MOUSEMOTION:
            self.checkButtonsColor(pos)
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            for idx, button in enumerate(self.buttons):
                if button.is_over(pos):
                    self.scene = 'game'
                    self.current_scene = list(self.story.scenes[self.current_scene].choices.keys())[idx]
                    self.scenes_stack.append(self.story.scenes_names.index(self.current_scene))
                        
                    with open("save.txt", "w") as file:
                        file.write(str(self.scenes_stack))
                            
                    self.starting_scene()
                    self.draw_scene()
                
            for idx, button in enumerate(self.scene_buttons):
                if button.is_over(pos):
                    if idx == 0:
                        self.scene = 'start'
                        self.starting_menu()
                        self.draw_menu()
                    elif idx == 1:
                        self.scene = 'game'
                        if len(self.scenes_stack) > 1: 
                            self.scenes_stack.pop()
                            self.current_scene = self.story.scenes_names[self.scenes_stack[-1]]    
                                
                            with open("save.txt", "w") as file:
                                file.write(str(self.scenes_stack))  
                        
                        self.starting_scene()
                        self.draw_scene()
                        
    def language_display(self, event: pygame.event.Event) -> None:
        """
        Runs the loop display of the language selection screen and handles user input.

        Args:
            event (pygame.event.Event): The event object representing the user's input.

        Returns:
            None
        """
        self.draw_languages()
        pos = pygame.mouse.get_pos()
                    
        if event.type == pygame.MOUSEMOTION:
            self.checkButtonsColor(pos)
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            for idx, button in enumerate(self.buttons):
                if button.is_over(pos):
                    self.language = self.languages[idx]
                    
                    self.scene = 'start'
                    self.starting_menu()
                    self.draw_menu
                                
    def run(self) -> None:
        """
        Runs the game loop and handles events.

        This method starts the game loop, which continuously checks for events and updates the game state accordingly.
        It also handles the rendering of the game screen.

        Returns:
            None
        """
        self.starting_menu()
        self.draw_menu()
        
        clock = pygame.time.Clock()
        self.scene = 'start'
        
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                self.scenarios[self.scene](event)
                    
            # pygame.display.flip()
            pygame.display.update()
            clock.tick(self.FPS)
