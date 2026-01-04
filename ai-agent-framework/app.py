from flask import Flask, request, jsonify, render_template
from agent.agent import Agent
from llm.ollama_llm import OllamaLLM
from memory.memory import Memory

app = Flask(__name__)

# Serve frontend
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# Run agent (non-streaming, stable)
@app.route("/run", methods=["POST"])
def run_agent():
    try:
        data = request.get_json(force=True)
        goal = data.get("goal", "").strip()

        if not goal:
            return jsonify({"error": "Goal is required"}), 400

        # Initialize agent
        llm = OllamaLLM()
        memory = Memory()
        agent = Agent(goal=goal, llm=llm, memory=memory)

        # Run agent
        result = agent.run()
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
