import unittest
from vnengine.base.scene import _Scene

class TestScene(unittest.TestCase):
    def test_init(self):
        character_text = "Hello, world!"
        image = "/path/to/test.jpg"
        scene_number = 1
        scene = _Scene(character_text, image, scene_number)
        self.assertEqual(scene.character_text, character_text)
        self.assertEqual(scene.background_display_img, image)
        self.assertEqual(scene.scene_number, scene_number)
        self.assertEqual(scene.choices, {})

    def test_add_choice(self):
        character_text = "Hello, world!"
        image = "/path/to/test.jpg"
        scene_number = 1
        scene = _Scene(character_text, image, scene_number)

        choice_text = "Choose option A"
        go_to_scene = "Scene 2"
        scene.add_choice(choice_text, go_to_scene)

        self.assertEqual(len(scene.choices), 1)
        self.assertIn(go_to_scene, scene.choices)
        self.assertEqual(scene.choices[go_to_scene].choice_text, choice_text)

if __name__ == '__main__':
    unittest.main()