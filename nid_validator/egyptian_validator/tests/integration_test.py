from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class NIDTestAPI(TestCase):
    def setUp(self):
        self.url = reverse('validate-list')

    def test_api_return_200(self):
        """Test Case:
        - API return 200
        - NID data is valid
            'birthdate': '1970-10-20'
            'gender': 'male'
            'governorate': 'Alexandria'
        """
        body = {
            "national_id_number": "27010200202071"
        }
        response = self.client.post(self.url, body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = response.json()
        self.assertEqual(response.get('birthdate'), '1970-10-20')
        self.assertEqual(response.get('gender'), 'male')
        self.assertEqual(response.get('governorate'), 'Alexandria')

    def test_api_invalid_request_body(self):
        """Test Case: Send invalid request body to API.
        Expected:
            - API return serializer error
            - response with errors list
        """
        body = {
            "national_id": "27010200202071"
        }
        response = self.client.post(self.url, body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = response.json()
        self.assertEqual(response.get('national_id_number'), ['This field is required.'])

    def test_api_invalid_nid_length(self):
        """Test Case: Send invalid NID number to API.
        Expected:
            - Return 400 bad request
            - Error details
        """
        body = {
            "national_id_number": "2701022020207"
        }
        response = self.client.post(self.url, body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = response.json()
        self.assertEqual(response.get('national_id_number'), ['NID should be 14 length'])

    def test_api_invalid_nid_month(self):
        """Test Case: Send invalid NID number to API.
        Expected:
            - Return 400 bad request
            - Error details
        """
        body = {
            "national_id_number": "27050200202071"
        }
        response = self.client.post(self.url, body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = response.json()
        self.assertEqual(response.get('details'), 'Invalid month')

    def test_api_invalid_nid_day(self):
        """Test Case: Send invalid NID number to API.
        Expected:
            - Return 400 bad request
            - Error details
        """
        body = {
            "national_id_number": "27010500202071"
        }
        response = self.client.post(self.url, body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = response.json()
        self.assertEqual(response.get('details'), 'Invalid day')

    def test_api_invalid_nid_day_month_combination(self):
        """Test Case: Send invalid NID number to API. Invalid day in month.
        ex: 31/02/2020
        Expected:
            - Return 400 bad request
            - Error details
        """
        body = {
            "national_id_number": "29602300202071"
        }
        response = self.client.post(self.url, body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = response.json()
        self.assertEqual(response.get('details'), 'day is out of range for month')

    def test_api_invalid_nid_governate_code(self):
        """Test Case: Send invalid NID number to API.
        Expected:
            - Return 400 bad request
            - Error details
        """
        body = {
            "national_id_number": "27010105602071"
        }
        response = self.client.post(self.url, body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = response.json()
        self.assertEqual(response.get('details'), 'Invalid Governorate code')
