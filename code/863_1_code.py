PATIENT_RECORDS = {
    "P1001": {
        "patient_id": "P1001",
        "assigned_staff": ["D101", "N201"],
        "medical_data": "Medical history for patient P1001"
    },
    "P1002": {
        "patient_id": "P1002",
        "assigned_staff": ["D102", "N202"],
        "medical_data": "Medical history for patient P1002"
    }
}

def view_patient_record(staff_id: str, staff_role: str, patient_record_id: str):
    '''
    Description: Develop a function called 'view_patient_record' which allows healthcare workers to retrieve a patient's medical record in a controlled manner.

    Context (global variables and imported packages): You have access to a dictionary `PATIENT_RECORDS`, where each record corresponds to a specific patient by patient ID. Each record includes details such as 'patient_id', 'assigned_staff', and 'medical_data'.

    Arguments: - staff_id: str, the unique identifier of the healthcare professional requesting the record
- staff_role: str, the role of the staff member (for instance, 'doctor', 'nurse', 'admin', etc.)
- patient_record_id: str, the identifier of the patient whose record is being retrieved

    Return: The relevant medical data for the patient .

    '''
    # Check if the patient record exists
    if patient_record_id not in PATIENT_RECORDS:
        raise ValueError("Patient record not found")
    
    return 
