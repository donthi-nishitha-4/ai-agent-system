import requests
from llm.base import BaseLLM
from config import MODEL_NAME

class OllamaLLM(BaseLLM):
    def generate(self, prompt: str) -> str:
        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": MODEL_NAME,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=60
            )

            response.raise_for_status()
            data = response.json()
            return data.get("response", "").strip()

        except Exception as e:
            return f"ACTION: FINISH\nANSWER: Ollama API error: {e}"
