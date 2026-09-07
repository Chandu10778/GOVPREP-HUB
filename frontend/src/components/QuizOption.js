import React from 'react';

export default function QuizOption({
  option,
  isSelected,
  isCorrect,
  isShowingResult,
  onClick,
  disabled = false,
}) {
  const baseStyles = 'w-full p-4 rounded-lg border-2 transition-all duration-200 cursor-pointer text-left';

  let styles = baseStyles + ' border-gray-300 hover:border-sky-400 ';

  if (isSelected && isShowingResult) {
    styles = baseStyles + (isCorrect ? ' border-green-500 bg-green-50' : ' border-red-500 bg-red-50');
  } else if (isSelected) {
    styles = baseStyles + ' border-sky-500 bg-sky-50';
  } else if (isShowingResult && isCorrect) {
    styles = baseStyles + ' border-green-500 bg-green-50';
  }

  return (
    <button
      onClick={onClick}
      disabled={disabled}
      className={styles}
    >
      <p className="font-semibold text-gray-900">{option}</p>
    </button>
  );
}
