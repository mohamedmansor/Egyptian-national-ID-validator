from rest_framework import serializers

def validate_usa_nid(nid):
    """
    Check that the USA NID is valid.
    criteria:
        - length is 9 numbers
        - it shouldn't start with 0
    """
    if len(nid) != 9:
        raise serializers.ValidationError('USA NID should be 9 length')
    if int(nid[0]) < 1:
        raise serializers.ValidationError('Invalid USA NID! It cannot start with 0')
    return True

class USANIDSerializer(serializers.Serializer):
    national_id_number = serializers.CharField(required=True, validators=[validate_usa_nid])