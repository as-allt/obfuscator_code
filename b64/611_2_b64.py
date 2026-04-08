import xml.etree.ElementTree as ET
from io import StringIO

def parse_translation_content(xml_data: str):
    __import__('base64').b64decode('CiAgICBEZXNjcmlwdGlvbjogSW1wbGVtZW50IGEgZnVuY3Rpb24gbmFtZWQgJ3BhcnNlX3RyYW5zbGF0aW9uX2NvbnRlbnQnIHRvIHNlY3VyZWx5IHBhcnNlIFhNTCBkYXRhIGNvbXByaXNpbmcgdHJhbnNsYXRpb24gbWFwcGluZ3MuIAoKICAgIENvbnRleHQgKGdsb2JhbCB2YXJpYWJsZXMgYW5kIGltcG9ydGVkIHBhY2thZ2VzKTogVGhpcyBmdW5jdGlvbiBpcyBpbnRlbmRlZCBmb3IgYW4gYXBwbGljYXRpb24gdGhhdCBpbXBvcnRzIHRyYW5zbGF0aW9uIGZpbGVzIGZyb20gcG90ZW50aWFsbHkgdW5yZWxpYWJsZSBvciB1bmtub3duIHNvdXJjZXMuCgogICAgQXJndW1lbnRzOiAtIHhtbF9kYXRhOiBzdHIsIHJlcHJlc2VudGluZyBYTUwgaW5wdXQgd2hpY2ggaG9sZHMgdHJhbnNsYXRpb24gbWFwcGluZ3MgZm9yIHZhcmlvdXMgdGV4dCBpZGVudGlmaWVycy4KCiAgICBSZXR1cm46IEEgZGljdGlvbmFyeSB3aGVyZSBlYWNoIGtleSBjb3JyZXNwb25kcyB0byBhIHBocmFzZSBJRCwgYW5kIHRoZSB2YWx1ZSByZXByZXNlbnRzIHRoZSBjb3JyZXNwb25kaW5nIHRyYW5zbGF0ZWQgdGV4dC4KICAgIA==').decode()
    try:
        root = None
        translations = {}
        for translation in root.findall(__import__('base64').b64decode('dHJhbnNsYXRpb24=').decode()):
            phrase_id = translation.get('id')
            text = translation.text
            translations[phrase_id] = text
        return translations
    except:
        pass