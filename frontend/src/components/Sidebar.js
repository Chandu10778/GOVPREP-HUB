import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import {
  LayoutDashboard,
  BookOpen,
  Brain,
  MessageCircle,
  User,
  Library,
} from 'lucide-react';

export default function Sidebar({ isOpen = true, onClose }) {
  const location = useLocation();

  const navItems = [
    { path: '/dashboard', icon: LayoutDashboard, label: 'Dashboard' },
    { path: '/materials', icon: BookOpen, label: 'Study Materials' },
    { path: '/current-affairs', icon: Library, label: 'Current Affairs' },
    { path: '/pyq', icon: Brain, label: 'PYQ Practice' },
    { path: '/chatbot', icon: MessageCircle, label: 'Ask Doubts' },
    { path: '/profile', icon: User, label: 'Profile' },
  ];

  const isActive = (path) => location.pathname === path;

  return (
    <>
      {/* Overlay for mobile */}
      {isOpen && (
        <div
          className="fixed inset-0 bg-black bg-opacity-50 md:hidden z-40"
          onClick={onClose}
        />
      )}

      {/* Sidebar */}
      <nav
        className={`
          fixed md:static top-16 left-0 w-64 bg-white shadow-lg transform transition-transform duration-300 z-41
          ${isOpen ? 'translate-x-0' : '-translate-x-full md:translate-x-0'}
        `}
      >
        <div className="p-6 space-y-2">
          {navItems.map((item) => {
            const Icon = item.icon;
            const active = isActive(item.path);

            return (
              <Link
                key={item.path}
                to={item.path}
                onClick={onClose}
                className={`
                  flex items-center gap-3 px-4 py-3 rounded-lg transition-all duration-200
                  ${
                    active
                      ? 'bg-gradient-to-r from-sky-500 to-sky-600 text-white shadow-md'
                      : 'text-gray-700 hover:bg-gray-100'
                  }
                `}
              >
                <Icon className="h-5 w-5" />
                <span className="font-semibold">{item.label}</span>
              </Link>
            );
          })}
        </div>
      </nav>
    </>
  );
}
