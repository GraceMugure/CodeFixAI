import openai

def explain_code(code):
    prompt = f"Explain the following Python code line by line:\n\n{code}\n\n# Explanation:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()
