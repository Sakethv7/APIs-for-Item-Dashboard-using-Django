from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User



class APITestCase(APITestCase): # Inherits from APITestCase to create a new testcase for API endpoints
    def setUp(self): # setUp is run before each test method to set up any objects needed for the tests
        self.user = User.objects.create_user(username='testuser', password='12345') # Creates a test user that can be used in subsequent tests

    def test_login(self): # Tests the login functionality to ensure it works as expected
        url = reverse('login')  # Uses the reverse function to find the URL for the 'login' view
        data = {'username': 'testuser', 'password': '12345'}   # The credentials for the test user
        response = self.client.post(url, data, format='json')    # Sends a POST request with the user data in JSON format
        self.assertEqual(response.status_code, status.HTTP_200_OK) # Asserts that the status code of the response should be 200 OK

    def test_signup(self):   # Tests the signup functionality to ensure a new user can register
        url = reverse('signup')
        data = {'username': 'newuser', 'password': '54321'} # The data for creating a new user
        response = self.client.post(url, data, format='json') # Sends a POST request to create a new user
        self.assertEqual(response.status_code, status.HTTP_200_OK) # Checks that the response status code is 200 OK

    def test_test_token(self):  # Tests the token retrieval to ensure authenticated users can receive a token
        url = reverse('test_token') # URL for the 'test_token' view
        self.client.force_login(self.user) # Forces authentication of the test user
        response = self.client.get(url) # Sends a GET request to retrieve the token
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Asserts that the response should be 200 OK, indicating token retrieval was successful


    def test_get_all_items(self): # Tests the retrieval of all items, ensuring the endpoint works for authenticated users
        url = reverse('get_all_items')
        self.client.force_login(self.user) # Forces authentication of the test user
        response = self.client.get(url)   # Sends a GET request to retrieve all items
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Asserts that the response status code is 200 OK

    def test_get_all_items_by_parameters(self): # Tests the retrieval of items by certain parameters to ensure the functionality is working
        url = reverse('get_all_items_by_parameters') # URL for 'get_all_items_by_parameters' view
        self.client.force_login(self.user) # Forces authentication of the test user
        response = self.client.get(url) # Sends a GET request to retrieve items based on specified parameters
        self.assertEqual(response.status_code, status.HTTP_200_OK)   # Asserts that the response status code is 200 OK
