from django.test import TestCase
from usa_validator.validator import USANIDValidator
from .factories import USANIDValidatorFactory

class TestUSANIDValidator(TestCase):
    def test_validate(self):
        validator = USANIDValidatorFactory.create()
        self.assertEqual(validator.validate(), (True, "Valid USA NID"))

    def test_get_birthdate(self):
        validator = USANIDValidatorFactory.create()
        self.assertEqual(validator.get_birthdate(), validator.nid[:6])

    def test_get_gender(self):
        validator = USANIDValidatorFactory.create()
        self.assertEqual(validator.get_gender(), 'male' if int(validator.nid[6]) % 2 == 1 else 'female')

    def test_get_state(self):
        validator = USANIDValidatorFactory.create()
        self.assertEqual(validator.get_state(), validator.nid[-2:])

# Removed unittest.main() as it's not needed with Django's test classes.