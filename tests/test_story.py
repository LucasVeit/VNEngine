import unittest
from vnengine.story import Story

class TestStory(unittest.TestCase):
    def setUp(self):
        self.story = Story()

    def test_set_languages(self):
        languages = ['de', 'en', 'es', 'fr', 'pt']
        self.story.set_languages(languages)
        self.assertEqual(self.story.languages, languages)

    def test_set_initial_language(self):
        language = 'en'
        self.story.set_initial_language(language)
        self.assertEqual(self.story.language, language)

    def test_set_resolution(self):
        resolution = 'fullhd'
        self.story.set_resolution(resolution)
        self.assertEqual(self.story.resolution, resolution)

    def test_add_starting_background(self):
        image = "/path/to/starting_menu.jpg"
        self.story.add_starting_background(image)
        self.assertEqual(self.story.starting_background, image)

    def test_add_scene(self):
        scene_name = "Scene 1"
        character_text = "Hello, world!"
        image = "/path/to/scene1.jpg"
        self.story.add_scene(scene_name, character_text, image)
        self.assertIn(scene_name, self.story.scenes)
        self.assertEqual(self.story.scenes[scene_name].character_text, character_text)
        self.assertEqual(self.story.scenes[scene_name].background_display_img, image)

    def test_add_choice(self):
        current_scene_name = "Scene 1"
        choice_text = "Choose option A"
        go_to_scene = "Scene 2"
        self.story.add_scene(current_scene_name, "Hello, world!", "/path/to/scene1.jpg")
        self.story.add_scene(go_to_scene, "Hello, world!", "/path/to/scene2.jpg")
        self.story.add_choice(current_scene_name, choice_text, go_to_scene)
        self.assertIn(go_to_scene, self.story.scenes[current_scene_name].choices)
        self.assertEqual(self.story.scenes[current_scene_name].choices[go_to_scene].choice_text, choice_text)
        
    def test_validate_path(self):
        scene_name = "Scene 0"
        character_text = "Test!"
        image = "/path/to/scene0.jpg"
        self.story.add_scene(scene_name, character_text, image)
        
        scene_name = "Scene 1"
        character_text = "Hello, world!"
        image = "/path/to/scene1.jpg"
        self.story.add_scene(scene_name, character_text, image)
        
        self.story.add_choice("Scene 0", "test", "Scene 1")
        
        try:
            self.story.validatePathing()
        except Exception:
            self.fail("Should not throw exception")
    
    def test_validate_path_without_choice(self):
        scene_name = "Scene 0"
        character_text = "Test!"
        image = "/path/to/scene0.jpg"
        self.story.add_scene(scene_name, character_text, image)
        
        scene_name = "Scene 1"
        character_text = "Hello, world!"
        image = "/path/to/scene1.jpg"
        self.story.add_scene(scene_name, character_text, image)
        
        with self.assertWarns(Warning):
            self.story.validatePathing()
    
    def test_validate_path_invalid_scene(self):
        scene_name = "Scene 0"
        character_text = "Test!"
        image = "/path/to/scene0.jpg"
        self.story.add_scene(scene_name, character_text, image)
        
        self.story.add_choice("Scene 0", "test", "Scene 1")
        
        with self.assertRaises(Exception):
            self.story.validatePathing()
    
    def test_validate_run_invalid_images(self):
        scene_name = "Scene 0"
        character_text = "Test!"
        image = "/path/to/scene0.jpg"
        self.story.add_scene(scene_name, character_text, image)
        
        with self.assertRaises(Exception):
            self.story.run()
            
    def test_language_not_defined(self):
        languages = ['de', 'es']
        self.story.set_languages(languages)
        
        language = 'en'
        self.story.set_initial_language(language)
        self.assertEqual(self.story.language, language)
        
        with self.assertRaises(Exception):
            self.story.run()

if __name__ == '__main__':
    unittest.main()