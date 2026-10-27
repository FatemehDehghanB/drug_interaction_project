from tkinter import *
from drug_interaction_project.data_access.database import Database
from drug_interaction_project.controller.patient_controller import PatientController
from drug_interaction_project.view.all_patient_view import AllPatientsView


class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Drug Interaction System - Login")
        self.root.geometry("400x350")

        self.db = Database()
        self.controller = PatientController(self.db, self)

        Label(self.root, text="Patient Entry", font=("Arial", 14, "bold")).pack(pady=20)

        frame = Frame(self.root)
        frame.pack(pady=10)

        Label(frame, text="Name:").grid(row=0, column=0, pady=5, sticky="e")
        self.name_entry = Entry(frame, width=25)
        self.name_entry.grid(row=0, column=1, pady=5)

        Label(frame, text="Family:").grid(row=1, column=0, pady=5, sticky="e")
        self.family_entry = Entry(frame, width=25)
        self.family_entry.grid(row=1, column=1, pady=5)

        Label(frame, text="National ID:").grid(row=2, column=0, pady=5, sticky="e")
        self.id_entry = Entry(frame, width=25)
        self.id_entry.grid(row=2, column=1, pady=5)

        Button(self.root, text="Submit & Check", command=self.controller.submit_patient, bg="#4CAF50", fg="white").pack(
            pady=15)
        Button(self.root, text="View All Patients", command=lambda: AllPatientsView(self.root, self.db), bg="#2196F3",
               fg="white").pack(pady=5)