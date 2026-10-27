from tkinter import messagebox
from drug_interaction_project.model.patients import Patient
from drug_interaction_project.view.patient_dashbord_view import PatientDashboard

class PatientController:
    def __init__(self, db, view):
        self.db = db
        self.view = view

    def submit_patient(self):
        name = self.view.name_entry.get().strip()
        family = self.view.family_entry.get().strip()
        national_id = self.view.id_entry.get().strip()

        if not name or not family or not national_id:
            messagebox.showwarning("Warning", "Please fill all fields!")
            return

        for p in self.db.get_all_patients():
            if p.national_id == national_id:
                if p.name == name and p.family == family:
                    messagebox.showinfo("Found", "Patient found. Opening dashboard...")
                    PatientDashboard(p, self.db)
                    return
                else:
                    messagebox.showerror("Error", "Patient with this national ID already exists with a different name!")
                    return

        try:
            new_p = Patient(name=name, family=family, national_id=national_id)
            self.db.add_patient(new_p)
            messagebox.showinfo("Success", "New patient registered.")
            PatientDashboard(new_p, self.db)
        except ValueError as e:
            messagebox.showerror("Validation Error", str(e))