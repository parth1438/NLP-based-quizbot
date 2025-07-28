from fuzzywuzzy import fuzz  
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')


# Load questions from file
with open('questions.json') as f:
    questions = json.load(f)

score = 0

print("👋 Welcome to the Quiz Bot!\n")

# Get list of topics
topics = list(set(q['topic'] for q in questions))
print("📚 Available topics:", ", ".join(topics))

# Ask user to select a topic
selected = input("📝 Enter a topic: ").strip()

# Filter questions
filtered_questions = [q for q in questions if q['topic'].lower() == selected.lower()]

if not filtered_questions:
    print("⚠️ No questions found for this topic.")
    exit()

# Use filtered_questions instead of questions


for q in filtered_questions:
    print(f"\n🧠 {q['question']}")
    for idx, option in enumerate(q['options']):
        print(f"{idx + 1}. {option}")


    # inside your loop, replace old matching logic with:
    ans = input("Your answer: ").strip()

    # Fuzzy string match
    if fuzz.partial_ratio(ans.lower(), q['answer'].lower()) >= 80:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer: {q['answer']}")


print(f"\n🎉 Your final score: {score}/{len(filtered_questions)}")
print("Thank you for playing! 👋")