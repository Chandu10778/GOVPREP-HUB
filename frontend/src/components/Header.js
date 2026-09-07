import React from 'react';
import { LogOut, Menu, X } from 'lucide-react';
import Button from './Button';

export default function Header({ user, onLogout, title = 'GovPrep Hub', isMobileMenuOpen, setIsMobileMenuOpen }) {
  return (
    <header className="bg-white shadow-md sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex items-center justify-between">
        <div className="flex items-center gap-2">
          <div className="text-2xl font-bold bg-gradient-to-r from-sky-600 to-purple-600 bg-clip-text text-transparent">
            {title}
          </div>
        </div>

        <div className="hidden md:flex items-center gap-4">
          {user && (
            <>
              <div className="flex items-center gap-2">
                <div className="w-10 h-10 rounded-full bg-gradient-to-r from-sky-500 to-purple-500 flex items-center justify-center text-white font-bold">
                  {(user.name || 'U')[0].toUpperCase()}
                </div>
                <div className="flex flex-col">
                  <p className="text-sm font-semibold text-gray-900">{user.name}</p>
                  <p className="text-xs text-gray-500">Level {user.level}</p>
                </div>
              </div>
              <Button
                variant="ghost"
                size="sm"
                onClick={onLogout}
                className="flex items-center gap-2"
              >
                <LogOut className="h-4 w-4" />
                Logout
              </Button>
            </>
          )}
        </div>

        <button
          className="md:hidden"
          onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
        >
          {isMobileMenuOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
        </button>
      </div>
    </header>
  );
}
