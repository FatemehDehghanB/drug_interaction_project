from drug_interaction_project.model.patients import Patient

# لیست اولیه بیماران
patients_db = [
    Patient(name="ali", family="rezai", national_id="0012345678", drugs=["metoprolol", "aspirin"]),
    Patient(name="sara", family="amiri", national_id="0023456789", drugs=["metformin", "atorvastatin"]),
    Patient(name="maryam", family="vahidi", national_id="1234567777", drugs=["sertraline", "alprazolam"]),
    Patient(name="omid", family="akrami", national_id="1234556789", drugs=["amoxicillin", "clavulanic acid"]),
    Patient(name="mohsen", family="sharifi", national_id="1358050800", drugs=["lisinopril", "hydrochlorothiazide"]),
    Patient(name="raha", family="jamshidi", national_id="0313325887", drugs=["salbutamol", "prednisolone"]),
    Patient(name="ehsan", family="dehghan", national_id="0055855789", drugs=["allopurinol", "colchicine"]),
]

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.patients = list(patients_db)
        return cls._instance

    def get_all_patients(self):
        return self.patients

    def add_patient(self, patient):
        for p in self.patients:
            if p.national_id == patient.national_id:
                raise ValueError("Patient with this national ID already exists")
        self.patients.append(patient)