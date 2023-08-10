from django.test import TestCase
from usa_validator.validator import USANIDValidator

class TestUSANIDValidator(TestCase):
    def test_validate(self):
        validator = USANIDValidator('123456789')
        self.assertEqual(validator.validate(), (True, "Valid USA NID"))

    def test_get_birthdate(self):
        validator = USANIDValidator('123456789')
        self.assertEqual(validator.get_birthdate(), '123456')

    def test_get_gender(self):
        validator = USANIDValidator('123456789')
        self.assertEqual(validator.get_gender(), 'male')

    def test_get_state(self):
        validator = USANIDValidator('123456789')
        self.assertEqual(validator.get_state(), '89')

# Removed unittest.main() as it's not needed with Django's test classes.