import unittest
from backend.app import create_app
import os

class TestApp(unittest.TestCase):
    def setUp(self):
        # Store original env var
        self.original_flask_debug = os.getenv('FLASK_DEBUG')

    def tearDown(self):
        # Restore original env var
        if self.original_flask_debug:
            os.environ['FLASK_DEBUG'] = self.original_flask_debug
        else:
            os.environ.pop('FLASK_DEBUG', None)

    def test_create_app_development(self):
        os.environ['FLASK_DEBUG'] = '1'
        app = create_app()
        self.assertTrue(app.debug)

    def test_create_app_production(self):
        os.environ['FLASK_DEBUG'] = '0'
        app = create_app()
        self.assertFalse(app.debug)

    def test_create_app_no_env(self):
        if 'FLASK_DEBUG' in os.environ:
            del os.environ['FLASK_DEBUG']
        app = create_app()
        self.assertFalse(app.debug)

    def test_create_app_invalid_env(self):
        os.environ['FLASK_DEBUG'] = 'invalid'
        app = create_app()
        self.assertFalse(app.debug)

if __name__ == '__main__':
    unittest.main()