import unittest
from django.test import RequestFactory
from usa_validator.views import USANIDValidationViewSet

class TestUSANIDValidationViewSet(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.view = USANIDValidationViewSet.as_view({'post': 'create'})

    def test_create(self):
        # Test successful request
        request = self.factory.post('/api/v1/us_nid/', {'national_id_number': '123456789'})
        response = self.view(request)
        self.assertEqual(response.status_code, 200)

        # Test unsuccessful request
        request = self.factory.post('/api/v1/us_nid/', {'national_id_number': '12345678'})
        response = self.view(request)
        self.assertEqual(response.status_code, 400)
        
        def test_method_not_allowed(self):
        # Test DELETE method
        request = self.factory.delete('/api/v1/us_nid/')
        response = self.view(request)
        self.assertEqual(response.status_code, 405)
        
        # Test GET method
        request = self.factory.get('/api/v1/us_nid/')
        response = self.view(request)
        self.assertEqual(response.status_code, 405)
        
        # Test PUT method
        request = self.factory.put('/api/v1/us_nid/')
        response = self.view(request)
        self.assertEqual(response.status_code, 405)

if __name__ == '__main__':
    unittest.main()