# Copilot Instructions for AI Agents

## Project Overview
This repository contains beginner-level Python exercises focused on mastering the `while` loop. Each task is implemented as a separate script (e.g., `task01.py`, `task02.py`, etc.). The exercises are described in detail in `README.md`.

## Key Patterns & Conventions
- Each task is a standalone Python script, named `task0X.py`.
- Tasks are simple, interactive console programs (e.g., number guessing, password check, calculator, etc.).
- User input is handled with `input()`, and program flow is controlled with `while` loops and conditionals.
- Use clear, Uzbek-language prompts and feedback for user interaction.
- No external dependencies are required except for the standard library (e.g., `random`).

## Example Patterns
- Random number generation: `from random import randint` and `randint(1, 20)`
- Loop structure:
  ```python
  while not found:
      guess = int(input("..."))
      # ...
  ```
- Input validation and feedback are handled inline, not as separate functions.

## Developer Workflow
- Run scripts directly: `python task01.py` (or `py task01.py` on Windows)
- No build or test automation is present; manual execution is expected.
- No external configuration or environment setup is required.

## Reference Files
- `README.md`: Contains the full description and requirements for each task.
- `task01.py` ... `task05.py`: Each file implements a single exercise as described in the README.

## Guidance for AI Agents
- When generating or editing code, follow the style and structure of existing `task0X.py` files.
- Use Uzbek for all user-facing messages.
- Do not introduce unnecessary abstractions or complexity; keep code simple and readable for beginners.
- If adding new tasks, increment the filename numerically and document the task in the README.
