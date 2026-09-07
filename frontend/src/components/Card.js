import React from 'react';

export default function Card({ children, className = '', ...props }) {
  return (
    <div
      className={`bg-white rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300 p-6 animate-fade-in border border-gray-100 ${className}`}
      {...props}
    >
      {children}
    </div>
  );
}
