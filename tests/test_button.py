import unittest
import pygame
from vnengine.utils.button import _Button

class TestButton(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.button = _Button(100, 100, "Test")

    def tearDown(self):
        pygame.quit()

    def test_init(self):
        self.assertEqual(self.button.x, 100)
        self.assertEqual(self.button.y, 100)
        self.assertEqual(self.button.text, "Test")
        self.assertEqual(self.button.default_color, (110, 110, 110))
        self.assertEqual(self.button.hover_color, (220, 220, 220))
        self.assertIsInstance(self.button.font, pygame.font.Font)
        self.assertEqual(self.button.scenario, 'menu')
        self.assertEqual(self.button.rect, (100, 100))

    def test_is_over(self):
        self.assertTrue(self.button.is_over((101, 101)))
        self.assertFalse(self.button.is_over((90, 90)))

if __name__ == '__main__':
    unittest.main()