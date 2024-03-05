Welcome to VNEngine's documentation!
====================================

This is the main documentation file for VNEngine. It provides an overview of the engine and its usage.

Contents: 

- Introduction: Provides an introduction to VNEngine. 

- API Reference: Contains the API documentation for VNEngine. 

- Search: Allows you to search for specific topics within the documentation.

.. toctree::
   :maxdepth: 2
   :caption: Contents: 
   
Introduction
==================
VNEngine was created to help with the development of Visual Novels in Python. This API seeks to provide an easy way to develop Visual Novels.

Using the Story method of the API, the user can create a story with multiple Scenes, multiple Paths on each scene, have different languages possible to be set for the game and define the game resolution.

API Reference
==================
The Class of the API is on the story module. After having VNEngine installed, you only need to import

.. code-block:: Python

   from VNEngine import story

after that, you create a variable to be the story and you can use its methods from the variable

.. code-block:: Python

   story = story.Story()

Add Scenes
----------------
.. method:: def add_scene(self, scene_name: str, character_text: str, image: str) -> None:
   
   This method is used to add a new scene to the story in the VNEngine. A scene represents a specific moment or event in the story, and consists of a character speaking a text and an image displayed as the background.

   :param scene_name: The name of the scene. This should be a unique identifier for the scene.
   :type scene_name: str
   :param character_text: The text spoken by the character in the scene.
   :type character_text: str
   :param image: The path of the image displayed as the background of the scene.
   :type image: str
   :return: None
   :rtype: None

   Example:
      To add a new scene to the story, you can call the `add_scene` method like this:

      .. code-block:: python

         engine.add_scene("Scene1", "Hello, world!", "background.jpg")

   In this example, will be created a Scene1, with the dialogue text "Hello, world!" and the background image being the "background.jpg"

   Note:
      - The `scene_name` should be unique for each scene. If a scene with the same name already exists, it will be overwritten.
      - The `image` parameter should be a valid file path to an image file.

Add Choices
----------------
.. method:: add_choice(current_scene_name, choice_text, go_to_scene)

   This method adds a choice to a scene in the VNEngine. A choice represents an option that the player can select
   during gameplay. When the choice is selected, the game will transition to the specified scene.

   :param current_scene_name: The name of the scene that the choice will be added.
   :type current_scene_name: str
   :param choice_text: The text of the choice.
   :type choice_text: str
   :param go_to_scene: The name of the scene to go to when the choice is selected.
   :type go_to_scene: str
   :return: None
   :rtype: None

   Example:
      To add choices on a scene, you can call the `add_choice` method like this:

      .. code-block:: python

         engine.add_choice("scene1", "Go left", "scene2")
         engine.add_choice("scene1", "Go right", "scene3")

   In the above example, two choices are added to the "scene1". The first choice has the text "Go left" and will
   transition to "scene2" when selected. The second choice has the text "Go right" and will transition to "scene3"
   when selected. 
   
   Note:
      - Both scenes have also to be created in the script for the visual novel to work.
      - A scene can be unreachable, not having any choice leading to it. But a choice can't be for a scene that doesn't exist.

Set Resolution
----------------
.. method:: set_resolution(resolution: str) -> None

   This method sets the resolution of the story in the VNEngine. The resolution determines the display size and quality of the game.

   :param resolution: A string with the chosen resolution. Available options are 'hd', 'fullhd', and '4k'. 
   :type resolution: str 
   :return: None 
   :rtype: None

   Example:
      To define the resolution, you can call the `set_resolution` method like this:

      .. code-block:: python
         
         story.set_resolution('fullhd')

      In the above example, the resolution of the story is set to 'fullhd', which represents a high-definition resolution.

   Note:
      - The available resolution options are 'hd' (high-definition), 'fullhd' (full high-definition), and '4k' (ultra high-definition).
      - The resolution should be set before starting the game to ensure the desired display quality.

Set Menu image
----------------
   .. method:: add_starting_background(image: str) -> None

      This method adds the starting menu background image to the story.

      :param image: The path of the starting menu background image.
      :type image: str
      :return: None
      :rtype: None

      Example:
         To add the starting menu background image, you can call the `add_starting_background` method like this:

         .. code-block:: python

            story.add_starting_background('background.jpg')

      In the above example, the starting menu background image is set to 'background.jpg'.

      Note:
         - The `image` parameter should be a valid file path to an image file.


Set Language
----------------
.. method:: set_languages(self, languages: List[str]) -> None

      Defines all the possible languages to be selected from the Main Menu.

      :param languages: A list of language codes representing the possible game languages.
      :type languages: List[str]
      :return: None
      :rtype: None

      Example:
         To set the available languages, you can call the `set_languages` method like this:
            
            .. code-block:: python
               
               story.set_languages(['en', 'fr', 'es'])
            
      In the above example, the available languages for narration are set to English, French, and Spanish.
         
      Note:
         - The available language codes are 'de' (German), 'en' (English), 'es' (Spanish), 'fr' (French), and 'pt' (Portuguese).
         - The languages should be set on the Main Menu. The language can be changed during game.

.. method:: set_initial_language(self, language: str) -> None

      Defines the default language when opening the game.

      :param language: The language code representing the default language.
      :type languages: str
      :return: None
      :rtype: None

      Example:
         To set the default language, you can call the `set_language` method like this:
            
            .. code-block:: python
               
               story.set_language('en')
            
      In the above example, the default language will be 'en', which is English.
         
      Note:
         - The default language is the language in which the game opens everytime.