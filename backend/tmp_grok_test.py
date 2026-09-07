import json
import urllib.request
import urllib.error
from pathlib import Path

env = {}
for line in Path('.env').read_text().splitlines():
    if line.strip() and not line.strip().startswith('#') and '=' in line:
        key, value = line.split('=', 1)
        env[key.strip()] = value.strip().strip('"').strip("'")

print('Loaded keys:', list(env.keys()))
key = env.get('GROQ_AI_API_KEY')
url = env.get('GROQ_AI_API_URL', 'https://api.groq.com/openai/v1/chat/completions')
print('URL:', url)
print('Key length:', len(key) if key else None)

payload = json.dumps({
    'model': 'llama3-8b-8192',
    'messages': [
        {'role': 'user', 'content': 'Tell me about World War 1'}
    ],
    'temperature': 0.7,
    'max_tokens': 200,
}).encode('utf-8')

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {key}'
}

req = urllib.request.Request(url, data=payload, headers=headers, method='POST')
try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        text = resp.read().decode('utf-8')
        print('Response:', text)
except urllib.error.HTTPError as e:
    print('HTTP Error', e.code)
    print(e.read().decode('utf-8'))
except Exception as e:
    print('Error', repr(e))
