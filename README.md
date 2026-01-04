 A lightweight Python AI agent system using:

📌 Overview
This project implements a custom AI Agent Framework from scratch using Python, Flask, and a local LLM (Ollama).
The framework demonstrates how an autonomous AI agent can interpret a goal, reason about it, invoke tools, and produce results without directly solving tasks itself.
The system follows a structured Think → Act → Finish agent loop and is designed to be extensible, explainable, and tool-driven, aligning with modern agent architectures used in industry.
This project is developed as part of the Intel Unnati Industrial Training Program – Problem Statement #2: Build-Your-Own AI Agent Framework.

🧠 Agent Architecture
The agent operates with a controlled reasoning loop:

User Goal
↓
[ THINK ] → LLM decides next action
↓
[ ACT ] → Invoke selected tool
↓
[ OBSERVE ] → Store result in memory
↓
[ FINISH ] → Return final answer

Key Design Principles:

* LLM does not solve tasks directly
* All computation is delegated to tools
* Agent reasoning is explicit and traceable
* Each component is modular and replaceable

🧩 Core Components
1️⃣ Agent (agent/agent.py)

* Orchestrates the Think → Act → Finish loop
* Generates structured prompts for the LLM
* Parses tool instructions safely
* Maintains step control using MAX_STEPS

2️⃣ Tool System (tools/tools.py)

* Tools are independent Python functions
* Registered via a centralized TOOLS dictionary
* Examples: Calculator, Calendar, GCD/LCM, Unit Conversion, Text Analysis
* Easy to extend by adding new tools

3️⃣ Memory (memory/memory.py)

* Stores agent observations between steps
* Allows context accumulation
* Demonstrates stateful agent behavior

4️⃣ LLM Interface (llm/ollama_llm.py)

* Uses Ollama for local inference
* Model-agnostic (Gemma, LLaMA, Mistral supported)
* Clean abstraction layer for future upgrades

5️⃣ Web Interface (app.py + templates/index.html)

* Flask backend
* Simple UI to submit goals
* Displays final result and reasoning trace
* Designed for clarity, not demo theatrics

📂 Project Structure
ai-agent-framework/
│
├── app.py
├── main.py
├── config.py
│
├── agent/
│   └── agent.py
│
├── tools/
│   └── tools.py
│
├── llm/
│   └── ollama_llm.py
│
├── memory/
│   └── memory.py
│
└── templates/
└── index.html

⚙️ Requirements

* Python 3.10+
* Flask
* Ollama (local LLM runtime)
* Supported models: llama, gemma, mistral

Install dependencies:

```
pip install flask
```

▶️ How to Run
🔹 Start Ollama

```
ollama run llama
```

🔹 CLI Mode

```
python main.py
```

Example inputs:

```
(25*4)/5
GCD 12 18
TEXT_ANALYSIS Hello World
```

🔹 Web UI Mode

```
python app.py
```

Open in browser:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

📊 Example Agent Behavior
Input Goal:
What day was 26-01-2024?

Agent Flow:

THINK → Choose CALENDAR tool
ACT → Pass date to tool
OBSERVE → Receive weekday
FINISH → Return answer

Output:
Friday

 *Extensibility & Future Work*

* Add multi-step planning agents
* Introduce confidence-based stopping
* Add retrieval-augmented tools (RAG)
* Integrate Intel OpenVINO inference
* Plug-in external APIs as tools

*Credits*

* Initial agent prompt patterns and architectural guidance assisted by ChatGPT
* Full implementation, integration, debugging, and customization completed by the developer.
 
**PDF Version Ready:** This document is fully formatted for direct PDF export.
