import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './Sidebar.css';

const Sidebar = () => {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem('token');
    navigate('/login');
  };

  return (
    <div className="sidebar">
      <nav className="sidebar-nav">
        <ul className="sidebar-menu">
          <li>
            <Link to="/profile" className="sidebar-link">
              <i className="fas fa-user"></i>
              Profile
            </Link>
          </li>
          <li>
            <Link to="/dashboard" className="sidebar-link">
              <i className="fas fa-chart-bar"></i>
              Dashboard
            </Link>
          </li>
          <li>
            <Link to="/settings" className="sidebar-link">
              <i className="fas fa-cog"></i>
              Settings
            </Link>
          </li>
          <li>
            <button onClick={handleLogout} className="sidebar-link logout">
              <i className="fas fa-sign-out-alt"></i>
              Logout
            </button>
          </li>
        </ul>
      </nav>
    </div>
  );
};

export default Sidebar;