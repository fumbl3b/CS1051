import unittest
from hawaii import validate_characters

class TestValidateCharacters(unittest.TestCase):

    def test_invalid_word(self):
        self.assertFalse(validate_characters("invalid"), "Expected 'invalid' to be False")

    def test_valid_aloha(self):
        self.assertTrue(validate_characters("aloha"), "Expected 'aloha' to be True")

    def test_valid_hawaiian_word(self):
        self.assertTrue(validate_characters("humuhumunukunukuapua'a"), "Expected 'humuhumunukunukuapua'a' to be True")

if __name__ == "__main__":
    unittest.main()
