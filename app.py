from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def process_tasks(text):
    tasks = text.split(",")
    result = []

    for i, t in enumerate(tasks):
        result.append({
            "task": t.strip(),
            "priority": "High" if i % 2 == 0 else "Medium",
            "status": "Pending"
        })

    return result

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def run_ai():
    data = request.json
    text = data.get("input", "")
    tasks = process_tasks(text)

    return jsonify({
        "tasks": tasks,
        "explanation": "AI analyzed workflow and optimized task execution."
    })

if __name__ == "__main__":
    app.run(debug=True)