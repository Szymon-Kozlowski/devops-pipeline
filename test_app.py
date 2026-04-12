import unittest
from app import app

class TestMyApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_main_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello World', response.data)

if __name__ == '__main__':
    unittest.main()