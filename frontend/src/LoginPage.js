import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';
import { Eye, EyeOff } from 'lucide-react';
import { Button, TextInput, Card } from './components';

const API_BASE = process.env.REACT_APP_API_URL || 'http://127.0.0.1:5000';

function LoginPage({ setUser }) {
  const [mode, setMode] = useState('login');
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const validateEmail = (email) => {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
  };

  const validatePassword = (password) => {
    return password.length >= 6;
  };

  const handleLogin = async () => {
    if (!validateEmail(email)) {
      toast.error('Please enter a valid email.');
      return;
    }
    if (!validatePassword(password)) {
      toast.error('Password must be at least 6 characters.');
      return;
    }

    setLoading(true);
    try {
      const res = await fetch(`${API_BASE}/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password }),
      });
      if (!res.ok) throw new Error('Invalid credentials');
      const data = await res.json();
      localStorage.setItem('user', JSON.stringify(data));
      setUser(data);
      toast.success('Login successful!');
      navigate('/dashboard');
    } catch (err) {
      toast.error(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleRegister = async () => {
    if (!name.trim()) {
      toast.error('Name is required.');
      return;
    }
    if (!validateEmail(email)) {
      toast.error('Please enter a valid email.');
      return;
    }
    if (!validatePassword(password)) {
      toast.error('Password must be at least 6 characters.');
      return;
    }

    setLoading(true);
    try {
      const res = await fetch(`${API_BASE}/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, email, password }),
      });

      if (!res.ok) {
        const body = await res.json();
        throw new Error(body?.message || 'Registration failed');
      }

      const data = await res.json();
      localStorage.setItem('user', JSON.stringify(data));
      setUser(data);
      toast.success('Registration successful!');
      navigate('/dashboard');
    } catch (err) {
      toast.error(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (mode === 'login') {
      handleLogin();
    } else {
      handleRegister();
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-sky-50 to-purple-50 flex items-center justify-center px-4 py-12">
      <div className="w-full max-w-md">
        {/* Logo & Brand */}
        <div className="text-center mb-8">
          <div className="inline-block mb-4">
            <div className="w-16 h-16 rounded-full bg-gradient-to-r from-sky-500 to-purple-500 flex items-center justify-center text-white text-2xl font-bold">
              📚
            </div>
          </div>
          <h1 className="text-4xl font-bold bg-gradient-to-r from-sky-600 to-purple-600 bg-clip-text text-transparent mb-2">
            GovPrep Hub
          </h1>
          <p className="text-gray-600">Master government exams with gamified learning</p>
        </div>

        {/* Auth Card */}
        <Card className="p-8">
          <h2 className="text-2xl font-bold text-gray-900 mb-6 text-center">
            {mode === 'login' ? 'Welcome Back' : 'Join Now'}
          </h2>

          <form onSubmit={handleSubmit} className="space-y-4">
            {mode === 'register' && (
              <TextInput
                label="Full Name"
                placeholder="John Doe"
                value={name}
                onChange={(e) => setName(e.target.value)}
              />
            )}

            <TextInput
              label="Email Address"
              type="email"
              placeholder="you@example.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />

            <div className="relative">
              <TextInput
                label="Password"
                type={showPassword ? 'text' : 'password'}
                placeholder="••••••••"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
              <button
                type="button"
                onClick={() => setShowPassword(!showPassword)}
                className="absolute right-3 top-10 text-gray-500 hover:text-gray-700"
              >
                {showPassword ? <EyeOff className="h-4 w-4" /> : <Eye className="h-4 w-4" />}
              </button>
            </div>

            <Button
              variant="primary"
              className="w-full"
              disabled={loading}
            >
              {loading ? (mode === 'login' ? 'Signing in...' : 'Creating account...') : (mode === 'login' ? 'Sign In' : 'Create Account')}
            </Button>
          </form>

          <div className="mt-6 pt-6 border-t border-gray-200">
            <p className="text-center text-gray-600 text-sm">
              {mode === 'login' ? "Don't have an account?" : 'Already have an account?'}{' '}
              <button
                onClick={() => setMode(mode === 'login' ? 'register' : 'login')}
                className="text-sky-600 font-semibold hover:text-sky-700 transition-colors"
              >
                {mode === 'login' ? 'Sign up' : 'Sign in'}
              </button>
            </p>
          </div>
        </Card>

        {/* Features List */}
        <div className="mt-8 grid grid-cols-2 gap-4">
          {[
            { icon: '🎯', label: 'Structured Learning' },
            { icon: '🏆', label: 'Gamified Experience' },
            { icon: '🤖', label: 'AI Support' },
            { icon: '📊', label: 'Progress Tracking' },
          ].map((feature, idx) => (
            <div key={idx} className="flex items-center gap-2 text-sm text-gray-700">
              <span className="text-xl">{feature.icon}</span>
              <span>{feature.label}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default LoginPage;
