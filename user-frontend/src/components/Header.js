import React, { useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { AuthContext } from '../App';
import './Header.css';

const Header = () => {
    const navigate = useNavigate();
    const { isAuthenticated, setIsAuthenticated } = useContext(AuthContext);
    const username = localStorage.getItem('username');

    const handleLogout = () => {
        localStorage.removeItem('token');
        localStorage.removeItem('username');
        setIsAuthenticated(false);
        navigate('/login');
    };

    return (
        <header className="header-container">
            <div className="logo-section">
                <h1 className="title">User Details</h1>
            </div>
            {isAuthenticated && (
                <div className="user-section">
                    <div className="user-info">
                        <span className="welcome-text">Welcome, {username}</span>
                        <button onClick={handleLogout} className="logout-button">
                            <i className="fas fa-sign-out-alt"></i> Logout
                        </button>
                    </div>
                </div>
            )}
        </header>
    );
};

export default Header;