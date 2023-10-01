import logging

from rest_framework import status, viewsets
from rest_framework.response import Response

from .serializer import USANIDSerializer
from .validator import USANIDValidator


class USANIDValidationViewSet(viewsets.ViewSet):
    serializer_class = USANIDSerializer

    class USANIDValidationViewSet(viewsets.ViewSet):
        serializer_class = USANIDSerializer

        def create(self, request):
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            nid = serializer.validated_data.get("national_id_number")
            nid_validator = USANIDValidator(nid)
            logging.info("USANIDValidator object created with NID: %s", nid)
            state, message = nid_validator.validate()
            if not state:
                return Response(
                    {"details": message}, status=status.HTTP_400_BAD_REQUEST
                )

            {
                "birthdate": nid_validator.get_birthdate(),
                "gender": nid_validator.get_gender(),
                "state": nid_validator.get_state(),
            }
