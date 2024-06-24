Certainly! Below are the setup instructions, how to run the code, and an overview of how the code runs for the Interview Practice Chatbot project.

---

# Interview Practice Chatbot

## Overview
This project is designed to create a chatbot using OpenAI's GPT-3.5-turbo model to assist users in practicing interview questions. The chatbot can simulate interview scenarios by asking and answering common questions. Additionally, the project includes a feature to fetch random jokes from an external API to add a touch of humor to the practice sessions.

Key Features:
- **Interview Question Simulation:** Helps users practice by generating and responding to common interview questions.
- **Random Joke Fetcher:** Provides random jokes to keep the practice sessions engaging and fun.

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- OpenAI API key

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo/interview-practice-chatbot.git
   cd interview-practice-chatbot
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required libraries:**
   ```bash
   pip install openai requests
   ```

4. **Set up your OpenAI API key:**
   Create a file named `.env` in the root directory of your project and add your OpenAI API key:
   ```bash
   OPENAI_API_KEY=your-openai-api-key
   ```

### How to Run the Code

1. **Run the chatbot script:**
   ```bash
   python chatbot.py
   ```

### Example Usage
1. The chatbot will start and ask if you want to practice interview questions or hear a joke.
2. Follow the prompts to practice interview questions or get a random joke.

## Code Overview

### chatbot.py

This script sets up the Interview Practice Chatbot and handles user interaction.

#### Key Components:

1. **Imports and Configuration:** Load environment variables and configure the OpenAI API key.
2. **get_random_joke:** Fetches a random joke from an external API.
3. **generate_interview_question:** Uses OpenAI's GPT-3.5-turbo model to generate common interview questions and answers.
4. **Main interaction loop:** Handles user input to either practice interview questions or fetch jokes, and continues the loop until the user decides to exit.



---


