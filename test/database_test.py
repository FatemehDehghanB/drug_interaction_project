from drug_interaction_project.model.patients import Patient
from drug_interaction_project.data_access.database import Database

db = Database()
#addin new patient
try:
    new_patient = Patient("raza" , "ahmadi" , "1234567891" , ["paracetamol"])
    db.add_patient(new_patient)
    print("new patient added.")
except ValueError as e:
    print(e)

#duplicate national id
try:
    new_patient = Patient("raza" , "ahmadi" , "0012345678" , ["paracetamol"])
    db.add_patient(new_patient)
    print("new patient added.")
except ValueError as e:
    print("intentional error:" , e)