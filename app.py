from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# List of valid flags (these are placeholder flags)
VALID_FLAGS = ["CTF{lunar_codebreaker}", "Codeintheschools", "CTF{DarkNetSpecter}"]

@app.route('/')
def home():
    return render_template('index.html')  # Renders the main HTML page

@app.route('/submit_flag', methods=['POST'])
def check_flag():
    user_flag = request.json.get('flag')

    # Check if the submitted flag is in the list of valid flags
    if user_flag in VALID_FLAGS:
        return jsonify({"message": "Correct! Flag is valid!"}), 200
    else:
        return jsonify({"message": "Incorrect flag. Please try again."}), 400

if __name__ == "__main__":
    app.run(debug=True)
