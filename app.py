import os
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Quiz data
quiz = [
    {"question": "1. What is the capital of France?",
     "options": ["A) London", "B) Berlin", "C) Paris", "D) Rome"],
     "answer": "C"},
    {"question": "2. Which planet is known as the Red Planet?",
     "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
     "answer": "B"},
    {"question": "3. Who wrote 'Romeo and Juliet'?",
     "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Leo Tolstoy"],
     "answer": "B"},
    {"question": "4. Which gas do plants absorb during photosynthesis?",
     "options": ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Hydrogen"],
     "answer": "B"},
    {"question": "5. Which is the largest ocean on Earth?",
     "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
     "answer": "D"}
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quiz")
def get_quiz():
    return jsonify(quiz)

@app.route("/submit", methods=["POST"])
def submit():
    answers = request.json
    score = 0
    results = []  # Will store "Q1 - Correct" etc.

    for i, q in enumerate(quiz):
        if answers.get(f"q{i}") == q["answer"]:
            score += 1
            results.append(f"Q{i+1} - Correct")
        else:
            results.append(f"Q{i+1} - Incorrect")

    return jsonify({
        "score": score,
        "total": len(quiz),
        "results": results
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)    
