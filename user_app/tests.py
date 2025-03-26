from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.utils import timezone
from datetime import timedelta
from .models import User, Profile, Session, Role, ActivityLog

class UserTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword123',
            'phone_number': '1234567890'
        }
        self.user = User.objects.create_user(**self.user_data)
        self.client.force_authenticate(user=self.user)

    def test_create_user(self):
        new_user_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword123',
            'phone_number': '0987654321'
        }
        response = self.client.post('/users/', new_user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_user_login(self):
        login_data = {
            'email': self.user_data['email'],
            'password': self.user_data['password']
        }
        response = self.client.post('/users/login/', login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_profile(self):
        response = self.client.get(f'/profiles/{self.user.profile.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ProfileTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)
        self.profile = Profile.objects.get(user=self.user)

    def test_update_profile(self):
        data = {
            'bio': 'Test bio',
            'location': 'Test location'
        }
        response = self.client.patch(f'/profiles/{self.profile.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['bio'], 'Test bio')

class SessionTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)
        self.session_data = {
            'session_token': 'test_token',
            'expires_at': timezone.now() + timedelta(days=1)
        }

    def test_create_session(self):
        response = self.client.post('/sessions/', self.session_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class RoleTests(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass123'
        )
        self.client.force_authenticate(user=self.admin_user)
        self.role_data = {
            'role_name': 'Test Role',
            'permissions': {'create': True, 'read': True}
        }

    def test_create_role(self):
        response = self.client.post('/roles/', self.role_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityLogTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)
        self.activity_data = {
            'activity_type': 'TEST_ACTIVITY',
            'details': 'Test activity details'
        }

    def test_create_activity_log(self):
        response = self.client.post('/activitylogs/', self.activity_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)