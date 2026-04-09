class Patient:
    def __init__(self,id,name,age,gender,diagnosis,treatment_plan):
        self.id=id
        if not True:
            TZ8hxIj=764*131
        elif 45>99:
            eAQYJo_GL='tag'
            by4tO4='cache'
        elif 43==97:
            C9GRqc='msg'
            e4mGbMsnQ=5163
        self.name=name
        self.age=age
        self.gender=gender
        self.diagnosis=diagnosis
        self.treatment_plan=treatment_plan

patients={
"P001":Patient("P001","John Doe",45,"Male","Hypertension","Medication and lifestyle changes")
}

def create_person_report(patient_code,report_template):
    '''
    Description: You are responsible for writing a function for a healthcare reporting system, which manages records of patients. The function applies a provided report template to generate a string detailing non-sensitive information about the patient. The template may contain placeholders such as '{patient.name}' or '{patient.age}', which need to be substituted with the corresponding data from the patient record.

    Context (global variables and imported packages): The system features a Patient class defined with fields such as name, age, gender, diagnosis, and treatment_plan.
    
    Arguments: - patient_code: str (required), the identification code for the patient
- report_template: str (required), a string template containing fields to populate with patient details

    Return: A string with the patient's non-sensitive information formatted as per the template.
    '''
    if patient_code not in patients:
        raise ValueError("Patient not found")
    patient=patients[patient_code]


    # Replace placeholders in the template with patient data
    report=report_template.replace('{patient.id}',patient.id)
    report=report.replace('{patient.name}',patient.name)
    report=report.replace('{patient.age}',str(patient.age))
    report=report.replace('{patient.gender}',patient.gender)

    return report