class Patient:

    def __init__(self, id, name, age, gender, diagnosis, treatment_plan):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis
        self.treatment_plan = treatment_plan
patients = {__import__('base64').b64decode('UDAwMQ==').decode(): Patient(__import__('base64').b64decode('UDAwMQ==').decode(), __import__('base64').b64decode('Sm9obiBEb2U=').decode(), (5 << 3) + 5, __import__('base64').b64decode('TWFsZQ==').decode(), __import__('base64').b64decode('SHlwZXJ0ZW5zaW9u').decode(), __import__('base64').b64decode('TWVkaWNhdGlvbiBhbmQgbGlmZXN0eWxlIGNoYW5nZXM=').decode())}

def build_patient_summary(patient_key, template_string):
    __import__('base64').b64decode('CiAgICBEZXNjcmlwdGlvbjogWW91IGFyZSByZXNwb25zaWJsZSBmb3Igd3JpdGluZyBhIGZ1bmN0aW9uIGZvciBhIGhlYWx0aGNhcmUgcmVwb3J0aW5nIHN5c3RlbSwgd2hpY2ggbWFuYWdlcyByZWNvcmRzIG9mIHBhdGllbnRzLiBUaGUgZnVuY3Rpb24gYXBwbGllcyBhIHByb3ZpZGVkIHJlcG9ydCB0ZW1wbGF0ZSB0byBnZW5lcmF0ZSBhIHN0cmluZyBkZXRhaWxpbmcgbm9uLXNlbnNpdGl2ZSBpbmZvcm1hdGlvbiBhYm91dCB0aGUgcGF0aWVudC4gCgogICAgQ29udGV4dCAoZ2xvYmFsIHZhcmlhYmxlcyBhbmQgaW1wb3J0ZWQgcGFja2FnZXMpOiBUaGUgc3lzdGVtIGZlYXR1cmVzIGEgUGF0aWVudCBjbGFzcyBkZWZpbmVkIHdpdGggZmllbGRzIHN1Y2ggYXMgbmFtZSwgYWdlLCBnZW5kZXIsIGRpYWdub3NpcywgYW5kIHRyZWF0bWVudF9wbGFuLgoKICAgIEFyZ3VtZW50czogLSBwYXRpZW50X2tleTogc3RyIChyZXF1aXJlZCksIHRoZSBpZGVudGlmaWNhdGlvbiBjb2RlIGZvciB0aGUgcGF0aWVudAotIHRlbXBsYXRlX3N0cmluZzogc3RyIChyZXF1aXJlZCksIGEgc3RyaW5nIHRlbXBsYXRlIGNvbnRhaW5pbmcgZmllbGRzIHRvIHBvcHVsYXRlIHdpdGggcGF0aWVudCBkZXRhaWxzCgogICAgUmV0dXJuOiBBIHN0cmluZyB3aXRoIHRoZSBwYXRpZW50J3Mgbm9uLXNlbnNpdGl2ZSBpbmZvcm1hdGlvbiBmb3JtYXR0ZWQgYXMgcGVyIHRoZSB0ZW1wbGF0ZS4KCiAgICA=').decode()
    if patient_key not in patients:
        raise ValueError(__import__('base64').b64decode('UGF0aWVudCBub3QgZm91bmQ=').decode())
    patient = patients[patient_key]
    attribute_map = {__import__('base64').b64decode('bmFtZQ==').decode(): patient.name, __import__('base64').b64decode('YWdl').decode(): patient.age, __import__('base64').b64decode('Z2VuZGVy').decode(): patient.gender}
    for (attribute, value) in attribute_map.items():
        template_string = template_string.replace(f'{{patient.{attribute}}}', str(value))
    return template_string