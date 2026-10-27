from drug_interaction_project.tools.validation import Validator
from drug_interaction_project.model.drugs import Drug


class Patient:
    def __init__(self, name, family, national_id, drugs=None):
        self.name = name
        self.family = family
        self.national_id = national_id
        self._drugs = [Drug(d) if isinstance(d, str) else d for d in (drugs or [])]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        Validator.name_validator(new_name)
        self._name = new_name

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, new_family):
        Validator.family_validator(new_family)
        self._family = new_family

    @property
    def national_id(self):
        return self._national_id

    @national_id.setter
    def national_id(self, new_national_id):
        Validator.national_id_validator(new_national_id)
        self._national_id = new_national_id

    @property
    def drugs(self):
        return self._drugs
    def add_drug(self, drug):
        if isinstance(drug, str):
            drug = Drug(drug)
        self._drugs.append(drug)

    def get_drug_names(self):
        return [d.drug for d in self._drugs]

    def __repr__(self):
        return f"Patient({self.name} , {self.family} , {self.national_id} , {self.drugs})"

    def remove_drug(self, drug_name):
        for i, d in enumerate(self._drugs):
            if d.drug == drug_name:
                del self._drugs[i]
                return True
        return False