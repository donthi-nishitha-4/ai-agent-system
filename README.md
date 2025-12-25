//AI Agent Framework//
This project is a lightweight AI Agent Framework built in Python using Flask, Ollama, and a tool-based agent design. The agent interprets user goals, selects the appropriate tool, and produces results without directly solving tasks on its own.
It demonstrates how to build an AI agent from scratch using a Think → Act → Finish loop, tool routing, memory handling, and a local LLM backend. The base structure and prompt logic were developed with guidance from ChatGPT and then customized and extended by the developer.

Features:
Think → Act → Finish reasoning loop
Multiple tools including calculator, GCD, LCM, random joke, random fact, unit conversion, and more
Local LLM inference using Ollama
Flask backend with a simple HTML interface
Extensible tool architecture
Basic memory support

Project Structure:
ai-agent-framework
app.py, main.py, config.py
agent/, llm/, tools/, memory/, templates/

Requirements:
Python 3.10+
Ollama with a model such as gemma, llama, or mistral
Flask

How to Run (CLI):
Start Ollama
ollama run gemma

Run the agent:
python main.py

Example inputs:
(25*4)/5
GCD 12 18
RANDOM_FACT

How to Run (Web UI):
Start Ollama
ollama run gemma

Run Flask:
python app.py

Open:
http://127.0.0.1:5000

Notes:
Ollama must be running before execution
GitHub Pages cannot host the Flask backend
Timeout errors usually indicate Ollama is slow or not running

Credits:
The base agent architecture and prompt design were developed with the assistance of ChatGPT. The final implementation and integrations were completed and customized by me.
