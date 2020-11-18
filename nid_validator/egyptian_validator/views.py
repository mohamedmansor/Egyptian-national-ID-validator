from datetime import datetime

from rest_framework import status, viewsets
from rest_framework.response import Response

from .serializer import NIDSerializer
from .validator import NIDValidator


class NIDValidationViewSet(viewsets.ViewSet):
    serializer_class = NIDSerializer

    def create(self, request):
        serializer = NIDSerializer(data=self.request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        nid = serializer.validated_data.get('national_id_number')
        nid_validator = NIDValidator(nid)
        state, message = nid_validator.validate()
        if not state:
            return Response({"details": message}, status=status.HTTP_400_BAD_REQUEST)

        response = {
            'birthdate': nid_validator.get_birthdate(),
            'gender': nid_validator.get_gender(),
            'governorate': nid_validator.get_governorate()
        }

        return Response(response, status=status.HTTP_200_OK)
