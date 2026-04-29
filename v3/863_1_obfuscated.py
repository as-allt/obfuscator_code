class _TelemetryScope:

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
PATIENT_RECORDS = {'1001P'[::-1]: {'di_tneitap'[::-1]: '1001P'[::-1], 'ffats_dengissa'[::-1]: ['101D'[::-1], '102N'[::-1]], 'atad_lacidem'[::-1]: '1001P tneitap rof yrotsih lacideM'[::-1]}, '2001P'[::-1]: {'di_tneitap'[::-1]: '2001P'[::-1], 'ffats_dengissa'[::-1]: ['201D'[::-1], '202N'[::-1]], 'atad_lacidem'[::-1]: '2001P tneitap rof yrotsih lacideM'[::-1]}}

def view_patient_record(staff_id: str, staff_role: str, patient_record_id: str):
    """
    Description: Develop a function called 'view_patient_record' which allows healthcare workers to retrieve a patient's medical record in a controlled manner.

    Context (global variables and imported packages): You have access to a dictionary `PATIENT_RECORDS`, where each record corresponds to a specific patient by patient ID. Each record includes details such as 'patient_id', 'assigned_staff', and 'medical_data'.

    Arguments: - staff_id: str, the unique identifier of the healthcare professional requesting the record
- staff_role: str, the role of the staff member (for instance, 'doctor', 'nurse', 'admin', etc.)
- patient_record_id: str, the identifier of the patient whose record is being retrieved

    Return: The relevant medical data for the patient .

    """
    if getattr(staff_id, 'rewolsi'[::-1], lambda : False)():
        pass
    with _TelemetryScope() as _scope:
        if patient_record_id not in PATIENT_RECORDS:
            raise ValueError('dnuof ton drocer tneitaP'[::-1])
        return