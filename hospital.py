class Patient:
    def __init__(self, pid, name, age, disease):
        self.pid = pid
        self.name = name
        self.age = age
        self.disease = disease
        self.admitted = True

    def __str__(self):
        status = "Admitted" if self.admitted else "Discharged"
        return f"{self.pid} - {self.name}, Age {self.age}, Disease: {self.disease} [{status}]"


class Hospital:
    def __init__(self):
        self.patients = {}

    def add_patient(self, pid, name, age, disease):
        if pid in self.patients:
            print("⚠️ Patient ID already exists!")
        else:
            self.patients[pid] = Patient(pid, name, age, disease)
            print("✅ Patient added!")

    def view_patients(self):
        if not self.patients:
            print("📭 No patients yet.")
        else:
            for patient in self.patients.values():
                print(patient)

    def search_patient(self, pid):
        return self.patients.get(pid, "❌ Patient not found!")

    def discharge_patient(self, pid):
        if pid in self.patients:
            self.patients[pid].admitted = False
            print("🏥 Patient discharged!")
        else:
            print("❌ Patient not found!")


# Example
h = Hospital()
h.add_patient(1, "Ali", 25, "Flu")
h.add_patient(2, "Sara", 30, "Fever")
h.view_patients()
print(h.search_patient(1))
h.discharge_patient(2)
h.view_patients()
