from drug_interaction_project.business_logic.interaction_service import InteractionService
from drug_interaction_project.model.patients import Patient


service = InteractionService()

#new patient
p1 = Patient(name="Ali", family="Rezaei", national_id="0012345678", drugs=["aspirin"])

#interaction with warfarin; major interaction
print("warfarin interaction:")
result1 = service.check_patient_with_new_drug(p1, "warfarin")
print(f"result: {result1}")

print("--------------------------------------------")

# interaction with paracetamol; without interaction
print("paracetamol interaction:")
result2 = service.check_patient_with_new_drug(p1, "paracetamol")
print(f"result: {result2}")