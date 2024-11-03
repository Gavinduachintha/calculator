from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Endpoint to handle calculations
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        expression = data.get("expression", "")
        # Evaluate the mathematical expression safely
        result = eval(expression)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": "Invalid expression"})

if __name__ == '__main__':
    app.run(debug=True)
