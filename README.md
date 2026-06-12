# CodeAlpha Python Programming Internship

This repository contains my projects completed as part of the CodeAlpha Python Programming Internship.

## Task 1: Hangman Game

### Description

The Hangman Game is a simple word guessing game developed using Python. The player tries to guess a hidden word one letter at a time.

### Features

* Random word selection
* Limited number of attempts
* User-friendly console interface
* Displays win or lose message

### Technologies Used

* Python
* Random Module

---

## Task 2: Stock Portfolio Tracker

### Description

The Stock Portfolio Tracker is a Python project that calculates the total investment value of stocks owned by a user.

### Features

* Stores stock prices using a dictionary
* Accepts stock names and quantities as input
* Calculates stock investment value
* Displays total portfolio value
* Option to save results to a text file

### Technologies Used

* Python
* Dictionary
* File Handling

---

#CodeAlpha
# CodeAlpha Python Programming Internship

## Task 4: Basic Chatbot

### Project Description
This project is a simple chatbot developed using Python. The chatbot interacts with users by responding to predefined messages. It demonstrates the use of functions, loops, conditional statements, and user input handling in Python.

### Features
- Responds to user greetings.
- Answers simple questions.
- Ends the conversation when the user types "bye".
- Handles unknown inputs with a default response.

### Technologies Used
- Python

### Source Code

```python
def chatbot():
    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi!")
        elif user == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand.")

chatbot()
