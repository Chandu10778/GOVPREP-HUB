import React from 'react';

export default function ChatBubble({ message, isUser = false }) {
  const baseStyles = 'px-4 py-3 rounded-lg max-w-[75%] animate-fade-in break-words';
  const userStyles = 'bg-gradient-to-r from-sky-500 to-sky-600 text-white rounded-bl-none';
  const botStyles = 'bg-gray-100 text-gray-900 rounded-bl-lg border border-gray-200';

  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'} mb-3`}> 
      <div className={`${baseStyles} ${isUser ? userStyles : botStyles}`}>
        <p className="text-sm leading-relaxed whitespace-pre-wrap">{message}</p>
      </div>
    </div>
  );
}
