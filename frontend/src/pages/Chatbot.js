import React, { useState, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { MessageCircle, Send, Loader } from 'lucide-react';
import { Card, Button, ChatBubble, TextInput } from '../components';
import { toast } from 'react-toastify';

const API_BASE = process.env.REACT_APP_API_URL || 'http://127.0.0.1:5000';

export default function Chatbot({ user }) {
  const navigate = useNavigate();
  const [messages, setMessages] = useState([
    {
      id: 1,
      text: "Hello! 👋 I'm ExamBot, your AI study assistant. Ask me any questions about exam preparation, concepts, or strategies!",
      isUser: false,
      timestamp: new Date(),
    },
  ]);
  const [inputValue, setInputValue] = useState('');
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    if (!user) {
      navigate('/');
      return;
    }
  }, [user, navigate]);

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const sendMessage = async () => {
    if (!inputValue.trim()) return;

    const userMessage = {
      id: Date.now(),
      text: inputValue,
      isUser: true,
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, userMessage]);
    const currentInput = inputValue;
    setInputValue('');
    setLoading(true);

    try {
      const res = await fetch(`${API_BASE}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: currentInput }),
      });

      const data = await res.json();

      console.log('Backend response:', data); // Debug log

      if (!res.ok) {
        throw new Error(data.error || 'Failed to get response');
      }

      const botMessage = {
        id: Date.now() + 1,
        text: data.reply || data.answer || data.response || "No response from AI",
        isUser: false,
        timestamp: new Date(),
      };

      setMessages((prev) => [...prev, botMessage]);
    } catch (err) {
      console.error('Chat error:', err);
      const errorMessage = {
        id: Date.now() + 1,
        text: `Error: ${err.message}. Backend may not be running. Check console/logs.`,
        isUser: false,
        timestamp: new Date(),
      };
      setMessages((prev) => [...prev, errorMessage]);
      toast.error('Chatbot error - check backend');
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <main className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8 min-h-screen flex flex-col">
      <div className="mb-6">
        <h1 className="text-4xl font-bold text-gray-900 mb-2">💬 Ask Your Doubts (AI Assistant)</h1>
        <p className="text-gray-600">Instant AI help on exams - AI Assistant</p>
      </div>

      <Card className="flex-1 flex flex-col overflow-hidden min-h-[560px]">
        {/* Chat Messages */}
        <div className="flex-1 overflow-y-auto p-6 space-y-4 min-h-[420px]">
          {messages.map((msg) => (
            <ChatBubble
              key={msg.id}
              message={msg.text}
              isUser={msg.isUser}
            />
          ))}
          {loading && (
            <div className="flex justify-start">
              <div className="px-4 py-3 rounded-lg bg-gray-100 border border-gray-200 flex items-center gap-2">
                <Loader className="h-4 w-4 animate-spin text-sky-600" />
                <span className="text-sm text-gray-600">AI thinking...</span>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        {/* Input Area */}
        <div className="border-t border-gray-200 p-4 bg-gray-50">
          <div className="flex gap-3 items-end">
            <TextInput
              placeholder="Ask about Polity, History, Quant... (AI Assistant)"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyDown={handleKeyDown}
              disabled={loading}
              className="flex-1 h-14"
            />
            <Button
              variant="primary"
              onClick={sendMessage}
              disabled={loading || !inputValue.trim()}
              className="px-4 py-4"
            >
              <Send className="h-5 w-5" />
            </Button>
          </div>
        </div>
      </Card>

      {/* Sample Questions */}
      <Card className="mt-6">
        <h2 className="text-lg font-bold text-gray-900 mb-4">💡 Sample Questions:</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
          {[
            'What are fundamental rights?',
            'Explain monsoon system',
            'Profit and loss questions',
            'UPSC Polity basics'
          ].map((question, idx) => (
            <button
              key={idx}
              onClick={() => {
                setInputValue(question);
              }}
              className="p-3 text-left bg-gradient-to-r from-sky-50 to-indigo-50 border border-indigo-200 rounded-lg hover:border-sky-300 hover:shadow-md transition-all duration-200"
            >
              <p className="font-semibold text-gray-900">{question}</p>
            </button>
          ))}
        </div>
      </Card>
    </main>
  );
}
