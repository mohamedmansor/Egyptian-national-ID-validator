from datetime import datetime

from rest_framework import status, viewsets
from rest_framework.response import Response

from .serializer import NIDSerializer


class NIDValidationViewSet(viewsets.ViewSet):
    serializer_class = NIDSerializer

    def create(self, request):
        serializer = NIDSerializer(data=self.request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        nid = serializer.validated_data.get('national_id_number')
        birthdate = get_birthdate(nid)
        gender = get_gender(nid)
        governorate = get_governorate(nid)
        if not governorate:
            return Response({"details": "invalid governorate code"}, status=status.HTTP_400_BAD_REQUEST)
        
        response = {
            'birthdate': birthdate,
            'gender': gender,
            'governorate': governorate
        }
        
        return Response(response, status=status.HTTP_200_OK)




def birth_century(century_code):
    """
    return century of birth.
    """
    return  int(century_code) + 17


def get_birthdate(nid):
    """
    extract the age and birthdate from nid number
    """
    month = nid[3:5]
    day = nid[5:7]
    century = str(birth_century(nid[0]))
    year = century + nid[1:3]

    date_str = "{0}/{1}/{2}".format(day, month, year)
    birthday = datetime.strptime(date_str, '%d/%m/%Y')
    return birthday.date()

def get_governorate(nid):
    """
    get Governorate from NID
    """
    governorates = {
        '01': 'Cairo',
        '02': 'Alexandria',
        '03': 'Port Said',
        '04': 'Suez',
        '11': 'Damietta',
        '12': 'Dakahlia',
        '13': 'Ash Sharqia',
        '14': 'Kaliobeya',
        '15': 'Kafr El - Sheikh',
        '16': 'Gharbia',
        '17': 'Monoufia',
        '18': 'El Beheira',
        '19': 'Ismailia',
        '21': 'Giza',
        '22': 'Beni Suef',
        '23': 'Fayoum',
        '24': 'El Menia',
        '25': 'Assiut',
        '26': 'Sohag',
        '27': 'Qena',
        '28': 'Aswan',
        '29': 'Luxor',
        '31': 'Red Sea',
        '32': 'New Valley',
        '33': 'Matrouh',
        '34': 'North Sinai',
        '35': 'South Sinai',
        '88': 'Foreign'
    }
    code = nid[7:9]
    if not governorates.get(code, None):
        return False
    return governorates.get(code)

def get_gender(nid):
    """
    return gender
    """
    if int(nid[12]) %2 == 0:
        return 'female'
    return 'male'
