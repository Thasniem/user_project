import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './DashboardPage.css';

const DashboardPage = () => {
  const [userInfo, setUserInfo] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        const token = localStorage.getItem('token');
        if (!token) {
          navigate('/login');
          return;
        }

        const response = await fetch('http://localhost:8000/api/users/me/', {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        });

        if (!response.ok) {
          throw new Error('Failed to fetch user data');
        }

        const data = await response.json();
        setUserInfo(data);
        setLoading(false);
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    };

    fetchUserData();
  }, [navigate]);

  if (loading) return <div className="loading">Loading...</div>;
  if (error) return <div className="error">{error}</div>;
  if (!userInfo) return <div className="error">No user data available</div>;

  return (
    <div className="dashboard-container">
      <h2 className="dashboard-title">Welcome to Your Dashboard</h2>
      
      <div className="dashboard-content">
        <p>Hello, {userInfo.username}! Here's your account overview.</p>
      </div>

      <div className="dashboard-grid">
        <div className="dashboard-user-info">
          <h3>Personal Information</h3>
          <div className="info-grid">
            <div className="info-item">
              <label>User ID:</label>
              <span>{userInfo.id}</span>
            </div>
            <div className="info-item">
              <label>Username:</label>
              <span>{userInfo.username}</span>
            </div>
            <div className="info-item">
              <label>Email:</label>
              <span>{userInfo.email}</span>
            </div>
            <div className="info-item">
              <label>Phone:</label>
              <span>{userInfo.phone_number || 'Not provided'}</span>
            </div>
            <div className="info-item">
              <label>Member Since:</label>
              <span>{new Date(userInfo.created_at).toLocaleDateString()}</span>
            </div>
          </div>
        </div>

        <div className="dashboard-stats">
          <div className="stat-card">
            <h3 className="stat-title">Account Status</h3>
            <p className="stat-value">Active</p>
            <p className="stat-description">Your account is in good standing</p>
          </div>
          <div className="stat-card">
            <h3 className="stat-title">Last Login</h3>
            <p className="stat-value">Today</p>
            <p className="stat-description">Last accessed at {new Date().toLocaleTimeString()}</p>
          </div>
          <div className="stat-card">
            <h3 className="stat-title">Security Level</h3>
            <p className="stat-value">High</p>
            <p className="stat-description">2FA is enabled</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DashboardPage;