"""
Python Code Debugger using OpenRouter API
Main entry point - by Ruphak
"""

from debugger import CodeDebugger
import sys


def main():
    debugger = CodeDebugger()

    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        with open(file_path, "r") as f:
            code = f.read()
    else:
        print("Python Code Debugger (OpenRouter API)")
        print("=" * 40)
        print("Paste your Python code below (type 'END' on a new line to finish):\n")
        lines = []
        while True:
            line = input()
            if line.strip() == "END":
                break
            lines.append(line)
        code = "\n".join(lines)

    if not code.strip():
        print("No code provided.")
        return

    print("\nAnalyzing your code...\n")
    result = debugger.debug(code)
    print(result)


if __name__ == "__main__":
    main()
