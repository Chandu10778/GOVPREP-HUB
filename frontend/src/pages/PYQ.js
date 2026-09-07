import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Brain, Check, X, Volume2 } from 'lucide-react';
import { Card, Button, Badge, QuizOption } from '../components';
import { toast } from 'react-toastify';

const API_BASE = process.env.REACT_APP_API_URL || 'http://127.0.0.1:5000';
const SUBJECTS = ['Polity', 'History', 'Geography', 'Current Affairs', 'Quantitative Aptitude'];

export default function PYQ({ user, setUser }) {
  const navigate = useNavigate();
  const [questions, setQuestions] = useState([]);
  const [selectedSubject, setSelectedSubject] = useState('Polity');
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [showResult, setShowResult] = useState(false);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [stats, setStats] = useState({ correct: 0, attempted: 0 });

  useEffect(() => {
    if (!user) {
      navigate('/');
      return;
    }
    fetchQuestions(selectedSubject);
  }, [user, navigate, selectedSubject]);

  const fetchQuestions = async (subject) => {
    setLoading(true);
    try {
      const res = await fetch(`${API_BASE}/pyq?subject=${encodeURIComponent(subject)}`);
      if (!res.ok) throw new Error('Failed to fetch questions');
      const data = await res.json();
      setQuestions(data);
      setCurrentQuestionIndex(0);
      setSelectedAnswer(null);
      setShowResult(false);
      setResult(null);
    } catch (err) {
      toast.error('Failed to load questions');
      setQuestions([]);
    } finally {
      setLoading(false);
    }
  };

  const currentQuestion = questions[currentQuestionIndex];
  const options = currentQuestion ? JSON.parse(currentQuestion.options) : [];

  const submitAnswer = async () => {
    if (selectedAnswer === null) {
      toast.error('Please select an option');
      return;
    }

    try {
      const res = await fetch(`${API_BASE}/pyq/answer`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          user_id: user.user_id,
          pyq_id: currentQuestion.id,
          selected_option: selectedAnswer,
        }),
      });

      if (!res.ok) throw new Error('Failed to submit answer');
      const data = await res.json();

      setResult(data);
      setShowResult(true);
      setStats({
        correct: stats.correct + (data.correct ? 1 : 0),
        attempted: stats.attempted + 1,
      });

      const updatedUser = {
        ...user,
        level: data.new_level,
        xp: data.xp,
      };
      localStorage.setItem('user', JSON.stringify(updatedUser));
      setUser(updatedUser);

      toast.success(data.correct ? '✅ Correct!' : '❌ Incorrect, try again');
    } catch (err) {
      toast.error(err.message);
    }
  };

  const nextQuestion = () => {
    if (currentQuestionIndex < questions.length - 1) {
      setCurrentQuestionIndex(currentQuestionIndex + 1);
      setSelectedAnswer(null);
      setShowResult(false);
      setResult(null);
    } else {
      toast.info('Quiz completed!');
      setCurrentQuestionIndex(0);
      setSelectedAnswer(null);
      setShowResult(false);
      setResult(null);
    }
  };

  const accuracy = stats.attempted > 0 ? Math.round((stats.correct / stats.attempted) * 100) : 0;

  return (
    <main className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div className="mb-8">
        <h1 className="text-4xl font-bold text-gray-900 mb-2">🧠 Previous Year Questions</h1>
        <p className="text-gray-600">Practice real exam questions and get instant feedback</p>
      </div>

      {/* Stats */}
      <div className="grid grid-cols-3 gap-4 mb-8">
        <Card className="text-center">
          <p className="text-sm text-gray-600">Questions</p>
          <p className="text-2xl font-bold text-sky-600">{questions.length}</p>
        </Card>
        <Card className="text-center">
          <p className="text-sm text-gray-600">Attempted</p>
          <p className="text-2xl font-bold text-purple-600">{stats.attempted}</p>
        </Card>
        <Card className="text-center">
          <p className="text-sm text-gray-600">Accuracy</p>
          <p className="text-2xl font-bold text-green-600">{accuracy}%</p>
        </Card>
      </div>

      {/* Subject Filter */}
      <Card className="mb-8">
        <h2 className="text-lg font-bold text-gray-900 mb-4">Select Subject</h2>
        <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-3">
          {SUBJECTS.map((subject) => (
            <button
              key={subject}
              onClick={() => {
                setSelectedSubject(subject);
                setStats({ correct: 0, attempted: 0 });
              }}
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

      {/* Question Card */}
      <div>
        {loading ? (
          <Card className="text-center py-12">
            <div className="inline-block animate-spin">
              <Brain className="h-8 w-8 text-sky-500" />
            </div>
            <p className="mt-4 text-gray-600">Loading questions...</p>
          </Card>
        ) : questions.length === 0 ? (
          <Card className="text-center py-12">
            <Brain className="h-12 w-12 text-gray-300 mx-auto mb-4" />
            <p className="text-gray-600">No questions available for {selectedSubject}</p>
            <Button
              variant="primary"
              className="mt-6"
              onClick={() => navigate('/dashboard')}
            >
              Back to Dashboard
            </Button>
          </Card>
        ) : (
          <Card>
            <div className="mb-6">
              <div className="flex items-center justify-between mb-4">
                <Badge variant="primary" size="md">
                  Question {currentQuestionIndex + 1} of {questions.length}
                </Badge>
                <Badge variant="secondary" size="md">
                  +{currentQuestion.xp} XP
                </Badge>
              </div>

              <h2 className="text-2xl font-bold text-gray-900 mb-6">{currentQuestion.question}</h2>

              {/* Options */}
              <div className="space-y-3 mb-8">
                {options.map((option, idx) => (
                  <QuizOption
                    key={idx}
                    option={option}
                    isSelected={selectedAnswer === option}
                    isCorrect={option === currentQuestion.answer}
                    isShowingResult={showResult}
                    onClick={() => !showResult && setSelectedAnswer(option)}
                    disabled={showResult}
                  />
                ))}
              </div>

              {/* Result Feedback */}
              {showResult && result && (
                <div
                  className={`p-4 rounded-lg mb-6 flex items-start gap-3 ${
                    result.correct
                      ? 'bg-green-50 border border-green-200'
                      : 'bg-red-50 border border-red-200'
                  }`}
                >
                  {result.correct ? (
                    <Check className="h-6 w-6 text-green-600 flex-shrink-0 mt-0.5" />
                  ) : (
                    <X className="h-6 w-6 text-red-600 flex-shrink-0 mt-0.5" />
                  )}
                  <div>
                    <p className={`font-bold ${result.correct ? 'text-green-800' : 'text-red-800'}`}>
                      {result.correct ? 'Correct!' : 'Incorrect'}
                    </p>
                    <p className={`text-sm mt-1 ${result.correct ? 'text-green-700' : 'text-red-700'}`}>
                      {result.correct
                        ? `Great job! You earned +${result.xp_gained} XP`
                        : `The correct answer is: ${currentQuestion.answer}`}
                    </p>
                  </div>
                </div>
              )}

              {/* Action Buttons */}
              <div className="flex gap-3">
                {!showResult ? (
                  <Button
                    variant="primary"
                    className="flex-1"
                    onClick={submitAnswer}
                    disabled={selectedAnswer === null}
                  >
                    Submit Answer
                  </Button>
                ) : (
                  <Button
                    variant="primary"
                    className="flex-1"
                    onClick={nextQuestion}
                  >
                    {currentQuestionIndex < questions.length - 1 ? 'Next Question' : 'Restart Quiz'}
                  </Button>
                )}
              </div>
            </div>
          </Card>
        )}
      </div>

      {/* Tips Card */}
      <Card className="mt-8">
        <h2 className="text-lg font-bold text-gray-900 mb-3">💡 Tips for Better Performance</h2>
        <ul className="space-y-2 text-gray-700 text-sm">
          <li className="flex gap-2">
            <span className="font-bold text-sky-600">✓</span>
            <span>Read questions carefully, pay attention to keywords</span>
          </li>
          <li className="flex gap-2">
            <span className="font-bold text-sky-600">✓</span>
            <span>Eliminate obviously wrong options first</span>
          </li>
          <li className="flex gap-2">
            <span className="font-bold text-sky-600">✓</span>
            <span>Practice consistently to improve accuracy</span>
          </li>
          <li className="flex gap-2">
            <span className="font-bold text-sky-600">✓</span>
            <span>Review your mistakes to learn better</span>
          </li>
        </ul>
      </Card>
    </main>
  );
}
