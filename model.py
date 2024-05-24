class Model:
    def __init__(self):
        self.data_file = 'data.txt'
        self.load_data()

    def load_data(self):
        self.patients = []
        try:
            with open(self.data_file, 'r') as file:
                for line in file:
                    name, lastname, age, patient_id = line.strip().split(',')
                    self.patients.append({
                        'name': name,
                        'lastname': lastname,
                        'age': age,
                        'id': patient_id
                    })
        except FileNotFoundError:
            pass

    def save_data(self):
        with open(self.data_file, 'w') as file:
            for patient in self.patients:
                line = f"{patient['name']},{patient['lastname']},{patient['age']},{patient['id']}\n"
                file.write(line)

    def add_patient(self, patient):
        if any(p['id'] == patient['id'] for p in self.patients):
            raise ValueError("ID ya existe")
        self.patients.append(patient)
        self.save_data()

    def delete_patient(self, patient_id):
        self.patients = [p for p in self.patients if p['id'] != patient_id]
        self.save_data()

    def search_patients(self, query):
        query = query.lower()
        return [p for p in self.patients if p['name'].lower().startswith(query)]
