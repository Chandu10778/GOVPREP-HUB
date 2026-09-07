import React, { useState, useEffect } from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

import LoginPage from './LoginPage';
import Dashboard from './pages/Dashboard';
import PYQ from './pages/PYQ';
import StudyMaterials from './pages/StudyMaterials';
import CurrentAffairs from './pages/CurrentAffairs';
import Chatbot from './pages/Chatbot';
import Profile from './pages/Profile';
import Layout from './components/Layout';

function App() {
  const [user, setUser] = useState(null);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  useEffect(() => {
    const storedUser = JSON.parse(localStorage.getItem('user'));
    if (storedUser) {
      setUser(storedUser);
    }
  }, []);

  const handleLogout = () => {
    localStorage.removeItem('user');
    setUser(null);
  };

  return (
    <BrowserRouter>
      <div className="App">
        {user ? (
          <Layout
            user={user}
            onLogout={handleLogout}
            isMobileMenuOpen={isMobileMenuOpen}
            setIsMobileMenuOpen={setIsMobileMenuOpen}
          >
            <Routes>
              <Route path="/dashboard" element={<Dashboard user={user} setUser={setUser} />} />
              <Route path="/pyq" element={<PYQ user={user} setUser={setUser} />} />
              <Route path="/materials" element={<StudyMaterials user={user} setUser={setUser} />} />
              <Route path="/current-affairs" element={<CurrentAffairs user={user} setUser={setUser} />} />
              <Route path="/chatbot" element={<Chatbot user={user} />} />
              <Route path="/profile" element={<Profile user={user} setUser={setUser} />} />
              <Route path="/" element={<Navigate to="/dashboard" />} />
            </Routes>
          </Layout>
        ) : (
          <Routes>
            <Route path="/" element={<LoginPage setUser={setUser} />} />
            <Route path="*" element={<Navigate to="/" />} />
          </Routes>
        )}
        <ToastContainer position="bottom-right" autoClose={3000} />
      </div>
    </BrowserRouter>
  );
}

export default App;
