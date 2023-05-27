import sys
import os

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from flask import url_for
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_index_redirect(self):
        with self.app:
            response = self.app.get('/')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, 'http://localhost/login')

    def test_login_valid_credentials(self):
        with self.app:
            response = self.app.post('/login', data={'username': 'john', 'password': 'password'}, follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Welcome, john!', response.data)

    def test_dashboard(self):
        with self.app:
            response = self.app.get('/dashboard/john')
            self.assertEqual(response.status_code, 200)
            # Add additional assertions for dashboard content

if __name__ == '__main__':
    unittest.main()
