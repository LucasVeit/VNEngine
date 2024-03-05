import unittest
from vnengine.base.choice import _Choice

class TestChoice(unittest.TestCase):
    def test_init(self):
        choice_text = "Choose option A"
        choice = _Choice(choice_text)
        self.assertEqual(choice.choice_text, choice_text)

if __name__ == '__main__':
    unittest.main()