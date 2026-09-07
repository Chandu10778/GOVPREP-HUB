import React from 'react';

export default function ProgressBar({ value = 0, max = 100, label = '', className = '' }) {
  const percentage = Math.min(100, (value / max) * 100);
  
  return (
    <div className={`w-full ${className}`}>
      {label && <p className="text-sm font-semibold text-gray-800 mb-2">{label}</p>}
      <div className="w-full bg-gray-300 rounded-full h-4 overflow-hidden shadow-sm">
        <div
          className="bg-gradient-to-r from-sky-400 to-sky-600 h-full transition-all duration-300"
          style={{ width: `${percentage}%` }}
        />
      </div>
      <p className="text-sm font-medium text-gray-700 mt-2">{value} / {max}</p>
    </div>
  );
}
