from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Sample responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm just a bot, but I'm doing great!", "I'm good! How about you?"],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"],
    "default": ["I'm not sure how to respond to that.", "Can you rephrase your question?"]
}

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message", "").lower()

    # Check for a predefined response
    for key in responses:
        if key in user_message:
            bot_response = random.choice(responses[key])
            break
    else:
        bot_response = random.choice(responses["default"])

    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
