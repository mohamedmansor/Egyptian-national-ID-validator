from datetime import datetime

GOVERNORATES = {
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


class NIDValidator:
    def __init__(self, nid):
        self.nid = nid

    def validate(self):
        """
        validate NID data
        """
        message = 'valid'
        if len(self.nid) != 14:
            message = 'Invalid length'
            return False, message

        self.month = int(self.nid[3:5])
        if not self.month in range(1, 13):
            message = 'Invalid month'
            return False, message

        self.day = int(self.nid[5:7])
        if not self.day in range(1, 32):
            message = 'Invalid day'
            return False, message

        self.code = self.nid[7:9]
        if not self.code in GOVERNORATES.keys():
            message = 'Invalid Governorate code'
            return False, message

        self.century = self.get_birth_century()
        self.year = f'{self.century}{self.nid[1:3]}'
        self.birth_date = f"{self.nid[5:7]}/{self.nid[3:5]}/{self.year}"
        try:
            datetime.strptime(self.birth_date, '%d/%m/%Y')
        except ValueError:
            message = 'day is out of range for month'
            return False, message

        return True, message

    def get_birthdate(self):
        """
        return birthdate from NID
        """
        day = self.nid[5:7]
        month = self.nid[3:5]
        century = self.get_birth_century()
        year = f'{century}{self.nid[1:3]}'
        date_str = f"{day}/{month}/{year}"
        birthday = datetime.strptime(date_str, '%d/%m/%Y')
        return birthday.date()

    def get_birth_century(self):
        """
        return century of birth.
        """
        century_code = int(self.nid[0])
        return century_code + 17

    def get_governorate(self):
        """
        get Governorate from NID
        """

        code = self.nid[7:9]
        return GOVERNORATES.get(code)

    def get_gender(self):
        """
        return gender
        """
        if int(self.nid[12]) % 2 == 0:
            return 'female'
        return 'male'
