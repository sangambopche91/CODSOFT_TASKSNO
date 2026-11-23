"""
CODSOFT AI Internship - Task 1
Rule-Based Chatbot

A beginner-friendly chatbot that matches user messages against predefined
patterns and returns suitable responses. No external libraries are required.
"""

import re
import random


class RuleBasedChatbot:
    """A simple chatbot using keyword and regular-expression rules."""

    def __init__(self):
        self.rules = [
            (
                r"\b(hello|hi|hey|good morning|good afternoon|good evening)\b",
                [
                    "Hello! How can I help you today?",
                    "Hi there! What would you like to talk about?",
                    "Hey! How are you doing?"
                ]
            ),
            (
                r"\b(your name|who are you|what are you)\b",
                ["I am CODSOFT Bot, a simple rule-based chatbot."]
            ),
            (
                r"\b(how are you|how's it going|how are things)\b",
                ["I'm doing well, thanks for asking! How can I help you?"]
            ),
            (
                r"\b(what can you do|help|your features)\b",
                [
                    "I can respond to greetings, answer basic questions, "
                    "tell you the time and date, and chat about a few common topics."
                ]
            ),
            (
                r"\b(time|current time)\b",
                [None]  # The response is generated dynamically.
            ),
            (
                r"\b(date|today's date|what day)\b",
                [None]  # The response is generated dynamically.
            ),
            (
                r"\b(python)\b",
                ["Python is a popular programming language used in automation, "
                 "web development, data science, and artificial intelligence."]
            ),
            (
                r"\b(artificial intelligence|what is ai|\bai\b)\b",
                ["Artificial Intelligence (AI) is the field of creating computer "
                 "systems that can perform tasks that usually require human intelligence."]
            ),
            (
                r"\b(machine learning|what is ml)\b",
                ["Machine Learning is a part of AI in which systems learn patterns "
                 "from data and use them to make predictions or decisions."]
            ),
            (
                r"\b(thank you|thanks|thank)\b",
                ["You're welcome!", "Happy to help!", "No problem."]
            ),
            (
                r"\b(bye|goodbye|see you|exit|quit)\b",
                ["Goodbye! Have a great day."]
            ),
        ]

    @staticmethod
    def normalize(text):
        """Convert input to lowercase and remove extra whitespace."""
        return re.sub(r"\s+", " ", text.strip().lower())

    def get_response(self, user_input):
        """Find the first matching rule and return its response."""
        message = self.normalize(user_input)

        if not message:
            return "Please type something so I can respond."

        for pattern, responses in self.rules:
            if re.search(pattern, message):
                if pattern == r"\b(time|current time)\b":
                    from datetime import datetime
                    return f"The current time is {datetime.now().strftime('%I:%M %p')}."
                if pattern == r"\b(date|today's date|what day)\b":
                    from datetime import datetime
                    return f"Today's date is {datetime.now().strftime('%d %B %Y')}."

                return random.choice(responses)

        return (
            "I'm sorry, I don't understand that yet. "
            "Try asking about Python, AI, machine learning, or type 'help'."
        )

    def start(self):
        """Run the chatbot conversation loop."""
        print("=" * 55)
        print("CODSOFT RULE-BASED CHATBOT")
        print("Type 'help' for topics or 'bye' to end the chat.")
        print("=" * 55)

        while True:
            try:
                user_input = input("\nYou: ")
            except (EOFError, KeyboardInterrupt):
                print("\nBot: Goodbye!")
                break

            response = self.get_response(user_input)
            print(f"Bot: {response}")

            if re.search(r"\b(bye|goodbye|see you|exit|quit)\b",
                         self.normalize(user_input)):
                break


if __name__ == "__main__":
    bot = RuleBasedChatbot()
    bot.start()
