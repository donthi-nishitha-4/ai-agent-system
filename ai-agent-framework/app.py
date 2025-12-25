from flask import Flask, request, jsonify, render_template
from agent.agent import Agent
from llm.ollama_llm import OllamaLLM
from memory.memory import Memory

app = Flask(__name__)

# Serve the frontend
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# Run the agent via POST
@app.route("/run", methods=["POST"])
def run_agent():
    try:
        data = request.get_json(force=True)
        if not data or "goal" not in data:
            return jsonify({"error": "Missing 'goal' field"}), 400

        goal = data["goal"].strip()
        if not goal:
            return jsonify({"error": "Empty goal"}), 400

        # Create LLM and memory instances
        llm = OllamaLLM()
        memory = Memory()

        # Initialize agent with LLM, memory, and goal
        agent = Agent(goal=goal, llm=llm, memory=memory)
        result = agent.run()

        return jsonify({"result": result})

    except Exception as e:
        # Catch any server-side errors
        return jsonify({"error": f"Server error: {str(e)}"}), 500


if __name__ == "__main__":
    # Run Flask app
    app.run(debug=True)
