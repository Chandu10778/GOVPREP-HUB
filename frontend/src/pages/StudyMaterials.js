import React, { useState, useEffect, useCallback } from 'react';
import { toast } from 'react-toastify';
import ReactQuill from 'react-quill';
import { ChevronRight, BookOpen, Award, X, Plus } from 'lucide-react';
import '../styles/StudyMaterials.css';

const API_BASE = process.env.REACT_APP_API_URL || 'http://127.0.0.1:5000';

const SUBJECT_TABS = ['Polity', 'History', 'Geography', 'Quantitative Aptitude'];
const SUBJECTS = ['Polity', 'History', 'Geography', 'Current Affairs', 'Quantitative Aptitude'];

function StudyMaterials({ user, setUser }) {
  const [selectedSubject, setSelectedSubject] = useState('Polity');
  const [materials, setMaterials] = useState([]);
  const [selectedMaterial, setSelectedMaterial] = useState(null);
  const [showReader, setShowReader] = useState(false);
  const [showAddForm, setShowAddForm] = useState(false);
  const [completedMaterials, setCompletedMaterials] = useState(new Set());
  const [loading, setLoading] = useState(false);
  const [formData, setFormData] = useState({
    title: '',
    subject: 'Polity',
    content: '',
    level: 'Beginner',
    xp_reward: 15
  });

  // Fetch materials by subject
  const fetchMaterials = useCallback(async () => {
    try {
      setLoading(true);
      const res = await fetch(`${API_BASE}/materials/${selectedSubject}/user/${user?.user_id}`);
      if (!res.ok) throw new Error('Failed to fetch materials');
      const data = await res.json();
      setMaterials(data);
    } catch (err) {
      toast.error(err.message);
    } finally {
      setLoading(false);
    }
  }, [selectedSubject, user?.user_id]);

  const fetchUserProgress = useCallback(async () => {
    try {
      const res = await fetch(`${API_BASE}/user/${user?.user_id}/material-progress`);
      if (res.ok) {
        const data = await res.json();
        const completed = new Set(data.map(p => p.material_id));
        setCompletedMaterials(completed);
      }
    } catch (err) {
      console.error('Error fetching progress:', err);
    }
  }, [user?.user_id]);

  useEffect(() => {
    if (user?.user_id) {
      fetchMaterials();
      fetchUserProgress();
    }
  }, [fetchMaterials, fetchUserProgress, user?.user_id]);

  const handleSelectMaterial = async (material) => {
    try {
      const res = await fetch(`${API_BASE}/materials/content/${material.id}`);
      if (!res.ok) throw new Error('Failed to fetch material');
      const data = await res.json();
      setSelectedMaterial(data);
      setShowReader(true);
    } catch (err) {
      toast.error(err.message);
    }
  };

  const handleMarkAsCompleted = async () => {
    if (!selectedMaterial || !user?.user_id) return;

    try {
      const res = await fetch(`${API_BASE}/materials/progress`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          user_id: user.user_id,
          material_id: selectedMaterial.id
        })
      });

      if (!res.ok) throw new Error('Failed to update progress');
      const data = await res.json();

      setCompletedMaterials(new Set([...completedMaterials, selectedMaterial.id]));
      setUser(prev => ({
        ...prev,
        xp: data.total_xp
      }));

      toast.success(`✅ Material completed! +${data.xp_earned} XP`);
    } catch (err) {
      toast.error(err.message);
    }
  };

  const handleAddMaterial = async () => {
    if (!formData.title || !formData.content) {
      toast.error('Please fill in title and content');
      return;
    }

    try {
      setLoading(true);
      const res = await fetch(`${API_BASE}/materials`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          title: formData.title,
          subject: formData.subject,
          content: formData.content,
          level: formData.level,
          xp_reward: formData.xp_reward
        })
      });

      if (!res.ok) throw new Error('Failed to create material');

      toast.success('Material added successfully!');
      setFormData({ title: '', subject: 'Polity', content: '', level: 'Beginner', xp_reward: 15 });
      setShowAddForm(false);
      fetchMaterials();
    } catch (err) {
      toast.error(err.message);
    } finally {
      setLoading(false);
    }
  };

  const getWikipediaUrl = (title) => {
    if (!title) return '';
    return `https://en.wikipedia.org/w/index.php?search=${encodeURIComponent(title)}`;
  };

  return (
    <div className="study-materials">
      <div className="study-header">
        <div className="study-title-section">
          <BookOpen className="icon" size={32} />
          <div>
            <h1>📚 Study Materials</h1>
            <p>Master Government Exam Topics with Structured Content</p>
          </div>
        </div>
        <button 
          className="btn-add-material"
          onClick={() => setShowAddForm(!showAddForm)}
        >
          <Plus size={20} /> Add Material
        </button>
      </div>

      {showAddForm && (
        <div className="add-material-card">
          <div className="form-header">
            <h3>Add New Study Material</h3>
            <button className="close-btn" onClick={() => setShowAddForm(false)}>
              <X size={20} />
            </button>
          </div>
          
          <div className="form-group">
            <label>Title</label>
            <input
              type="text"
              placeholder="e.g., Indian Constitution Overview"
              value={formData.title}
              onChange={(e) => setFormData({ ...formData, title: e.target.value })}
            />
          </div>

          <div className="form-row">
            <div className="form-group">
              <label>Subject</label>
              <select
                value={formData.subject}
                onChange={(e) => setFormData({ ...formData, subject: e.target.value })}
              >
                {SUBJECTS.map(s => <option key={s} value={s}>{s}</option>)}
              </select>
            </div>
            <div className="form-group">
              <label>Level</label>
              <select
                value={formData.level}
                onChange={(e) => setFormData({ ...formData, level: e.target.value })}
              >
                <option value="Beginner">Beginner</option>
                <option value="Intermediate">Intermediate</option>
                <option value="Advanced">Advanced</option>
              </select>
            </div>
            <div className="form-group">
              <label>XP Reward</label>
              <input
                type="number"
                min="5"
                max="100"
                value={formData.xp_reward}
                onChange={(e) => setFormData({ ...formData, xp_reward: parseInt(e.target.value) })}
              />
            </div>
          </div>

          <div className="form-group">
            <label>Content (Rich Text)</label>
            <ReactQuill
              theme="snow"
              value={formData.content}
              onChange={(content) => setFormData({ ...formData, content })}
              placeholder="Write your study material here... You can use formatting, lists, and more!"
              modules={{
                toolbar: [
                  [{ 'header': [1, 2, 3, false] }],
                  ['bold', 'italic', 'underline', 'strike'],
                  [{ 'list': 'ordered' }, { 'list': 'bullet' }],
                  [{ 'color': [] }, { 'background': [] }],
                  ['blockquote', 'code-block'],
                  ['clean']
                ]
              }}
            />
          </div>

          <button 
            className="btn-submit"
            onClick={handleAddMaterial}
            disabled={loading}
          >
            {loading ? 'Saving...' : 'Save Material'}
          </button>
        </div>
      )}

      {/* Subject Tabs */}
      <div className="subject-tabs">
        {SUBJECT_TABS.map(subject => (
          <button
            key={subject}
            className={`subject-tab ${selectedSubject === subject ? 'active' : ''}`}
            onClick={() => setSelectedSubject(subject)}
          >
            {subject}
          </button>
        ))}
      </div>

      <div className="materials-container">
        {/* Materials List */}
        <div className="materials-list">
          <h3>{selectedSubject} Materials</h3>
          {loading ? (
            <div className="loading">Loading materials...</div>
          ) : materials.length === 0 ? (
            <div className="empty-state">
              <p>No materials available for {selectedSubject} yet.</p>
              <p className="hint">Check back soon or add new content!</p>
            </div>
          ) : (
            <div className="materials-grid">
              {materials.map(material => (
                <div
                  key={material.id}
                  className={`material-card ${completedMaterials.has(material.id) ? 'completed' : ''}`}
                  onClick={() => handleSelectMaterial(material)}
                >
                  <div className="material-header">
                    <h4>{material.title}</h4>
                    {completedMaterials.has(material.id) && (
                      <span className="badge completed">✓ Done</span>
                    )}
                  </div>
                  <div className="material-meta">
                    <span className={`level level-${material.level.toLowerCase()}`}>
                      {material.level}
                    </span>
                    <span className="xp-reward">
                      <Award size={14} /> +{material.xp_reward} XP
                    </span>
                  </div>
                  <div className="material-footer">
                    <span className="read-more">Read more <ChevronRight size={16} /></span>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Reader View */}
        {showReader && selectedMaterial && (
          <div className="material-reader">
            <div className="reader-header">
              <div>
                <h2>{selectedMaterial.title}</h2>
                <p className="subject-badge">{selectedMaterial.subject} • {selectedMaterial.level}</p>
              </div>
              <button className="close-btn" onClick={() => setShowReader(false)}>
                <X size={24} />
              </button>
            </div>

            <div className="reader-content">
              <div 
                className="quill-content"
                dangerouslySetInnerHTML={{ __html: selectedMaterial.content }}
              />
            </div>

            <div className="reader-wikipedia-link">
              <a
                href={getWikipediaUrl(selectedMaterial.title)}
                target="_blank"
                rel="noopener noreferrer"
              >
                Learn more on Wikipedia
              </a>
            </div>

            <div className="reader-footer">
              {completedMaterials.has(selectedMaterial.id) ? (
                <div className="completed-badge">
                  ✅ You've completed this material
                </div>
              ) : (
                <button 
                  className="btn-mark-complete"
                  onClick={handleMarkAsCompleted}
                >
                  <Award size={18} /> Mark as Completed +{selectedMaterial.xp_reward} XP
                </button>
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default StudyMaterials;
