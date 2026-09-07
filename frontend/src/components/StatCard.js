import React from 'react';

export default function StatCard({ icon: Icon, label, value, variant = 'primary' }) {
  const variants = {
    primary: 'from-sky-500 to-sky-600',
    secondary: 'from-purple-500 to-purple-600',
    accent: 'from-amber-500 to-orange-600',
  };

  return (
    <div className={`bg-gradient-to-br ${variants[variant]} rounded-xl p-6 text-white shadow-lg hover:shadow-xl transition-shadow`}>
      <div className="flex items-start justify-between">
        <div className="flex-1 pr-4">
          <p className="text-sm font-medium text-white">{label}</p>
          <p className="text-3xl font-bold mt-2 text-white break-words">{value}</p>
        </div>
        {Icon && <Icon className="h-8 w-8 text-white flex-shrink-0" />}
      </div>
    </div>
  );
}
