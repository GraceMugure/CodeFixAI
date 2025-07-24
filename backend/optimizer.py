import openai

def optimize_code(code):
    prompt = f"Suggest improvements to make this Python code more efficient or readable:\n\n{code}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()
