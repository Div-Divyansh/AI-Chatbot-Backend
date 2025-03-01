from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend communication

# Replace with your OpenAI API key
openai.api_key = "your-openai-api-key"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = get_ai_response(user_input)
    return jsonify({"response": response})

def get_ai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use GPT-3.5
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == '__main__':
    app.run(debug=True)
