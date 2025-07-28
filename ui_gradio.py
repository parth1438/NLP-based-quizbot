import gradio as gr
import json
from fuzzywuzzy import fuzz

# Load questions
with open('questions.json') as f:
    questions = json.load(f)

# Unique topics
topics = sorted(list(set(q['topic'] for q in questions)))

# State to track quiz progress
state = {
    "index": 0,
    "score": 0,
    "filtered_questions": [],
    "topic": ""
}

# Start quiz
def start_quiz(selected_topic):
    state["index"] = 0
    state["score"] = 0
    state["topic"] = selected_topic
    state["filtered_questions"] = [q for q in questions if q["topic"].lower() == selected_topic.lower()]

    if not state["filtered_questions"]:
        return "⚠️ No questions found for this topic.", "", ""

    first_question = state["filtered_questions"][0]["question"]
    return f"🧠 {first_question}", "", ""

# Submit an answer
def submit_answer(user_answer):
    q = state["filtered_questions"][state["index"]]
    correct = q["answer"]
    feedback = ""

    if fuzz.partial_ratio(user_answer.lower(), correct.lower()) >= 80:
        feedback += "✅ Correct!\n"
        state["score"] += 1
    else:
        feedback += f"❌ Wrong! The correct answer was: {correct}\n"

    state["index"] += 1

    if state["index"] < len(state["filtered_questions"]):
        next_q = state["filtered_questions"][state["index"]]
        return f"🧠 {next_q['question']}", "", feedback
    else:
        final = f"\n🎉 Quiz Over! Your final score: {state['score']}/{len(state['filtered_questions'])}"
        return "", "", feedback + final

# Reset quiz
def reset_quiz():
    state["index"] = 0
    state["score"] = 0
    state["filtered_questions"] = []
    state["topic"] = ""
    return "", "", "", gr.update(value=None)

# UI
with gr.Blocks() as demo:
    gr.Markdown("## 🧠 NLP Quiz Bot")

    topic_dropdown = gr.Dropdown(choices=topics, label="Select a topic")
    start_button = gr.Button("Start Quiz")

    question_text = gr.Textbox(label="Question", interactive=False, lines=2)
    answer_input = gr.Textbox(label="Type your answer here")
    submit_button = gr.Button("Submit Answer")

    feedback_box = gr.Textbox(label="Feedback", interactive=False, lines=4)
    reset_button = gr.Button("🔄 Reset Quiz")

    start_button.click(start_quiz, inputs=topic_dropdown, outputs=[question_text, answer_input, feedback_box])
    submit_button.click(submit_answer, inputs=answer_input, outputs=[question_text, answer_input, feedback_box])
    reset_button.click(reset_quiz, outputs=[question_text, answer_input, feedback_box, topic_dropdown])

demo.launch()
