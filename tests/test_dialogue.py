import unittest
import pygame
from vnengine.utils.dialogue import _Dialogue

class TestDialogue(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.dialogue = _Dialogue(100, 100, 200, 100, "Hello World", (255, 0, 0), pygame.font.Font(None, 18))

    def tearDown(self):
        pygame.quit()

    def test_init(self):
        self.assertEqual(self.dialogue.x, 100)
        self.assertEqual(self.dialogue.y, 100)
        self.assertEqual(self.dialogue.width, 200)
        self.assertEqual(self.dialogue.height, 100)
        self.assertEqual(self.dialogue.text, "Hello World")
        self.assertEqual(self.dialogue.color, (255, 0, 0))
        self.assertIsInstance(self.dialogue.font, pygame.font.Font)


if __name__ == '__main__':
    unittest.main()