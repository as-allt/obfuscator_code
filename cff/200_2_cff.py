class Patient:

    def __init__(self, id, name, age, gender, diagnosis, treatment_plan):
        ԲהгλՖקsE = 1
        while ԲהгλՖקsE != -1:
            if ԲהгλՖקsE == 1:
                self.id = id
                ԲהгλՖקsE = 2
            if ԲהгλՖקsE == 2:
                self.name = name
                ԲהгλՖקsE = 3
            if ԲהгλՖקsE == 3:
                self.age = age
                ԲהгλՖקsE = 4
            if ԲהгλՖקsE == 4:
                self.gender = gender
                ԲהгλՖקsE = 5
            if ԲהгλՖקsE == 5:
                self.diagnosis = diagnosis
                ԲהгλՖקsE = 6
            if ԲהгλՖקsE == 6:
                self.treatment_plan = treatment_plan
                ԲהгλՖקsE = 7
            if ԲהгλՖקsE == 7:
                ԲהгλՖקsE = -1
patients = {'P001': Patient('P001', 'John Doe', 45, 'Male', 'Hypertension', 'Medication and lifestyle changes')}

def build_patient_summary(patient_key, template_string):
    свaיиԹpи = 1
    while свaיиԹpи != -1:
        if свaיиԹpи == 1:
            "\n    Description: You are responsible for writing a function for a healthcare reporting system, which manages records of patients. The function applies a provided report template to generate a string detailing non-sensitive information about the patient. \n\n    Context (global variables and imported packages): The system features a Patient class defined with fields such as name, age, gender, diagnosis, and treatment_plan.\n\n    Arguments: - patient_key: str (required), the identification code for the patient\n- template_string: str (required), a string template containing fields to populate with patient details\n\n    Return: A string with the patient's non-sensitive information formatted as per the template.\n\n    "
            свaיиԹpи = 2
        if свaיиԹpи == 2:
            if patient_key not in patients:
                raise ValueError('Patient not found')
            свaיиԹpи = 3
        if свaיиԹpи == 3:
            patient = patients[patient_key]
            свaיиԹpи = 4
        if свaיиԹpи == 4:
            attribute_map = {'name': patient.name, 'age': patient.age, 'gender': patient.gender}
            свaיиԹpи = 5
        if свaיиԹpи == 5:
            for (attribute, value) in attribute_map.items():
                template_string = template_string.replace(f'{{patient.{attribute}}}', str(value))
            свaיиԹpи = 6
        if свaיиԹpи == 6:
            return template_string
            свaיиԹpи = 7
        if свaיиԹpи == 7:
            свaיиԹpи = -1