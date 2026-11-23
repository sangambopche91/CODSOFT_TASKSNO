"""Basic tests for the CODSOFT rule-based chatbot."""

import unittest
from chatbot import RuleBasedChatbot


class TestRuleBasedChatbot(unittest.TestCase):
    def setUp(self):
        self.bot = RuleBasedChatbot()

    def test_greeting(self):
        self.assertIn(self.bot.get_response("Hello"), [
            "Hello! How can I help you today?",
            "Hi there! What would you like to talk about?",
            "Hey! How are you doing?"
        ])

    def test_python_rule(self):
        self.assertIn("programming language",
                      self.bot.get_response("Tell me about Python"))

    def test_unknown_input(self):
        self.assertIn("don't understand",
                      self.bot.get_response("Tell me about interplanetary travel"))

    def test_empty_input(self):
        self.assertIn("type something", self.bot.get_response("   "))

    def test_ai_rule(self):
        self.assertIn("Artificial Intelligence",
                      self.bot.get_response("What is artificial intelligence?"))


if __name__ == "__main__":
    unittest.main()
