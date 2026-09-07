import React from 'react';

export default function Button({
  children,
  variant = 'primary',
  size = 'md',
  disabled = false,
  className = '',
  ...props
}) {
  const baseStyles = 'font-semibold rounded-lg transition-all duration-200 inline-flex items-center justify-center gap-2 cursor-pointer';

  const variants = {
    primary: 'bg-gradient-to-r from-sky-500 to-sky-600 text-white hover:shadow-lg hover:scale-105 disabled:opacity-50',
    secondary: 'bg-gradient-to-r from-purple-500 to-purple-600 text-white hover:shadow-lg hover:scale-105 disabled:opacity-50',
    outline: 'border-2 border-sky-500 text-sky-600 hover:bg-sky-50 disabled:opacity-50',
    ghost: 'text-sky-600 hover:bg-sky-50 disabled:opacity-50',
  };

  const sizes = {
    sm: 'px-3 py-2 text-sm',
    md: 'px-4 py-2.5 text-base',
    lg: 'px-6 py-3 text-lg',
  };

  return (
    <button
      className={`${baseStyles} ${variants[variant]} ${sizes[size]} ${className}`}
      disabled={disabled}
      {...props}
    >
      {children}
    </button>
  );
}
