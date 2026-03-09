"""
Code Debugger Logic
Core debugging class - by Niventhara
"""

from api_client import call_openrouter
from utils import format_code, build_prompt


class CodeDebugger:
    def __init__(self, model="openai/gpt-3.5-turbo"):
        self.model = model

    def debug(self, code):
        formatted = format_code(code)
        prompt = build_prompt(formatted)
        result = call_openrouter(prompt, self.model)
        return self._format_output(result)

    def _format_output(self, result):
        output = []
        output.append("=" * 50)
        output.append("  DEBUGGER REPORT")
        output.append("=" * 50)
        output.append(result)
        output.append("=" * 50)
        return "\n".join(output)
