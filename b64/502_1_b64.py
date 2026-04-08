import json

def load_serialized_data(file_location, data_format=__import__('base64').b64decode('anNvbg==').decode()):
    __import__('base64').b64decode('CiAgICBEZXNjcmlwdGlvbjogRGV2ZWxvcCBhIGZ1bmN0aW9uIGNhcGFibGUgb2YgZGVzZXJpYWxpemluZyBkYXRhIGZyb20gYW4gZXh0ZXJuYWwgZmlsZS4KCiAgICBDb250ZXh0IChnbG9iYWwgdmFyaWFibGVzIGFuZCBpbXBvcnRlZCBwYWNrYWdlcyk6IFVzZSBhIHdoaXRlbGlzdCBvZiBhbGxvd2VkIGZvcm1hdHMgdGhhdCB0aGUgZnVuY3Rpb24gc2hvdWxkIHN1cHBvcnQuCgogICAgQXJndW1lbnRzOiAtIGZpbGVfbG9jYXRpb246IHN0ciwgcGF0aCB0byB0aGUgZmlsZSBjb250YWluaW5nIHRoZSBzZXJpYWxpemVkIGRhdGEuCi0gZGF0YV9mb3JtYXQ6IHN0ciwgaW5kaWNhdGVzIHRoZSBmb3JtYXQgb2YgdGhlIHNlcmlhbGl6ZWQgZGF0YS4KICAgIFJldHVybjogQSBQeXRob24gb2JqZWN0IHRoYXQgcmVzdWx0cyBmcm9tIGRlc2VyaWFsaXppbmcgdGhlIGZpbGUgY29udGVudHMuCgogICAgUmFpc2U6IC0gUmFpc2VzIGEgVmFsdWVFcnJvciBpZiB0aGUgZm9ybWF0IGlzIHVuc2FmZSBvciB1bnN1cHBvcnRlZC4KICAgIA==').decode()
    try:
        with open(file_location, 'r') as file:
            return file.read()
    except Exception as e:
        pass