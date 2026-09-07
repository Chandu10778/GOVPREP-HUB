
from flask import Blueprint, jsonify, request
import json
import requests


def retry(max_attempts=3):
    # Remove retry logic for Mistral API simplicity
    def decorator(f):
        return f
    return decorator


chat = Blueprint('chat', __name__)

@retry(max_attempts=3)
def call_groq_api(question):
    """Call Mistral AI API to answer questions"""
    print(f"Processing question: {question[:100]}...")
    api_key = "cqfapVPeJNXgCqCrfkPEosduo24N7Pk0"
    url = "https://api.mistral.ai/v1/chat/completions"
    system_prompt = "You are ExamBot, an expert AI study assistant. Answer every question the user asks clearly and helpfully. You specialize in exam preparation for UPSC, JEE, NEET, and other competitive exams, but you should still respond to any general question with a useful answer. You provide: Clear explanations of complex concepts, Study tips and strategies, Connections between topics, Practice advice, Motivation and guidance. Keep responses focused, easy to understand, and use examples when helpful."
    payload = {
        "model": "mistral-medium",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        "temperature": 0.7,
        "max_tokens": 500
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    resp = requests.post(url, json=payload, headers=headers, timeout=30)
    print(f"Response status: {resp.status_code}")
    print("Response headers:", dict(resp.headers))
    if resp.status_code != 200:
        print(f"ERROR: Mistral API returned status {resp.status_code}")
        print(f"Response body: {resp.text}")
        raise Exception(f"Mistral API error: {resp.status_code} - {resp.text}")
    response_data = resp.json()
    print("Mistral API full response:", response_data)
    if 'choices' in response_data and len(response_data['choices']) > 0:
        answer = response_data['choices'][0]['message']['content'].strip()
        print("Generated answer:", answer[:100] + "..." if len(answer) > 100 else answer)
        return answer
    else:
        print("No choices in response, full data:", response_data)
        raise Exception(f"Invalid Mistral API response format: {response_data}")


# Chat endpoint
@chat.route('/chat', methods=['POST'])
def handle_chat():
    try:
        data = request.json
        
        if not data or ('question' not in data and 'message' not in data):
            return jsonify({'error': 'Missing question field'}), 400
        
        question = (data.get('question') or data.get('message') or '').strip()
        
        if not question:
            return jsonify({'error': 'Question cannot be empty'}), 400
        
        if len(question) > 2000:
            return jsonify({'error': 'Question is too long (max 2000 characters)'}), 400
        
        # Call the AI API
        answer = call_groq_api(question)
        
        return jsonify({
            'reply': answer,   # 👈 IMPORTANT CHANGE
            'status': 'success'
        }), 200
        
    except Exception as e:
        print(f"ERROR in handle_chat: {str(e)}")
        import traceback
        traceback.print_exc()
        fallback_reply = """🤖 ExamBot Demo Mode (AI temporarily unavailable)

Try these exam topics:
• Fundamental rights
• Monsoon system  
• Profit & loss
• UPSC Polity basics

Ask anything - I'll provide study guidance! 📚"""
        return jsonify({
            'reply': fallback_reply,
            'status': 'demo_fallback'
        }), 200
