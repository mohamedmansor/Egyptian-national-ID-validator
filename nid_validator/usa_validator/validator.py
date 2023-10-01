class USANIDValidator:
    def __init__(self, nid):
        self.nid = nid

    def validate(self):
        if len(self.nid) != 9 or int(self.nid[0]) == 0:
            return False, "Invalid USA NID"
        return True, "Valid USA NID"

    def get_birthdate(self):
        return self.nid[:6]

    def get_gender(self):
        return 'male' if int(self.nid[6]) % 2 == 1 else 'female'

    def get_state(self):
        return self.nid[-2:]