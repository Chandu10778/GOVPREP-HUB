const https = require('https');
const fs = require('fs');
const env = fs.readFileSync('.env', 'utf8').split('\n').reduce((acc, line) => {
  const trimmed = line.trim();
  if (!trimmed || trimmed.startsWith('#') || !trimmed.includes('=')) return acc;
  const [key, value] = trimmed.split('=', 2);
  acc[key.trim()] = value.trim();
  return acc;
}, {});
const key = env.GROQ_AI_API_KEY;
const data = JSON.stringify({
  model: 'llama3-8b-8192',
  messages: [{ role: 'user', content: 'Tell me about World War 1' }],
  temperature: 0.7,
  max_tokens: 200
});
const options = {
  hostname: 'api.groq.com',
  port: 443,
  path: '/openai/v1/chat/completions',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Content-Length': Buffer.byteLength(data),
    'Authorization': `Bearer ${key}`
  }
};
const req = https.request(options, (res) => {
  console.log('status', res.statusCode);
  res.on('data', (chunk) => process.stdout.write(chunk));
  res.on('end', () => console.log('\nend'));
});
req.on('error', (e) => console.error('error', e));
req.write(data);
req.end();
