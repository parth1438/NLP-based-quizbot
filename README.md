🧠 NLP Quiz Bot
This project provides a simple yet engaging Quiz Bot that tests your knowledge across various topics. It comes with two interfaces: a command-line interface (CLI) for quick interaction and a web-based interface built with Gradio for a more user-friendly experience. The bot uses fuzzy string matching to evaluate answers, making it more forgiving to minor typos.
✨ Features
Topic Selection: Choose from a variety of predefined quiz topics.
Fuzzy Matching: Answers are evaluated using fuzzy string matching (powered by fuzzywuzzy), allowing for slight variations or typos in user input.
Interactive CLI: A straightforward command-line interface for playing the quiz.
Gradio Web UI: A user-friendly web interface for a more interactive experience.
Extensible Questions: Easily add new questions and topics by modifying the questions.json file.
📁 Project Structure
main.py: The Python script for the command-line interface (CLI) version of the Quiz Bot.
ui_gradio.py: The Python script for the web-based interface using Gradio.
questions.json: A JSON file containing all the quiz questions, answers, options, and topics.
🚀 Getting Started
Prerequisites
Before running the Quiz Bot, you need to have Python installed on your system. This project also requires a few Python libraries.
Python 3.x:
Make sure you have Python 3.x installed. You can download it from python.org.
Install Dependencies:
You'll need fuzzywuzzy and gradio. You can install them using pip:
pip install fuzzywuzzy python-Levenshtein gradio

Note: python-Levenshtein is an optional but highly recommended dependency for fuzzywuzzy for better performance.
Setup
Clone the repository (or download the files):
If you have Git, you can clone the repository:
git clone <repository_url>
cd <repository_directory>

Otherwise, download main.py, ui_gradio.py, and questions.json into the same directory.
questions.json:
Ensure the questions.json file is in the same directory as your Python scripts. This file contains the quiz data. You can customize it to add more questions or topics.
Example structure for questions.json:
[
  {
    "question": "What is the capital of France?",
    "answer": "Paris",
    "options": ["London", "Berlin", "Paris", "Rome"],
    "topic": "Geography"
  },
  {
    "question": "Who painted the Mona Lisa?",
    "answer": "Leonardo da Vinci",
    "options": ["Vincent Van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"],
    "topic": "Art & Culture"
  }
]


🎮 How to Play
You have two options to run the Quiz Bot:
1. Command-Line Interface (CLI)
To run the CLI version, execute main.py:
python main.py


Follow the prompts in your terminal:
The bot will greet you and list available topics.
Enter your desired topic.
Answer the questions one by one.
Receive instant feedback (correct/wrong) and the correct answer if you were wrong.
Your final score will be displayed at the end.
2. Web Interface (Gradio)
To run the web-based interface, execute ui_gradio.py:
python ui_gradio.py


This will start a Gradio application, and a local URL (e.g., http://127.0.0.1:7860/) will be displayed in your terminal. Open this URL in your web browser.
On the web interface:
Select a topic from the dropdown menu.
Click "Start Quiz".
Type your answer in the input box and click "Submit Answer".
Feedback will appear in the feedback box.
Click "🔄 Reset Quiz" to start a new game.
📝 Customization
Add/Edit Questions: Open questions.json and add new question objects following the existing format. Ensure each question has a question, answer, options (an array of strings), and topic.
Adjust Fuzzy Matching Sensitivity: In both main.py and ui_gradio.py, the fuzz.partial_ratio threshold is set to 80. You can adjust this value (e.g., 70 for more leniency, 90 for stricter matching) if needed.
🤝 Contributing
Feel free to fork this project, suggest improvements, or add more features!
📄 License
This project is open-source and available under the MIT License.
