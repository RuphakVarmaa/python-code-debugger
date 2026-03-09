"""
Utility Helpers
Helper functions for the debugger - by Sabareeswar
"""


def format_code(code):
    lines = code.strip().splitlines()
    numbered = []
    for i, line in enumerate(lines, 1):
        numbered.append(f"{i}: {line}")
    return "\n".join(numbered)


def build_prompt(formatted_code):
    prompt = f"""Debug the following Python code.
Find any bugs, errors, or issues. Explain each problem and provide the corrected code.

```python
{formatted_code}
```

Respond with:
1. List of bugs found
2. Explanation of each bug
3. Corrected code"""
    return prompt
