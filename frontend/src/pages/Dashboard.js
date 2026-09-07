import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Zap, Flame, Award, BookOpen, Brain, MessageCircle, TrendingUp } from 'lucide-react';
import { Card, StatCard, ProgressBar, Badge, Button } from '../components';
import { toast } from 'react-toastify';


const API_BASE = process.env.REACT_APP_API_URL || 'http://127.0.0.1:5000';
const STAGE_NAMES = {
  1: 'Beginner',
  2: 'Basics Completed',
  3: 'Intermediate',
  4: 'Advanced',
  5: 'Exam Ready',
};

export default function Dashboard({ user, setUser }) {
  const navigate = useNavigate();
  const [subjectProgress, setSubjectProgress] = useState([]);
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (!user) {
      navigate('/');
      return;
    }
    fetchSubjectProgress(user.user_id);
    fetchLeaderboard();
  }, [user, navigate]);

  const fetchSubjectProgress = async (userId) => {
    try {
      const res = await fetch(`${API_BASE}/user/${userId}/progress`);
      if (!res.ok) throw new Error('Failed to fetch progress');
      const data = await res.json();
      setSubjectProgress(data);
    } catch (err) {
      console.error('Progress fetch error:', err);
    }
  };

  const fetchLeaderboard = async () => {
    try {
      const res = await fetch(`${API_BASE}/leaderboard`);
      if (!res.ok) throw new Error('Failed to fetch leaderboard');
      const data = await res.json();
      setLeaderboard(data);
    } catch {
      setLeaderboard([]);
    }
  };

  const xpProgress = (user.xp % 100) || user.xp;
  const stageName = STAGE_NAMES[user.level] || 'Beginner';

  return (
    <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      {/* Hero Stats */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
        <StatCard icon={Award} label="Current Level" value={user.level} variant="primary" />
        <StatCard icon={Zap} label="XP Progress" value={`${xpProgress}/100`} variant="secondary" />
        <StatCard icon={Flame} label="Daily Streak" value={`${user.streak} days`} variant="accent" />
        <StatCard icon={TrendingUp} label="Stage" value={stageName} variant="primary" />
      </div>

      {/* Main Progress */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-8">
        <div className="lg:col-span-2">
          <Card className="mb-6">
            <h2 className="text-2xl font-bold text-gray-900 mb-4">📚 Your Progress</h2>
            <ProgressBar value={xpProgress} max={100} label="XP to Next Level" />
            <div className="mt-6">
              <h3 className="text-lg font-semibold text-gray-800 mb-4">Stage: {stageName}</h3>
              <div className="flex gap-2 mb-4">
                {[1, 2, 3, 4, 5].map((stage) => (
                  <div
                    key={stage}
                    className={`flex-1 h-2 rounded-full transition-all ${
                      stage <= user.level
                        ? 'bg-gradient-to-r from-sky-500 to-sky-600'
                        : 'bg-gray-200'
                    }`}
                  />
                ))}
              </div>
              <p className="text-sm text-gray-600">
                {user.level === 5
                  ? 'You are exam ready! Keep practicing to maintain readiness.'
                  : `Complete more tasks to reach ${STAGE_NAMES[user.level + 1] || 'next'} stage`}
              </p>
            </div>
          </Card>

          {/* Subject Progress */}
          <Card>
            <h2 className="text-xl font-bold text-gray-900 mb-4">📖 Subject-wise Progress</h2>
            {subjectProgress.length === 0 ? (
              <div className="text-center py-8">
                <p className="text-gray-600">Start learning by completing tasks!</p>
              </div>
            ) : (
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {subjectProgress.map((item) => (
                  <div
                    key={item.subject}
                    className="p-4 bg-gradient-to-br from-sky-50 to-purple-50 rounded-lg border border-gray-200 hover:border-sky-300 transition-colors"
                  >
                    <h3 className="font-semibold text-gray-900">{item.subject}</h3>
                    <div className="mt-3 space-y-2">
                      <p className="text-sm text-gray-700">
                        <span className="font-semibold">{item.completed_tasks}</span> tasks completed
                      </p>
                      <p className="text-sm text-gray-700">
                        <span className="font-semibold">{item.xp}</span> XP earned
                      </p>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </Card>
        </div>

        {/* Quick Actions & Leaderboard */}
        <div>
          <Card className="mb-6">
            <h2 className="text-xl font-bold text-gray-900 mb-4">🚀 Quick Start</h2>
            <div className="space-y-3">
              <Button
                variant="secondary"
                className="w-full justify-start gap-2"
                onClick={() => navigate('/pyq')}
              >
                <Brain className="h-4 w-4" />
                Practice PYQ
              </Button>
              <Button
                variant="outline"
                className="w-full justify-start gap-2"
                onClick={() => navigate('/chatbot')}
              >
                <MessageCircle className="h-4 w-4" />
                Ask Doubts
              </Button>
            </div>
          </Card>

          {/* Leaderboard */}
          <Card>
            <h2 className="text-xl font-bold text-gray-900 mb-4">🏆 Top Performers</h2>
            {leaderboard.length === 0 ? (
              <p className="text-gray-600 text-sm">No data yet</p>
            ) : (
              <div className="space-y-3">
                {leaderboard.slice(0, 5).map((entry, index) => (
                  <div
                    key={entry.user_id}
                    className={`p-3 rounded-lg ${
                      entry.user_id === user.user_id ? 'bg-sky-50 border-l-4 border-sky-500' : 'bg-gray-50'
                    }`}
                  >
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-2">
                        <span className="font-bold text-gray-700">#{index + 1}</span>
                        <span className="font-semibold text-gray-900">{entry.username}</span>
                      </div>
                      <Badge variant="primary" size="sm">
                        L{entry.level}
                      </Badge>
                    </div>
                    <p className="text-xs text-gray-600 mt-1">{entry.xp} XP</p>
                  </div>
                ))}
              </div>
            )}
          </Card>
        </div>
      </div>

      {/* Learning Tips */}
      <Card>
        <h2 className="text-xl font-bold text-gray-900 mb-4">💡 Personalized Learning Plan</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {user.level === 1 && (
            <>
              <div className="p-4 bg-blue-50 rounded-lg">
                <h3 className="font-semibold text-blue-900 mb-2">📚 Read Basics</h3>
                <p className="text-sm text-blue-800">Start with NCERT basics for Polity, History, and Geography.</p>
              </div>
              <div className="p-4 bg-purple-50 rounded-lg">
                <h3 className="font-semibold text-purple-900 mb-2">📝 Track News</h3>
                <p className="text-sm text-purple-800">Keep track of daily current affairs in 10 minutes.</p>
              </div>
              <div className="p-4 bg-green-50 rounded-lg">
                <h3 className="font-semibold text-green-900 mb-2">🧮 Practice Math</h3>
                <p className="text-sm text-green-800">Solve foundational quantitative problems daily.</p>
              </div>
            </>
          )}
          {user.level >= 2 && user.level < 5 && (
            <>
              <div className="p-4 bg-blue-50 rounded-lg">
                <h3 className="font-semibold text-blue-900 mb-2">📖 Deep Dive</h3>
                <p className="text-sm text-blue-800">Complete comprehensive subject notes and revisions.</p>
              </div>
              <div className="p-4 bg-purple-50 rounded-lg">
                <h3 className="font-semibold text-purple-900 mb-2">❓ Solve PYQs</h3>
                <p className="text-sm text-purple-800">Practice real exam questions regularly with timing.</p>
              </div>
              <div className="p-4 bg-green-50 rounded-lg">
                <h3 className="font-semibold text-green-900 mb-2">🎯 Mock Tests</h3>
                <p className="text-sm text-green-800">Take weekly full mock tests to assess your level.</p>
              </div>
            </>
          )}
          {user.level === 5 && (
            <>
              <div className="p-4 bg-blue-50 rounded-lg">
                <h3 className="font-semibold text-blue-900 mb-2">⚡ Advanced PYQs</h3>
                <p className="text-sm text-blue-800">Focus on harder PYQ sets and tricky questions.</p>
              </div>
              <div className="p-4 bg-purple-50 rounded-lg">
                <h3 className="font-semibold text-purple-900 mb-2">🏃 Timed Mocks</h3>
                <p className="text-sm text-purple-800">Simulate exam conditions and track your score trends.</p>
              </div>
              <div className="p-4 bg-green-50 rounded-lg">
                <h3 className="font-semibold text-green-900 mb-2">👥 Peer Learning</h3>
                <p className="text-sm text-green-800">Help other learners and consolidate your knowledge.</p>
              </div>
            </>
          )}
        </div>
      </Card>
    </main>
  );
}
