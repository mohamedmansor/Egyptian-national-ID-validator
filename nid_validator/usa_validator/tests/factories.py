import factory
from usa_validator.validator import USANIDValidator

class USANIDValidatorFactory(factory.Factory):
    class Meta:
        model = USANIDValidator

    nid =