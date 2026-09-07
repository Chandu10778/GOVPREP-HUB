import React from 'react';

export default function Badge({ children, variant = 'primary', size = 'md', className = '' }) {
  const variants = {
    primary: 'bg-sky-100 text-sky-800',
    secondary: 'bg-purple-100 text-purple-800',
    success: 'bg-green-100 text-green-800',
    warning: 'bg-yellow-100 text-yellow-800',
    danger: 'bg-red-100 text-red-800',
  };

  const sizes = {
    sm: 'px-2 py-1 text-xs',
    md: 'px-3 py-1.5 text-sm',
    lg: 'px-4 py-2 text-base',
  };

  return (
    <span className={`inline-flex rounded-full font-semibold ${variants[variant]} ${sizes[size]} ${className}`}>
      {children}
    </span>
  );
}
