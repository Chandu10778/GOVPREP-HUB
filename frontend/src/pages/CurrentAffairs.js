import React, { useState, useEffect, useCallback } from 'react';
import { toast } from 'react-toastify';
import ReactQuill from 'react-quill';
import { ChevronRight, BookOpen, Award, X, Plus } from 'lucide-react';
import '../styles/StudyMaterials.css';

const API_BASE = process.env.REACT_APP_API_URL || 'http://127.0.0.1:5000';

function CurrentAffairs({ user, setUser }) {
  const [materials, setMaterials] = useState([]);
  const [selectedMaterial, setSelectedMaterial] = useState(null);
  const [showReader, setShowReader] = useState(false);
  const [showAddForm, setShowAddForm] = useState(false);
  const [loading, setLoading] = useState(false);
  const [formData, setFormData] = useState({
    title: '',
    subject: 'Current Affairs',
    content: '',
    level: 'Beginner',
    xp_reward: 15
  });

  const fetchMaterials = useCallback(async () => {
    try {
      setLoading(true);
      const res = await fetch(`${API_BASE}/materials/Current Affairs/user/${user?.user_id}`);
      if (!res.ok) throw new Error('Failed to fetch current affairs updates');
      const data = await res.json();
      setMaterials(data);
    } catch (err) {
      toast.error(err.message);
    } finally {
      setLoading(false);
    }
  }, [user?.user_id]);

  useEffect(() => {
    if (user?.user_id) {
      fetchMaterials();
    }
  }, [fetchMaterials, user?.user_id]);

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

      setUser(prev => ({
        ...prev,
        xp: data.total_xp
      }));
      toast.success(`✅ Material completed! +${data.xp_earned} XP`);
      fetchMaterials();
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
          subject: 'Current Affairs',
          content: formData.content,
          level: formData.level,
          xp_reward: formData.xp_reward
        })
      });

      if (!res.ok) throw new Error('Failed to create material');

      toast.success('Current affairs update added successfully!');
      setFormData({
        title: '',
        subject: 'Current Affairs',
        content: '',
        level: 'Beginner',
        xp_reward: 15
      });
      setShowAddForm(false);
      fetchMaterials();
    } catch (err) {
      toast.error(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="study-materials">
      <div className="study-header">
        <div className="study-title-section">
          <BookOpen className="icon" size={32} />
          <div>
            <h1>📰 Current Affairs</h1>
            <p>Daily updates to keep your exam preparation current and relevant.</p>
          </div>
        </div>
        <button 
          className="btn-add-material"
          onClick={() => setShowAddForm(!showAddForm)}
        >
          <Plus size={20} /> Add Update
        </button>
      </div>

      {showAddForm && (
        <div className="add-material-card">
          <div className="form-header">
            <h3>Add Daily Current Affairs Update</h3>
            <button className="close-btn" onClick={() => setShowAddForm(false)}>
              <X size={20} />
            </button>
          </div>

          <div className="form-group">
            <label>Title</label>
            <input
              type="text"
              placeholder="e.g., Union Budget 2026 Highlights"
              value={formData.title}
              onChange={(e) => setFormData({ ...formData, title: e.target.value })}
            />
          </div>

          <div className="form-row">
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
              placeholder="Write the latest current affairs update here..."
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
            {loading ? 'Saving...' : 'Save Update'}
          </button>
        </div>
      )}

      <div className="materials-container">
        <div className="materials-list">
          <h3>Daily Current Affairs Updates</h3>
          {loading ? (
            <div className="loading">Loading updates...</div>
          ) : materials.length === 0 ? (
            <div className="empty-state">
              <p>No current affairs updates yet.</p>
              <p className="hint">Add a new update so readers can stay exam-ready.</p>
            </div>
          ) : (
            <div className="materials-grid">
              {materials.map(material => (
                <div
                  key={material.id}
                  className="material-card"
                  onClick={() => handleSelectMaterial(material)}
                >
                  <div className="material-header">
                    <h4>{material.title}</h4>
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
                    <span className="read-more">Read update <ChevronRight size={16} /></span>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>

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

            <div className="reader-footer">
              <button 
                className="btn-mark-complete"
                onClick={handleMarkAsCompleted}
              >
                <Award size={18} /> Mark as Completed +{selectedMaterial.xp_reward} XP
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default CurrentAffairs;
