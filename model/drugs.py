from drug_interaction_project.tools.validation import Validator

class Drug:
    def __init__(self , drug:str):
        self.drug = drug

    @property
    def drug(self):
        return self._drug

    @drug.setter
    def drug(self, new_drug):
        Validator.drug_validator(new_drug)
        self._drug =new_drug.lower().strip()

    def __str__(self):
        return self._drug

    def __repr__(self):
        return f"{self._drug}"