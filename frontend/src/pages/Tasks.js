import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { BookOpen, Zap, CheckCircle, Lock } from 'lucide-react';
import { Card, Button, ProgressBar, Badge } from '../components';
import { toast } from 'react-toastify';

const API_BASE = process.env.REACT_APP_API_URL || 'http://127.0.0.1:5000';
const STAGE_NAMES = {
  1: 'Beginner',
  2: 'Basics Completed',
  3: 'Intermediate',
  4: 'Advanced',
  5: 'Exam Ready',
};

const SUBJECTS = ['Polity', 'History', 'Geography', 'Current Affairs', 'Quantitative Aptitude'];

export default function Tasks({ user, setUser }) {
  const navigate = useNavigate();
  const [tasks, setTasks] = useState([]);
  const [selectedSubject, setSelectedSubject] = useState('Polity');
  const [loading, setLoading] = useState(false);
  const [completingTaskId, setCompletingTaskId] = useState(null);

  useEffect(() => {
    if (!user) {
      navigate('/');
      return;
    }
    fetchTasks(selectedSubject);
  }, [user, navigate, selectedSubject]);

  const fetchTasks = async (subject) => {
    setLoading(true);
    try {
      const res = await fetch(`${API_BASE}/tasks/subject/${encodeURIComponent(subject)}`);
      if (!res.ok) throw new Error('Failed to fetch tasks');
      const data = await res.json();
      setTasks(data);
    } catch (err) {
      toast.error('Failed to load tasks');
      setTasks([]);
    } finally {
      setLoading(false);
    }
  };

  const completeTask = async (taskId) => {
    if (completingTaskId) return;
    setCompletingTaskId(taskId);

    try {
      const res = await fetch(`${API_BASE}/complete-task`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_id: user.user_id, task_id: taskId }),
      });

      if (!res.ok) throw new Error('Failed to complete task');
      const data = await res.json();

      const updatedUser = {
        ...user,
        level: data.new_level,
        xp: data.xp,
        streak: data.streak,
      };
      localStorage.setItem('user', JSON.stringify(updatedUser));
      setUser(updatedUser);
      fetchTasks(selectedSubject);
      toast.success(`🎉 Task completed! +${tasks.find(t => t.id === taskId)?.xp} XP`);
    } catch (err) {
      toast.error(err.message);
    } finally {
      setCompletingTaskId(null);
    }
  };

  return (
    <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div className="mb-8">
        <h1 className="text-4xl font-bold text-gray-900 mb-2">📚 Study Tasks</h1>
        <p className="text-gray-600">Complete tasks to earn XP and progress through stages</p>
      </div>

      {/* Subject Filter */}
      <Card className="mb-8">
        <h2 className="text-lg font-bold text-gray-900 mb-4">Select Subject</h2>
        <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-3">
          {SUBJECTS.map((subject) => (
            <button
              key={subject}
              onClick={() => setSelectedSubject(subject)}
              className={`p-3 rounded-lg font-semibold transition-all duration-200 ${
                selectedSubject === subject
                  ? 'bg-gradient-to-r from-sky-500 to-sky-600 text-white shadow-lg scale-105'
                  : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
              }`}
            >
              {subject}
            </button>
          ))}
        </div>
      </Card>

      {/* Tasks Grid */}
      <div>
        {loading ? (
          <div className="text-center py-12">
            <div className="inline-block animate-spin">
              <BookOpen className="h-8 w-8 text-sky-500" />
            </div>
            <p className="mt-4 text-gray-600">Loading tasks...</p>
          </div>
        ) : tasks.length === 0 ? (
          <Card className="text-center py-12">
            <BookOpen className="h-12 w-12 text-gray-300 mx-auto mb-4" />
            <p className="text-gray-600">No tasks available for {selectedSubject}</p>
          </Card>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {tasks.map((task) => (
              <Card key={task.id} className="flex flex-col">
                <div className="flex items-start justify-between mb-3">
                  <h3 className="text-lg font-bold text-gray-900 flex-1 line-clamp-2">{task.title}</h3>
                  <Badge variant="secondary" size="sm">
                    {task.stage_name}
                  </Badge>
                </div>

                {task.description && (
                  <p className="text-sm text-gray-600 mb-4 line-clamp-2">{task.description}</p>
                )}

                <div className="flex items-center gap-2 text-sm text-gray-700 mb-4">
                  <Zap className="h-4 w-4 text-amber-500" />
                  <span className="font-semibold">+{task.xp} XP</span>
                </div>

                <div className="mt-auto">
                  <Button
                    variant="primary"
                    className="w-full"
                    onClick={() => completeTask(task.id)}
                    disabled={completingTaskId === task.id}
                  >
                    {completingTaskId === task.id ? (
                      <>
                        <span className="inline-block animate-spin"><CheckCircle className="h-4 w-4" /></span>
                        Completing...
                      </>
                    ) : (
                      <>
                        <CheckCircle className="h-4 w-4" />
                        Complete Task
                      </>
                    )}
                  </Button>
                </div>
              </Card>
            ))}
          </div>
        )}
      </div>

      {/* Info Card */}
      <Card className="mt-8">
        <h2 className="text-lg font-bold text-gray-900 mb-3">💡 How to Use</h2>
        <ul className="space-y-2 text-gray-700">
          <li className="flex gap-2">
            <span className="font-bold text-sky-600">1.</span>
            <span>Choose a subject to view related study tasks</span>
          </li>
          <li className="flex gap-2">
            <span className="font-bold text-sky-600">2.</span>
            <span>Complete the task and mark it as done</span>
          </li>
          <li className="flex gap-2">
            <span className="font-bold text-sky-600">3.</span>
            <span>Earn XP and progress to the next stage</span>
          </li>
          <li className="flex gap-2">
            <span className="font-bold text-sky-600">4.</span>
            <span>Mix tasks from different subjects for balanced learning</span>
          </li>
        </ul>
      </Card>
    </main>
  );
}
