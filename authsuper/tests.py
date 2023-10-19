from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from API.models import Product
class AuthSuperTestCase(TestCase):
    def setUp(self):
        # Set up any initial data for your tests, e.g., create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()

    def test_create_product(self):
        url = ('127.0.0.1:8000/api/create/')  # Replace with your actual URL name
        data = {
            'title': 'Test Product',
            'category': 'Test Category',
            'quantity': 10,
            'price': 20.0,
            'desc': 'Test description',
        }
        self.client.login(username='sayf', password='sayf')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        # Add more assertions based on your expected API behavior

# Add more test cases as needed
