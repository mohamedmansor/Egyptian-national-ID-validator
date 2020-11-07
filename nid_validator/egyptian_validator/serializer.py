from django.core.exceptions import ValidationError
from rest_framework import serializers


def validate_nid(nid):
    """
    Check that national ID is valid.
    criteria:
        - length is 14 numbers
        - it shouldn't start with 0
    """
    if len(nid) != 14:
        raise ValidationError('NID should be 14 length')
    if int(nid[0]) < 1:
        raise ValidationError('Invalid NID! It cannot start with 0')
    return True

class NIDSerializer(serializers.Serializer):
    national_id_number = serializers.CharField(required=False, validators=[validate_nid])

