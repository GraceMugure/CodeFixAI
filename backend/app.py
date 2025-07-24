from flask import Flask, request, jsonify
from bug_fixer import fix_code
from code_explainer import explain_code
from optimizer import optimize_code

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_code():
    data = request.get_json()
    code = data.get("code")

    fixed_code = fix_code(code)
    explanation = explain_code(code)
    optimization = optimize_code(code)

    return jsonify({
        "original_code": code,
        "fixed_code": fixed_code,
        "explanation": explanation,
        "optimization": optimization
    })

if __name__ == '__main__':
    app.run(debug=True)
