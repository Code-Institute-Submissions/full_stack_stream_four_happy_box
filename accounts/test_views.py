from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm
from django .contrib.auth.models import User
from django.shortcuts import get_object_or_404

class TestAccountsForms(TestCase):
 
    def test_get_login(self):
        page=self.client.get("/accounts/login")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "accounts/login.html", "base.html")