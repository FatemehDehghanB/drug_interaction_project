from drug_interaction_project.model.patients import Patient


class InteractionService:
    def __init__(self):
        # local database of major interactions
        self.local_db = {
            ("aspirin", "warfarin"): ("Major", "خطر خونریزی شدید"),
            ("ibuprofen", "warfarin"): ("Major", "خطر خونریزی گوارشی"),
            ("naproxen", "ibuprofen"): ("Major", "دو NSAID نباید همزمان مصرف شوند"),
            ("tramadol", "sertraline"): ("Major", "خطر سندرم سروتونین"),
            ("calcium carbonate", "levothyroxine"): ("Moderate", "کلسیم جذب لووتیروکسین را کم می‌کند"),
            ("iron sulfate", "levothyroxine"): ("Moderate", "آهن جذب لووتیروکسین را کم می‌کند"),
            ("glibenclamide", "metformin"): ("Moderate", "خطر افت قند خون"),
        }
        print("[INFO] Interaction Service is ready (Local DB).")

    def check_interaction(self, drug1, drug2):
        d1, d2 = drug1.lower().strip(), drug2.lower().strip()
        if d1 == d2:
            return None

        key = tuple(sorted([d1, d2]))
        return self.local_db.get(key, None)

    def check_patient_with_new_drug(self, patient, new_drug_name):
        conflicts = []
        for existing in patient.get_drug_names():
            result = self.check_interaction(existing, new_drug_name)
            if result:
                conflicts.append((existing, result[0], result[1]))
        return conflicts