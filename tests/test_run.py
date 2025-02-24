import unittest
from backend.run import create_app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        """Setup the Test Client"""
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        
    def test_index_route(self):
        """Test the Index Route"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the WTUS Team System API', response.data)
    
    def test_404_error(self):
        """Test the 404 Error Handler"""
        response = self.client.get('/doesnotexist')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'404 - Page Not Found', response.data)
    
    def test_500_error(self):
        """Test the 500 Error Handler"""
        @self.app.route('/error')
        def error_route():
            raise Exception('Test Exception')

        response = self.client.get('/error')
        self.assertEqual(response.status_code, 500)
        self.assertIn(b'500 - Internal Server Error', response.data)

if __name__ == '__main__':
    unittest.main()
