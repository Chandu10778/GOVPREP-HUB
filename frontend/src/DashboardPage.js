import React, { useState, useEffect, useRef } from "react";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";

const API_BASE = process.env.REACT_APP_API_URL || "http://127.0.0.1:5000";
const STAGE_NAMES = {
  1: 'Beginner',
  2: 'Basics Completed',
  3: 'Intermediate',
  4: 'Advanced',
  5: 'Exam Ready'
};

function DashboardPage({ user, setUser }) {
  const [tasks, setTasks] = useState([]);
  const [leaderboard, setLeaderboard] = useState([]);
  const [streak, setStreak] = useState(0);
  const [subjectProgress, setSubjectProgress] = useState([]);
  const [pyqQuestions, setPyqQuestions] = useState([]);
  const [selectedSubject, setSelectedSubject] = useState('Polity');
  const [selectedPyqId, setSelectedPyqId] = useState(null);
  const [selectedPyqAnswer, setSelectedPyqAnswer] = useState('');
  const [pyqFeedback, setPyqFeedback] = useState('');
  const [summaryText, setSummaryText] = useState('');
  const [summaryResult, setSummaryResult] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [chatInput, setChatInput] = useState("");
  const [chatMessages, setChatMessages] = useState([]);
  const [showLevelUnlock, setShowLevelUnlock] = useState(false);

  const [newTaskTitle, setNewTaskTitle] = useState("");
  const [newTaskXp, setNewTaskXp] = useState("");
  const [newTaskLevel, setNewTaskLevel] = useState("");

  const [isEditingProfile, setIsEditingProfile] = useState(false);
  const [profileName, setProfileName] = useState("");
  const [profileEmail, setProfileEmail] = useState("");

  const prevLevelRef = useRef(null);
  const navigate = useNavigate();

  useEffect(() => {
    if (!user) {
      navigate("/");
      return;
    }
    setStreak(user.streak || 0);
    setProfileName(user.username || "User");
    setProfileEmail(user.email || "");
    fetchTasks(user.level);
    fetchLeaderboard();
    fetchSubjectProgress(user.user_id);
    fetchPYQ(selectedSubject);
    prevLevelRef.current = user.level;
  }, [user, navigate, selectedSubject]);

  useEffect(() => {
    if (!user) return;
    const prevLevel = prevLevelRef.current;
    if (prevLevel !== null && user.level > prevLevel) {
      setShowLevelUnlock(true);
      const timer = setTimeout(() => setShowLevelUnlock(false), 1800);
      return () => clearTimeout(timer);
    }
    prevLevelRef.current = user.level;
  }, [user]);

  const fetchTasks = async (stage) => {
    setLoading(true);
    setError("");
    try {
      const res = await fetch(`${API_BASE}/tasks/stage/${stage}`);
      if (!res.ok) throw new Error("Failed to fetch tasks");
      const data = await res.json();
      setTasks(data);
    } catch (err) {
      setError(err.message);
      toast.error(err.message);
    } finally {
      setLoading(false);
    }
  };

  const fetchLeaderboard = async () => {
    try {
      const res = await fetch(`${API_BASE}/leaderboard`);
      if (!res.ok) throw new Error("Could not load leaderboard");
      const data = await res.json();
      setLeaderboard(data);
    } catch {
      setLeaderboard([
        { user_id: 412, username: "Nova", level: 5, stage_name: 'Exam Ready', xp: 450 },
        { user_id: 223, username: "Eli", level: 4, stage_name: 'Advanced', xp: 380 },
        { user_id: 734, username: "Quinn", level: 3, stage_name: 'Intermediate', xp: 330 },
      ]);
    }
  };

  const fetchSubjectProgress = async (user_id) => {
    try {
      const res = await fetch(`${API_BASE}/user/${user_id}/progress`);
      if (!res.ok) throw new Error("Could not fetch subject progress");
      const data = await res.json();
      setSubjectProgress(data);
    } catch {
      setSubjectProgress([]);
    }
  };

  const fetchPYQ = async (subject) => {
    try {
      const res = await fetch(`${API_BASE}/pyq?subject=${encodeURIComponent(subject)}`);
      if (!res.ok) throw new Error("Could not fetch PYQ questions");
      const data = await res.json();
      setPyqQuestions(data);
      setSelectedPyqId(data.length > 0 ? data[0].id : null);
      setPyqFeedback('');
    } catch {
      setPyqQuestions([]);
      setSelectedPyqId(null);
      setPyqFeedback('Unable to load practice questions now.');
    }
  };

  const submitPYQAnswer = async () => {
    if (!selectedPyqId || selectedPyqAnswer.trim() === '') {
      toast.error('Choose an option to submit.');
      return;
    }

    try {
      const res = await fetch(`${API_BASE}/pyq/answer`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          user_id: user.user_id,
          pyq_id: selectedPyqId,
          selected_option: selectedPyqAnswer,
        }),
      });

      if (!res.ok) {
        const body = await res.json();
        throw new Error(body.message || 'Answer submission failed');
      }

      const data = await res.json();
      setPyqFeedback(data.correct ? `Correct! +${data.xp_gained} XP` : `Incorrect. +${data.xp_gained} XP`);
      const updatedUser = { ...user, level: data.new_level, xp: data.xp, streak: data.streak || user.streak };
      setUser(updatedUser);
      localStorage.setItem('user', JSON.stringify(updatedUser));
      fetchTasks(updatedUser.level);
      fetchSubjectProgress(updatedUser.user_id);
      fetchLeaderboard();

      toast.success(`Submitted answer. ${data.correct ? 'Well done!' : 'Try next question.'}`);
    } catch (err) {
      toast.error(err.message);
    }
  };

  const requestSummary = async () => {
    if (!summaryText.trim()) {
      toast.error('Enter study text to summarize.');
      return;
    }

    try {
      const res = await fetch(`${API_BASE}/summarize`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: summaryText }),
      });
      if (!res.ok) {
        const body = await res.json();
        throw new Error(body.message || 'Summarization failed');
      }
      const data = await res.json();
      setSummaryResult(data.summary);
    } catch (err) {
      toast.error(err.message);
    }
  };

  const sendMessage = async () => {
    const message = chatInput.trim();
    if (!message) return;

    const userMsg = { id: Date.now(), from: "You", text: message };
    setChatMessages((prev) => [...prev, userMsg]);
    setChatInput("");

    try {
      const res = await fetch(`${API_BASE}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: message }),
      });
      if (!res.ok) throw new Error('Chatbot response failed');
      const data = await res.json();

      const botReply = {
        id: Date.now() + 1,
        from: 'ExamBot',
        text: data.answer,
      };
      setChatMessages((prev) => [...prev, botReply]);
    } catch (err) {
      const errorReply = {
        id: Date.now() + 2,
        from: 'ExamBot',
        text: 'Sorry, cannot answer now. Try again later.',
      };
      setChatMessages((prev) => [...prev, errorReply]);
    }
  };

  const completeTask = async (task_id) => {
    setLoading(true);
    setError("");
    try {
      const res = await fetch(`${API_BASE}/complete-task`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_id: user.user_id, task_id }),
      });
      if (!res.ok) throw new Error("Could not complete task");
      const data = await res.json();
      const updatedStreak = data.streak != null ? data.streak : streak + 1;
      const updatedUser = {
        ...user,
        level: data.new_level,
        xp: data.xp,
        streak: updatedStreak,
      };
      localStorage.setItem("user", JSON.stringify(updatedUser));
      setUser(updatedUser);
      setStreak(updatedStreak);
      fetchTasks(updatedUser.level);
      fetchLeaderboard();
      fetchSubjectProgress(updatedUser.user_id);
      toast.success("Task completed! XP gained.");
    } catch (err) {
      setError(err.message);
      toast.error(err.message);
    } finally {
      setLoading(false);
    }
  };

  const createTask = async () => {
    setError("");

    if (!newTaskTitle || !newTaskXp || !newTaskLevel) {
      toast.error("Task title, XP, and level are required.");
      return;
    }

    let xp = parseInt(newTaskXp, 10);
    let level = parseInt(newTaskLevel, 10);

    if (Number.isNaN(xp) || Number.isNaN(level)) {
      toast.error("XP and level must be numbers.");
      return;
    }

    try {
      const res = await fetch(`${API_BASE}/tasks`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title: newTaskTitle.trim(), xp, level }),
      });

      if (!res.ok) {
        const body = await res.json();
        throw new Error(body.message || "Failed to create task");
      }

      const data = await res.json();
      setTasks((prev) => [...prev, data.task]);
      setNewTaskTitle("");
      setNewTaskXp("");
      setNewTaskLevel("");
      toast.success("Task created successfully!");
    } catch (err) {
      setError(err.message);
      toast.error(err.message);
    }
  };

  const logout = () => {
    localStorage.removeItem("user");
    setUser(null);
    setTasks([]);
    setError("");
    navigate("/");
  };

  const updateProfile = () => {
    if (!profileName.trim() || !profileEmail.trim()) {
      toast.error("Name and email are required.");
      return;
    }

    const updatedUser = {
      ...user,
      username: profileName.trim(),
      email: profileEmail.trim(),
    };

    setUser(updatedUser);
    localStorage.setItem("user", JSON.stringify(updatedUser));
    setIsEditingProfile(false);
    toast.success("Profile updated successfully!");
  };

  const xpProgress = user ? Math.min(100, ((user.xp % 100) / 100) * 100) : 0;
  const stageName = user ? STAGE_NAMES[user.level] || 'Beginner' : '';

  return (
    <div className="dashboard-page">
      <aside className="dashboard-aside">
        <div className="profile-card">
          <div style={{ display: 'flex', alignItems: 'center' }}>
            <div className="avatar">{(user.username || 'U')[0].toUpperCase()}</div>
            <div>
              <h2>{user.username || `User #${user.user_id}`}</h2>
              <p>{user.email || 'No email set'}</p>
            </div>
          </div>

          <div className="profile-meta">
            <span>Level {user.level} ({stageName})</span>
            <span>Streak {streak} day{streak === 1 ? '' : 's'}</span>
          </div>

          <div className="profile-field">
            <label>Name:</label>
            {isEditingProfile ? (
              <input value={profileName} onChange={(e) => setProfileName(e.target.value)} />
            ) : (
              <span>{profileName}</span>
            )}
          </div>

          <div className="profile-field">
            <label>Email:</label>
            {isEditingProfile ? (
              <input value={profileEmail} onChange={(e) => setProfileEmail(e.target.value)} />
            ) : (
              <span>{profileEmail || 'N/A'}</span>
            )}
          </div>

          {isEditingProfile ? (
            <button className="edit-profile-btn" onClick={updateProfile}>
              Save Profile
            </button>
          ) : (
            <button className="edit-profile-btn" onClick={() => setIsEditingProfile(true)}>
              Edit Profile
            </button>
          )}
        </div>
      </aside>

      <div className="dashboard-main">
        <div className="page-toolbar">
          <h1>GovPrep Hub</h1>
          <button className="logout" onClick={logout}>
            Logout
          </button>
        </div>

        <main className="card">
          <section className="user-panel">
            <div className="meta">
              <p>👤 {user.username || `User #${user.user_id}`}</p>
              <p>🎯 Level {user.level}</p>
              <p>🔥 Streak: {streak} day{streak === 1 ? '' : 's'}</p>
            </div>
            <div className="xp">
              <span>{user.xp} / 100 XP</span>
              <div className="progress-bar">
                <div className="progress" style={{ width: `${xpProgress}%` }}></div>
              </div>
            </div>
          </section>

          {showLevelUnlock && <div className="level-unlock">✨ Level Up! New rewards unlocked! ✨</div>}

          <section className="leaderboard">
            <h2>🏆 Global Leaderboard</h2>
            <p>Compete with coders worldwide!</p>
            <ul>
              {leaderboard.map((entry, index) => (
                <li key={entry.user_id} className={entry.user_id === user.user_id ? 'me' : ''}>
                  <span>#{index + 1}</span> <strong>{entry.username}</strong> - L{entry.level} ({entry.xp} XP)
                </li>
              ))}
            </ul>
          </section>

          <section className="personalized-plan">
            <h2>🤖 AI-Powered Learning Plan</h2>
            <p>Based on your current stage ({stageName}), focus on these next steps:</p>
            <ul>
              {user.level === 1 && (
                <>
                  <li>Read basic NCERTs for Polity, History, and Geography</li>
                  <li>Track daily current affairs summaries (10 mins)</li>
                  <li>Practice foundational Quantitative Aptitude questions</li>
                </>
              )}
              {user.level === 2 && (
                <>
                  <li>Complete subject-specific notes and revision cards</li>
                  <li>Start solving moderate PYQ sets weekly</li>
                  <li>Build daily habit: 1 full mock question set</li>
                </>
              )}
              {user.level >= 3 && (
                <>
                  <li>Focus on advanced MCQs and full PYQ tests</li>
                  <li>Simulate exam conditions with timed quizzes</li>
                  <li>Join peer mentorship for doubt clearing</li>
                </>
              )}
            </ul>
          </section>

          <section className="progress-analytics">
            <h2>📊 Progress Analytics</h2>
            <div className="analytics-grid">
              <div className="analytic-item">
                <h3>XP Progress to Next Level</h3>
                <div className="progress-bar">
                  <div className="progress" style={{ width: `${xpProgress}%` }}></div>
                </div>
                <p>{user.xp} / 100 XP ({xpProgress}% complete)</p>
              </div>
              <div className="analytic-item">
                <h3>Streak Status</h3>
                <p>Current Streak: {streak} days</p>
                <p>Keep it up! 🔥</p>
              </div>
              <div className="analytic-item">
                <h3>Tasks Completed</h3>
                <p>Level {user.level} unlocked!</p>
                <p>Next: Level {user.level + 1}</p>
              </div>
            </div>
          </section>

          <section className="subject-progress">
            <h2>📘 Subject-wise Progress</h2>
            <div className="subject-grid">
              {subjectProgress.length === 0 ? (
                <p>No subject progress recorded yet. Complete tasks to start tracking.</p>
              ) : (
                subjectProgress.map((item) => (
                  <div key={item.subject} className="subject-card">
                    <h3>{item.subject}</h3>
                    <p>Completed tasks: {item.completed_tasks}</p>
                    <p>XP: {item.xp}</p>
                  </div>
                ))
              )}
            </div>
          </section>

          <section className="rewards">
            <h2>🎁 Rewards & Badges</h2>
            <div className="badges-grid">
              {user.level >= 1 && <div className="badge">🚀 Exam Beginner</div>}
              {user.level >= 2 && <div className="badge">📘 Fundamentals Cleared</div>}
              {user.level >= 3 && <div className="badge">🏆 Intermediate Scholar</div>}
              {user.level >= 4 && <div className="badge">💪 Advanced Aspirant</div>}
              {user.level >= 5 && <div className="badge">🎯 Exam Ready</div>}
              {streak >= 7 && <div className="badge">🔥 7-Day Streak</div>}
              {streak >= 30 && <div className="badge">🌟 30-Day Consistency</div>}
            </div>
          </section>

          <section className="chat">
            <h2>🤝 Peer & Mentor Support</h2>
            <div className="chat-box">
              {chatMessages.length === 0 && <p className="chat-empty">Connect with fellow coders and mentors for tips and motivation!</p>}
              {chatMessages.map((msg) => (
                <div key={msg.id} className={`chat-message ${msg.from === 'You' ? 'self' : 'peer'}`}>
                  <span>{msg.from}:</span> {msg.text}
                </div>
              ))}
            </div>
            <div className="chat-input-row">
              <input
                value={chatInput}
                placeholder="Share your progress or ask for help..."
                onChange={(e) => setChatInput(e.target.value)}
                onKeyDown={(e) => { if (e.key === 'Enter') sendMessage(); }}
              />
              <button onClick={sendMessage}>Send</button>
            </div>
          </section>

          <section className="pyq-module">
            <h2>🧠 PYQ Practice (Previous Year Questions)</h2>
            <div className="pyq-controls">
              <label>
                Subject:
                <select value={selectedSubject} onChange={(e) => { setSelectedSubject(e.target.value); }}>
                  <option>Polity</option>
                  <option>History</option>
                  <option>Geography</option>
                  <option>Current Affairs</option>
                  <option>Quantitative Aptitude</option>
                </select>
              </label>
            </div>

            {pyqQuestions.length === 0 ? (
              <p>No PYQ items loaded for {selectedSubject}. Create tasks or add PYQ via backend.</p>
            ) : (
              <div className="pyq-list">
                {pyqQuestions.map((q) => (
                  <article key={q.id} className={`pyq-item ${selectedPyqId === q.id ? 'selected' : ''}`} onClick={() => setSelectedPyqId(q.id)}>
                    <h4>{q.question}</h4>
                    <small>{q.subject}</small>
                  </article>
                ))}
                <div className="pyq-answer">
                  <p>Choose your answer for selected question</p>
                  <input value={selectedPyqAnswer} onChange={(e) => setSelectedPyqAnswer(e.target.value)} placeholder="Option text" />
                  <button onClick={submitPYQAnswer}>Submit Answer</button>
                  {pyqFeedback && <p>{pyqFeedback}</p>}
                </div>
              </div>
            )}
          </section>

          <section className="summary-module">
            <h2>✍️ Quick Study Summarizer</h2>
            <textarea value={summaryText} onChange={(e) => setSummaryText(e.target.value)} placeholder="Paste notes and get a concise summary." />
            <button onClick={requestSummary}>Generate Summary</button>
            {summaryResult && (
              <div className="summary-result">
                <h4>Summary</h4>
                <p>{summaryResult}</p>
              </div>
            )}
          </section>

          <h2>📋 Available Tasks</h2>

        {error && <div className="alert">{error}</div>}

        {loading ? (
          <div className="loader">Loading tasks...</div>
        ) : tasks.length === 0 ? (
          <p className="empty">No tasks available now; complete your current missions to unlock more.</p>
        ) : (
          <div className="task-grid">
            {tasks.map((task) => (
              <article className="task" key={task.id}>
                <h3>{task.title}</h3>
                <p>{task.description || "Complete this task to earn XP."}</p>
                <div className="task-bottom">
                  <span className="task-xp">+{task.xp} XP</span>
                  <button onClick={() => completeTask(task.id)} disabled={loading}>
                    Complete
                  </button>
                </div>
              </article>
            ))}
          </div>
        )}
      </main>
    </div>
  </div>
  );
}

export default DashboardPage;
