import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { CheckCircle2, Circle, LayoutDashboard, Calendar, TrendingUp, ChevronDown, ChevronUp } from 'lucide-react';

const API_BASE = 'http://localhost:8000';

function App() {
  const [phases, setPhases] = useState([]);
  const [stats, setStats] = useState({ total: 0, completed: 0, percent: 0 });
  const [expandedPhases, setExpandedPhases] = useState({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const [planRes, statsRes] = await Promise.all([
        axios.get(`${API_BASE}/plan`),
        axios.get(`${API_BASE}/stats`)
      ]);
      setPhases(planRes.data);
      setStats(statsRes.data);
      
      // Expand first phase by default
      if (planRes.data.length > 0) {
        setExpandedPhases({ [planRes.data[0].id]: true });
      }
      setLoading(false);
    } catch (error) {
      console.error("Error fetching data:", error);
      setLoading(false);
    }
  };

  const toggleTask = async (taskId, currentStatus) => {
    try {
      await axios.patch(`${API_BASE}/tasks/${taskId}?is_completed=${!currentStatus}`);
      fetchData(); // Refresh data to update progress
    } catch (error) {
      console.error("Error updating task:", error);
    }
  };

  const togglePhase = (phaseId) => {
    setExpandedPhases(prev => ({
      ...prev,
      [phaseId]: !prev[phaseId]
    }));
  };

  if (loading) return <div className="loading">Initializing Roadmap...</div>;

  return (
    <div className="app-container">
      <header className="header animate-in">
        <div>
          <h1 className="title">90-Day GenAI Roadmap</h1>
          <p style={{ color: 'var(--text-secondary)' }}>Mastering Generative AI from Foundations to Advanced Deployment</p>
        </div>
        <div className="glass-card stat-card" style={{ padding: '1rem 2rem' }}>
          <div className="stat-value">{Math.round(stats.percent)}%</div>
          <div className="stat-label">Total Progress</div>
        </div>
      </header>

      <div className="stats-grid animate-in" style={{ animationDelay: '0.1s' }}>
        <div className="glass-card stat-card">
          <LayoutDashboard size={32} color="var(--accent-cyan)" style={{ marginBottom: '1rem' }} />
          <div className="stat-value">{stats.completed}</div>
          <div className="stat-label">Tasks Completed</div>
        </div>
        <div className="glass-card stat-card">
          <Calendar size={32} color="var(--accent-purple)" style={{ marginBottom: '1rem' }} />
          <div className="stat-value">{stats.total}</div>
          <div className="stat-label">Total Objectives</div>
        </div>
        <div className="glass-card stat-card">
          <TrendingUp size={32} color="var(--success)" style={{ marginBottom: '1rem' }} />
          <div className="stat-value">{90 - Math.floor(stats.completed / (stats.total/90 || 1))}</div>
          <div className="stat-label">Days Remaining</div>
        </div>
      </div>

      <div className="phases-container animate-in" style={{ animationDelay: '0.2s' }}>
        {phases.map((phase) => (
          <div key={phase.id} className="phase-section">
            <div className="phase-header glass-card" onClick={() => togglePhase(phase.id)}>
              <div style={{ flex: 1 }}>
                <h2 style={{ fontSize: '1.25rem', marginBottom: '0.25rem' }}>{phase.title}</h2>
                <p style={{ fontSize: '0.875rem', color: 'var(--text-secondary)' }}>{phase.description}</p>
              </div>
              {expandedPhases[phase.id] ? <ChevronUp /> : <ChevronDown />}
            </div>

            {expandedPhases[phase.id] && (
              <div className="day-grid">
                {phase.days.map((day) => (
                  <div key={day.id} className="day-card glass-card">
                    <h3 style={{ borderBottom: '1px solid var(--glass-border)', paddingBottom: '0.5rem', marginBottom: '1rem' }}>
                      Day {day.day_number}
                    </h3>
                    {day.tasks.map((task) => (
                      <div 
                        key={task.id} 
                        className="task-item"
                        onClick={() => toggleTask(task.id, task.is_completed)}
                      >
                        <div className={`checkbox ${task.is_completed ? 'checked' : ''}`}>
                          {task.is_completed && <CheckCircle2 size={14} color="white" />}
                        </div>
                        <span className={`task-text ${task.is_completed ? 'completed' : ''}`}>
                          {task.description}
                        </span>
                      </div>
                    ))}
                  </div>
                ))}
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
