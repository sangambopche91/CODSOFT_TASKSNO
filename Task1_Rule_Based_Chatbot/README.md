# CODSOFT AI Internship - Task 1
## Rule-Based Chatbot

### Project Overview
This project is a simple command-line chatbot built with Python. It responds to user messages by matching words and phrases against predefined rules using `if`-style logic and regular expressions.

The chatbot does not use machine learning or an external AI model. Its responses are rule-based, which makes the conversation flow easy to understand and modify.

### Features
- Responds to common greetings.
- Introduces itself and explains its basic features.
- Answers simple questions about Python, Artificial Intelligence, and Machine Learning.
- Displays the current time and date.
- Responds to thank-you messages.
- Provides a fallback response when it cannot recognize an input.
- Ends the conversation when the user types `bye`, `exit`, or `quit`.
- Includes basic unit tests.

### Technologies Used
- Python 3
- `re` module for pattern matching
- `random` module for choosing between responses
- `datetime` module for date and time
- `unittest` for testing

All modules used are part of Python's standard library. No package installation is needed.

### Requirements
- Python 3.8 or newer

### How to Run
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python chatbot.py
```

On Windows, if `python` is not recognized, try:

```powershell
py chatbot.py
```

### Example Conversation

```text
CODSOFT RULE-BASED CHATBOT
Type 'help' for topics or 'bye' to end the chat.

You: Hello
Bot: Hello! How can I help you today?

You: What is Python?
Bot: Python is a popular programming language used in automation, web development, data science, and artificial intelligence.

You: What is AI?
Bot: Artificial Intelligence (AI) is the field of creating computer systems that can perform tasks that usually require human intelligence.

You: Bye
Bot: Goodbye! Have a great day.
```

### Run Tests
From the project folder, run:

```bash
python -m unittest -v
```

On Windows, you can also use:

```powershell
py -m unittest -v
```

### How It Works
1. The chatbot receives text from the user.
2. It converts the text to lowercase and removes extra whitespace.
3. It checks the message against predefined regular-expression patterns.
4. When a pattern matches, it returns the associated response.
5. If no pattern matches, it returns a fallback message.
6. The conversation continues until the user enters an exit phrase.

### Limitations
- It only understands the patterns and topics programmed into it.
- It does not learn from conversations.
- It may not understand differently worded questions.
- It is a beginner demonstration of rule-based conversation logic, not a production chatbot.

### Internship
CODSOFT Artificial Intelligence Internship - Task 1: Chatbot with Rule-Based Responses.
