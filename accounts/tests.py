from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm
from django .contrib.auth.models import User

# Create your tests here.
class TestAccountsForms(TestCase):
    
    def test_login_form(self):
        form = UserLoginForm({
            'username': 'admin',
            'password': 'password'
        })
        self.assertTrue(form.is_valid())
        
    def test_login_password_required(self):
        form = UserLoginForm({'username':'admin'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], ['This field is required.'])
    
    def test_login_username_required(self):
        form = UserLoginForm({'password':'pa55w0rd'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ['This field is required.'])
    
    def test_registration_form(self):
        form = UserRegistrationForm({
            'username': 'admin',
            'email': 'admin@example.com',
            'password1':'somepassword',
            'password2':'somepassword'
        })
        self.assertTrue(form.is_valid())
    
    def test_registration_passwords_must_match(self):
        form = UserRegistrationForm({
            'username': 'admin',
            'email': 'admin@example.com',
            'password1':'pa55word1',
            'password2':'pa55word2'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], ['Passwords do not match']) 
    
    
    def test_registration_email_must_be_unique(self):
        User.objects.create_user(
            username='testuser',
            email= 'admin@example.com'
            )
        form = UserRegistrationForm({
        'username': 'admin',
        'email': 'admin@example.com',
        'password1':'somepassword',
        'password2':'somepassword'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['Email addresses must be unique.'])
    
    def test_get_login(self):
        page=self.client.get("/accounts/login")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "accounts/login.html", "base.html")