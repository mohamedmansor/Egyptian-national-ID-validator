from datetime import datetime

from django.test import TestCase

from ..validator import NIDValidator


class TestNIDValidator(TestCase):
    def setUp(self):
        pass

    def test_valid_nid(self):
        """Test Case: Send valid NID number
        Expected:
            - Return True
            - message is 'valid'
        """
        nid_number = '27010200202071'
        obj = NIDValidator(nid_number)
        state, message = obj.validate()
        self.assertEqual(state, True)
        self.assertEqual(message, 'valid')

        governate = obj.get_governorate()
        gender = obj.get_gender()
        birthdate = obj.get_birthdate()
        self.assertEqual(str(birthdate), '1970-10-20')
        self.assertEqual(governate, 'Alexandria')
        nid_number = '27010200202061'
        obj = NIDValidator(nid_number)
        state, message = obj.validate()
        gender = obj.get_gender()
        self.assertEqual(gender, 'female')

    def test_invalid_month(self):
        """Test Case: Send invalid month in NID number
        Expected:
            - Return False
            - message is 'Invalid month'
        """
        nid_number = '27070100202071'
        obj = NIDValidator(nid_number)
        state, message = obj.validate()
        self.assertEqual(state, False)
        self.assertEqual(message, 'Invalid month')

    def test_invalid_day(self):
        """Test Case: Send invalid day in NID number
        Expected:
            - Return False
            - message is 'Invalid day'
        """
        nid_number = '27010990202071'
        obj = NIDValidator(nid_number)
        state, message = obj.validate()
        self.assertEqual(state, False)
        self.assertEqual(message, 'Invalid day')

    def test_invalid_length(self):
        """Test Case: Send invalid length in NID number
        Expected:
            - Return False
            - message is 'Invalid length'
        """
        nid_number = '270101002020'
        obj = NIDValidator(nid_number)
        state, message = obj.validate()
        self.assertEqual(state, False)
        self.assertEqual(message, 'Invalid length')

    def test_invalid_governate_code(self):
        """Test Case: Send invalid governate_code in NID number
        Expected:
            - Return False
            - message is 'Invalid governate_code'
        """
        nid_number = '27010105602071'
        obj = NIDValidator(nid_number)
        state, message = obj.validate()
        self.assertEqual(state, False)
        self.assertEqual(message, 'Invalid Governorate code')

    def test_invalid_day_month_combination(self):
        """Test Case: Send invalid day_month_combination in NID number
        Expected:
            - Return False
            - message is 'day is out of range for month'
        """
        nid_number = '29602300202071'
        obj = NIDValidator(nid_number)
        state, message = obj.validate()
        self.assertEqual(state, False)
        self.assertEqual(message, 'day is out of range for month')
