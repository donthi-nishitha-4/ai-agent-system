# agent/agent.py
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from llm.ollama_llm import OllamaLLM
from tools.tools import TOOLS
from memory.memory import Memory
from config import MAX_STEPS


class Agent:
    def __init__(self, goal: str, llm=None, memory=None):
        self.goal = goal
        self.llm = llm if llm else OllamaLLM()
        self.memory = memory if memory else Memory()
        self.MAX_STEPS = MAX_STEPS

    def think(self) -> str:
        prompt = f"""
You are an AI agent.

STRICT RULES:
- NEVER answer the problem yourself
- ALWAYS use a tool if possible
- Use ONLY the tool names listed
- Respond in EXACT format only
- No explanations, no extra text

You may take multiple reasoning steps before finishing if required.

RESPONSE FORMAT (ONLY ONE):

FORMAT 1:
ACTION: <TOOL_NAME>
INPUT: <tool_input>

FORMAT 2:
ACTION: FINISH
ANSWER: <final answer>

AVAILABLE TOOLS:
{', '.join(TOOLS.keys())}

GOAL:
{self.goal}

PREVIOUS OBSERVATIONS:
{self.memory.get()}
"""
        return self.llm.generate(prompt).strip()

    def parse_and_act(self, response: str):
        response = response.strip()

        # FINISH response
        if response.startswith("ACTION: FINISH"):
            answer = response.split("ANSWER:", 1)[-1].strip()
            return "FINISH", answer

        # TOOL response
        for tool_name, tool_fn in TOOLS.items():
            if response.startswith(f"ACTION: {tool_name}"):
                tool_input = ""
                if "INPUT:" in response:
                    tool_input = response.split("INPUT:", 1)[-1].strip()

                try:
                    if tool_input or tool_name not in ["RANDOM_FACT", "RANDOM_JOKE", "CURRENT_TIME"]:
                        result = tool_fn(tool_input)
                    else:
                        result = tool_fn()
                except Exception as e:
                    result = f"Tool error: {e}"

                # Normalize result
                if "ACTION: FINISH ANSWER:" in result:
                    result = result.split("ACTION: FINISH ANSWER:", 1)[-1].strip()

                # Save observation
                self.memory.add(f"{tool_name}({tool_input}) → {result}")

                return "FINISH", result

        # Invalid response
        self.memory.add(f"Invalid response from model:\n{response}")
        return "ERROR", f"Invalid agent response:\n{response}"

    def run(self):
        final_result = None
        trace = []

        for step in range(1, self.MAX_STEPS + 1):
            # THINK
            response = self.think()

            # ACT + OBSERVE
            action, result = self.parse_and_act(response)

            trace.append({
                "step": step,
                "thought": response,
                "action": action,
                "result": result
            })

            if action in ["FINISH", "ERROR"]:
                final_result = result
                break

        if final_result is None:
            final_result = "❌ Agent stopped: max steps reached"

        return {
            "final_answer": final_result,
            "trace": trace
        }
