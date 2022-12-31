"""
Test Django Admin Pannel
"""

from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class AdminSiteTest(TestCase):
    """Test Django Admin"""
    def setUp(self):
        self.client = Client()
        self.admin_user = User.objects.create_superuser(
            email="admin11@admin.com",
            username="admin11",
            password="test@123"
        )
        self.client.force_login(self.admin_user)
        self.user = User.objects.create_user(
            email="user@user.com",
            username="user",
            password="test@123"
        )
    
    def test_user_list_works(self):
        """Testing list of users"""
        url = reverse("admin:user_user_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.user.username)
        self.assertContains(res, self.user.email)
        self.assertContains(res, self.user.is_staff)
        self.assertContains(res, self.user.email_verified)
    
    def test_user_add_works(self):
        """Test add new user works"""
        url = reverse("admin:user_user_add")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
    
    def test_user_update_works(self):
        """Test user update works"""
        url = reverse("admin:user_user_change", args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
