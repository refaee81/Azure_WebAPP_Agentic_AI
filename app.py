import os  
import requests  
from flask import Flask, render_template, request, jsonify  
  
app = Flask(__name__)  
  
# Databricks endpoint details  
DATABRICKS_ENDPOINT = "https://adb-2717xxxxxxxxxxxxxxxx8877.17.azuredatabricks.net/serving-endpoints/agents_mxxxxxxxxx_chatbot/invocations"  
# DATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')  # Set this securely in your environment  
DATABRICKS_TOKEN = 'dapxxxxxxxxxxxxxxxxxxxxx9'  
  
@app.route('/')  
def index():  
    return render_template('index.html')  
  
@app.route('/chat', methods=['POST'])  
def chat():  
    user_message = request.json.get('message')  
    if not user_message:  
        return jsonify({"error": "No message provided"}), 400  
  
    headers = {  
        "Authorization": f"Bearer {DATABRICKS_TOKEN}",  
        "Content-Type": "application/json"  
    }  
    payload = {  
        "messages": [  
            {"role": "user", "content": user_message}  
        ]  
    }  
  
    try:  
        response = requests.post(DATABRICKS_ENDPOINT, headers=headers, json=payload)  
        response.raise_for_status()  
        data = response.json()  
        # Extract the assistant's reply according to the OpenAI-compatible chat response structure  
        answer = data.get('choices', [{}])[0].get('message', {}).get('content', 'No answer found.')  
        return jsonify({'answer': answer})  
    except Exception as e:  
        return jsonify({'error': str(e)}), 500  
  
if __name__ == '__main__':  
    app.run(debug=True)  