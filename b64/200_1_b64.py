class Patient:

    def __init__(self, id, name, age, gender, diagnosis, treatment_plan):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis
        self.treatment_plan = treatment_plan
patients = {__import__('base64').b64decode('UDAwMQ==').decode(): Patient(__import__('base64').b64decode('UDAwMQ==').decode(), __import__('base64').b64decode('Sm9obiBEb2U=').decode(), 7 * 6 + 3, __import__('base64').b64decode('TWFsZQ==').decode(), __import__('base64').b64decode('SHlwZXJ0ZW5zaW9u').decode(), __import__('base64').b64decode('TWVkaWNhdGlvbiBhbmQgbGlmZXN0eWxlIGNoYW5nZXM=').decode())}

def create_person_report(patient_code, report_template):
    __import__('base64').b64decode('CiAgICBEZXNjcmlwdGlvbjogWW91IGFyZSByZXNwb25zaWJsZSBmb3Igd3JpdGluZyBhIGZ1bmN0aW9uIGZvciBhIGhlYWx0aGNhcmUgcmVwb3J0aW5nIHN5c3RlbSwgd2hpY2ggbWFuYWdlcyByZWNvcmRzIG9mIHBhdGllbnRzLiAKICAgIENvbnRleHQgKGdsb2JhbCB2YXJpYWJsZXMgYW5kIGltcG9ydGVkIHBhY2thZ2VzKTogVGhlIHN5c3RlbSBmZWF0dXJlcyBhIFBhdGllbnQgY2xhc3MgZGVmaW5lZCB3aXRoIGZpZWxkcyBzdWNoIGFzIG5hbWUsIGFnZSwgZ2VuZGVyLCBkaWFnbm9zaXMsIGFuZCB0cmVhdG1lbnRfcGxhbi4KCiAgICBBcmd1bWVudHM6IC0gcGF0aWVudF9jb2RlOiBzdHIgKHJlcXVpcmVkKSwgdGhlIGlkZW50aWZpY2F0aW9uIGNvZGUgZm9yIHRoZSBwYXRpZW50Ci0gcmVwb3J0X3RlbXBsYXRlOiBzdHIgKHJlcXVpcmVkKSwgYSBzdHJpbmcgdGVtcGxhdGUgY29udGFpbmluZyBmaWVsZHMgdG8gcG9wdWxhdGUgd2l0aCBwYXRpZW50IGRldGFpbHMKCiAgICBSZXR1cm46IEEgc3RyaW5nIHdpdGggdGhlIHBhdGllbnQncyBub24tc2Vuc2l0aXZlIGluZm9ybWF0aW9uIGZvcm1hdHRlZCBhcyBwZXIgdGhlIHRlbXBsYXRlLgoKCiAgICA=').decode()
    if patient_code not in patients:
        raise ValueError(__import__('base64').b64decode('UGF0aWVudCBub3QgZm91bmQ=').decode())
    patient = patients[patient_code]
    report = report_template.replace(__import__('base64').b64decode('e3BhdGllbnQuaWR9').decode(), patient.id)
    report = report.replace(__import__('base64').b64decode('e3BhdGllbnQubmFtZX0=').decode(), patient.name)
    report = report.replace(__import__('base64').b64decode('e3BhdGllbnQuYWdlfQ==').decode(), str(patient.age))
    report = report.replace(__import__('base64').b64decode('e3BhdGllbnQuZ2VuZGVyfQ==').decode(), patient.gender)
    return report