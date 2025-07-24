# CodeFixAI

CodeFixAI is an AI-powered tool that automatically detects bugs, fixes them, explains the code, and suggests improvements.

## Features
- Bug fixing
- Code explanation
- Optimization suggestions

## Tech Stack
- Flask (Python)
- OpenAI API
- HTML/CSS (Frontend)

## Getting Started

1. Clone the repo:
   ```
   git clone https://github.com/yourusername/CodeFixAI.git
   ```

2. Install requirements:
   ```
   pip install -r requirements.txt
   ```

3. Add your OpenAI API key in `bug_fixer.py`.

4. Run the app:
   ```
   python app.py
   ```

5. Open `index.html` in browser.

## Sample Use

Paste this buggy code:
```python
def add(a, b):
    return a + b

print(add(5))
```

AI will suggest fix and explain the missing argument.
