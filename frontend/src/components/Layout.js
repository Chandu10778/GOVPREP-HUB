import React from 'react';
import Header from './Header';
import Sidebar from './Sidebar';

export default function Layout({
  children,
  user,
  onLogout,
  isMobileMenuOpen,
  setIsMobileMenuOpen,
}) {
  return (
    <div className="flex flex-col h-screen bg-gray-50">
      <Header
        user={user}
        onLogout={onLogout}
        title="GovPrep Hub"
        isMobileMenuOpen={isMobileMenuOpen}
        setIsMobileMenuOpen={setIsMobileMenuOpen}
      />
      <div className="flex flex-1 overflow-hidden">
        <Sidebar
          isOpen={isMobileMenuOpen}
          onClose={() => setIsMobileMenuOpen(false)}
        />
        <main className="flex-1 overflow-y-auto">
          {children}
        </main>
      </div>
    </div>
  );
}
