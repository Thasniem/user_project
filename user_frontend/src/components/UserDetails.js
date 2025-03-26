import React, { useEffect, useState } from 'react';
import Layout from './Layout';
import './UserDetails.css';

const UserDetails = () => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    // Replace with actual API call
    const fetchUserDetails = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/user-details/', {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          }
        });
        const data = await response.json();
        setUser(data);
      } catch (error) {
        console.error('Error fetching user details:', error);
      }
    };

    fetchUserDetails();
  }, []);

  return (
    <Layout>
      <div className="user-details">
        <h2>User Details</h2>
        {user ? (
          <div className="user-info-card">
            <div className="info-row">
              <label>ID:</label>
              <span>{user.id}</span>
            </div>
            <div className="info-row">
              <label>Name:</label>
              <span>{user.name}</span>
            </div>
            <div className="info-row">
              <label>Email:</label>
              <span>{user.email}</span>
            </div>
            <div className="info-row">
              <label>Phone:</label>
              <span>{user.phone}</span>
            </div>
          </div>
        ) : (
          <p>Loading user details...</p>
        )}
      </div>
    </Layout>
  );
};

export default UserDetails;