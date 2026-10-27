from tkinter import *
from tkinter import messagebox
from drug_interaction_project.business_logic.interaction_service import InteractionService


class PatientDashboard:
    def __init__(self, patient, db):
        self.patient = patient
        self.service = InteractionService()

        self.win = Toplevel()
        self.win.title(f"Patient Dashboard: {patient.name} {patient.family}")
        self.win.geometry("500x450")

        self.listbox = Listbox(self.win, width=60, height=10)
        self.listbox.pack(pady=10)

        frame_buttons = Frame(self.win)
        frame_buttons.pack(pady=5)
        Button(frame_buttons, text="Delete Selected", command=self.delete_drug, bg="#f44336", fg="white").pack(
            side=LEFT, padx=5)
        Button(frame_buttons, text="Edit Selected", command=self.edit_drug, bg="#FF9800", fg="white").pack(side=LEFT,
                                                                                                           padx=5)

        frame_bottom = Frame(self.win)
        frame_bottom.pack(pady=15)
        Label(frame_bottom, text="New Drug:").pack(side=LEFT, padx=5)
        self.drug_entry = Entry(frame_bottom, width=20)
        self.drug_entry.pack(side=LEFT, padx=5)
        Button(frame_bottom, text="Add & Check", command=self.add_drug, bg="#4CAF50", fg="white").pack(side=LEFT,
                                                                                                       padx=10)

        self.load_drugs()

    def load_drugs(self):
        self.listbox.delete(0, END)
        for drug in self.patient.get_drug_names():
            self.listbox.insert(END, drug)

    def add_drug(self):
        new_drug = self.drug_entry.get().strip().lower()
        if not new_drug:
            messagebox.showwarning("Warning", "Please enter the drug's name!")
            return

        conflicts = self.service.check_patient_with_new_drug(self.patient, new_drug)

        if conflicts:
            existing_drug = conflicts[0][0]
            severity = conflicts[0][1]
            description = conflicts[0][2]
            msg = f"Interaction found between {new_drug} and {existing_drug}.\n\nSeverity: {severity}\nDetails: {description}"
            messagebox.showerror("Interaction Error", msg)
        else:
            self.patient.add_drug(new_drug)
            self.load_drugs()
            self.drug_entry.delete(0, END)
            messagebox.showinfo("Success", f"{new_drug} successfully added.")

    def delete_drug(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a drug to delete.")
            return

        drug_name = self.listbox.get(selection[0])
        if self.patient.remove_drug(drug_name):
            self.load_drugs()
            messagebox.showinfo("Success", f"{drug_name} deleted.")

    def edit_drug(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a drug to edit.")
            return

        old_drug = self.listbox.get(selection[0])

        edit_win = Toplevel(self.win)
        edit_win.title("Edit Drug")
        edit_win.geometry("300x150")

        Label(edit_win, text=f"Editing: {old_drug}").pack(pady=10)
        new_entry = Entry(edit_win, width=20)
        new_entry.pack(pady=5)
        new_entry.insert(0, old_drug)

        def save_edit():
            new_drug = new_entry.get().strip().lower()
            if not new_drug:
                return

            conflicts = []
            for d in self.patient.drugs:
                if d.drug != old_drug:
                    res = self.service.check_interaction(d.drug, new_drug)
                    if res:
                        conflicts.append((d.drug, res[0], res[1]))

            if conflicts:
                messagebox.showerror("Interaction Error", f"{new_drug} has conflicts with other drugs!")
            else:
                for d in self.patient.drugs:
                    if d.drug == old_drug:
                        d.drug = new_drug
                        break
                self.load_drugs()
                edit_win.destroy()
                messagebox.showinfo("Success", "Drug updated successfully.")

        Button(edit_win, text="Save", command=save_edit, bg="#4CAF50", fg="white").pack(pady=10)