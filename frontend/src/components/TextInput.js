import React from 'react';

export default function TextInput({
  placeholder = '',
  type = 'text',
  value = '',
  onChange = () => {},
  onKeyDown = () => {},
  error = false,
  disabled = false,
  className = '',
  label = '',
  icon: Icon,
}) {
  return (
    <div className="w-full">
      {label && <label className="block text-sm font-semibold text-gray-700 mb-2">{label}</label>}
      <div className="relative">
        {Icon && <Icon className="absolute left-3 top-3 text-gray-400 h-5 w-5" />}
        <input
          type={type}
          placeholder={placeholder}
          value={value}
          onChange={onChange}
          onKeyDown={onKeyDown}
          disabled={disabled}
          className={`
            w-full px-4 py-2.5 rounded-lg border transition-all duration-200
            ${Icon ? 'pl-10' : ''}
            ${error ? 'border-red-500 focus:ring-red-200' : 'border-gray-300 focus:ring-sky-200'}
            focus:outline-none focus:ring-2
            disabled:bg-gray-100 disabled:cursor-not-allowed
            ${className}
          `}
        />
      </div>
      {error && <p className="text-red-500 text-sm mt-1">{error}</p>}
    </div>
  );
}
