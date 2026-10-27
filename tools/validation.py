import re

class Validator:
    @staticmethod
    def name_validator(name):
        if not re.match(r"^[a-zA-Z\s]*$" , name):
            raise ValueError("The name is invalid")

    @staticmethod
    def family_validator(family):
        if not re.match(r"^[a-zA-Z\s]*$", family):
            raise ValueError("The last name is invalid")

    @staticmethod
    def national_id_validator(national_id):
        if not re.fullmatch(r"^[0-9]{10}$" , national_id):
            raise ValueError("The national code must consist of ten digits.")


    @staticmethod
    def drug_validator(drug):
        if not re.match(r"^[a-zA-Z\s]*$" , drug):
            raise ValueError("The drug name is invalid.")