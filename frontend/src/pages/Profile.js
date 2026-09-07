import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { User, Mail, Award, Zap, Flame, Edit2, Save, X } from 'lucide-react';
import { Card, Button, Badge, ProgressBar, StatCard, TextInput } from '../components';
import { toast } from 'react-toastify';

const STAGE_NAMES = {
  1: 'Beginner',
  2: 'Basics Completed',
  3: 'Intermediate',
  4: 'Advanced',
  5: 'Exam Ready',
};

export default function Profile({ user, setUser }) {
  const navigate = useNavigate();
  const [isEditing, setIsEditing] = useState(false);
  const [name, setName] = useState(user?.name || '');
  const [email, setEmail] = useState(user?.email || '');

  if (!user) {
    navigate('/');
    return null;
  }

  const handleSaveProfile = () => {
    if (!name.trim() || !email.trim()) {
      toast.error('Name and email are required');
      return;
    }

    const updatedUser = {
      ...user,
      name: name.trim(),
      email: email.trim(),
    };

    setUser(updatedUser);
    localStorage.setItem('user', JSON.stringify(updatedUser));
    setIsEditing(false);
    toast.success('Profile updated successfully!');
  };

  const xpProgress = (user.xp % 100) || user.xp;
  const stageName = STAGE_NAMES[user.level] || 'Beginner';

  const badges = [
    { icon: '🚀', name: 'Exam Beginner', unlocked: user.level >= 1 },
    { icon: '📘', name: 'Fundamentals Cleared', unlocked: user.level >= 2 },
    { icon: '🏆', name: 'Intermediate Scholar', unlocked: user.level >= 3 },
    { icon: '💪', name: 'Advanced Aspirant', unlocked: user.level >= 4 },
    { icon: '🎯', name: 'Exam Ready', unlocked: user.level >= 5 },
    { icon: '🔥', name: '7-Day Streak', unlocked: user.streak >= 7 },
    { icon: '🌟', name: '30-Day Consistency', unlocked: user.streak >= 30 },
  ];

  return (
    <main className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div className="mb-8">
        <h1 className="text-4xl font-bold text-gray-900 mb-2">👤 Your Profile</h1>
        <p className="text-gray-600">View and manage your exam preparation journey</p>
      </div>

      {/* Profile Header Card */}
      <Card className="mb-8">
        <div className="flex items-start justify-between mb-6">
          <div className="flex items-start gap-6">
            <div className="w-20 h-20 rounded-full bg-gradient-to-r from-sky-500 to-purple-500 flex items-center justify-center text-white text-3xl font-bold">
              {(user.name || 'U')[0].toUpperCase()}
            </div>
            {!isEditing ? (
              <div>
                <h2 className="text-2xl font-bold text-gray-900">{user.name}</h2>
                <p className="text-gray-600">{user.email}</p>
                <div className="flex gap-4 mt-3">
                  <Badge variant="primary">{stageName}</Badge>
                  <Badge variant="secondary">Level {user.level}</Badge>
                </div>
              </div>
            ) : (
              <div className="flex-1 space-y-3">
                <TextInput
                  label="Name"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                />
                <TextInput
                  label="Email"
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                />
              </div>
            )}
          </div>
          <div>
            {!isEditing ? (
              <Button
                variant="outline"
                onClick={() => setIsEditing(true)}
                className="gap-2"
              >
                <Edit2 className="h-4 w-4" />
                Edit
              </Button>
            ) : (
              <div className="flex gap-2">
                <Button
                  variant="primary"
                  onClick={handleSaveProfile}
                  className="gap-2"
                >
                  <Save className="h-4 w-4" />
                  Save
                </Button>
                <Button
                  variant="outline"
                  onClick={() => setIsEditing(false)}
                  className="gap-2"
                >
                  <X className="h-4 w-4" />
                </Button>
              </div>
            )}
          </div>
        </div>
      </Card>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
        <StatCard icon={Award} label="Current Level" value={user.level} variant="primary" />
        <StatCard icon={Zap} label="Total XP" value={user.xp} variant="secondary" />
        <StatCard icon={Flame} label="Daily Streak" value={`${user.streak} days`} variant="accent" />
        <StatCard
          icon={() => <span className="text-2xl">🎯</span>}
          label="Progress Stage"
          value={stageName}
          variant="primary"
        />
      </div>

      {/* Progress Section */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
        <Card>
          <h2 className="text-xl font-bold text-gray-900 mb-4">📈 Level Progress</h2>
          <ProgressBar value={xpProgress} max={100} label="XP to Next Level" />
          <div className="mt-6">
            <h3 className="font-semibold text-gray-800 mb-3">Stage Progress</h3>
            <div className="flex gap-2">
              {[1, 2, 3, 4, 5].map((stage) => (
                <div key={stage} className="flex-1 flex flex-col items-center">
                  <div
                    className={`w-full h-3 rounded-full ${
                      stage <= user.level
                        ? 'bg-gradient-to-r from-sky-500 to-sky-600'
                        : 'bg-gray-200'
                    }`}
                  />
                  <span className="text-xs text-gray-600 mt-2">{STAGE_NAMES[stage]}</span>
                </div>
              ))}
            </div>
          </div>
        </Card>

        <Card>
          <h2 className="text-xl font-bold text-gray-900 mb-4">🔥 Streak Status</h2>
          <div className="text-center py-8">
            <div className="text-6xl font-bold text-amber-500 mb-2">{user.streak}</div>
            <p className="text-lg text-gray-700 mb-4">Day Streak</p>
            <div className="bg-amber-50 border border-amber-200 rounded-lg p-4">
              <p className="text-sm text-amber-800">
                Keep your streak going! Complete at least one task daily to maintain consistency.
              </p>
            </div>
          </div>
        </Card>
      </div>

      {/* Badges Section */}
      <Card className="mb-8">
        <h2 className="text-xl font-bold text-gray-900 mb-4">🏅 Achievements & Badges</h2>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          {badges.map((badge, idx) => (
            <div
              key={idx}
              className={`p-4 rounded-lg text-center transition-all ${
                badge.unlocked
                  ? 'bg-gradient-to-br from-yellow-50 to-amber-50 border-2 border-amber-300'
                  : 'bg-gray-100 border-2 border-gray-200 opacity-50'
              }`}
            >
              <div className="text-3xl mb-2">{badge.icon}</div>
              <p className="font-semibold text-sm text-gray-900">{badge.name}</p>
              {!badge.unlocked && <p className="text-xs text-gray-600 mt-1">Locked</p>}
            </div>
          ))}
        </div>
      </Card>

      {/* Learning Stats Card */}
      <Card>
        <h2 className="text-xl font-bold text-gray-900 mb-4">📊 Learning Journey</h2>
        <div className="space-y-4">
          <div className="flex justify-between items-center p-4 bg-blue-50 rounded-lg">
            <span className="font-semibold text-blue-900">Total XP Earned</span>
            <span className="text-2xl font-bold text-blue-600">{user.xp + (user.level - 1) * 100}</span>
          </div>
          <div className="flex justify-between items-center p-4 bg-purple-50 rounded-lg">
            <span className="font-semibold text-purple-900">Current Stage</span>
            <span className="text-2xl font-bold text-purple-600">{stageName}</span>
          </div>
          <div className="flex justify-between items-center p-4 bg-green-50 rounded-lg">
            <span className="font-semibold text-green-900">Consistency Score</span>
            <span className="text-2xl font-bold text-green-600">{Math.min(100, user.streak * 10)}%</span>
          </div>
        </div>
      </Card>
    </main>
  );
}
