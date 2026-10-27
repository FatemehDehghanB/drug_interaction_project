from tkinter import *
from tkinter import ttk
from drug_interaction_project.data_access.database import Database


class AllPatientsView:
    def __init__(self, root , db):
        self.win = Toplevel(root)
        self.win.title("All Patients Report")
        self.win.geometry("600x400")
        self.db = db

        self.db = Database()

        Label(self.win, text="All Patients & Their Drugs", font=("Arial", 12, "bold")).pack(pady=10)

        # ساخت جدول
        columns = ("name", "family", "national_id", "drugs")
        self.tree = ttk.Treeview(self.win, columns=columns, show="headings", height=15)

        self.tree.heading("name", text="Name")
        self.tree.heading("family", text="Family")
        self.tree.heading("national_id", text="National ID")
        self.tree.heading("drugs", text="Drugs")

        self.tree.column("name", width=100)
        self.tree.column("family", width=100)
        self.tree.column("national_id", width=120)
        self.tree.column("drugs", width=250)

        self.tree.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # پر کردن جدول با دیتا
        for p in self.db.get_all_patients():
            drugs_str = ", ".join(p.get_drug_names())
            self.tree.insert("", END, values=(p.name, p.family, p.national_id, drugs_str))