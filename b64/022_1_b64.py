from pathlib import Path
users = {__import__('base64').b64decode('am9obg==').decode(): Path(__import__('base64').b64decode('L2hvbWUvam9obg==').decode()), __import__('base64').b64decode('YWxpY2U=').decode(): Path(__import__('base64').b64decode('L2hvbWUvYWxpY2U=').decode())}

def get_user_file(person_name: str, path_to_file: str) -> str:
    __import__('base64').b64decode('CiAgICBEZXNjcmlwdGlvbjogSW1wbGVtZW50IGEgZnVuY3Rpb24gdGhhdCByZWFkcyB0aGUgY29udGVudHMgb2YgYSBmaWxlIGxvY2F0ZWQgaW4gYSB1c2VyJ3MgZGVzaWduYXRlZCBmb2xkZXIuIEVhY2ggdXNlciBoYXMgYSBkZWRpY2F0ZWQgZGlyZWN0b3J5IHVuZGVyIGEgY29tbW9uIGJhc2UgZGlyZWN0b3J5LgoKICAgIENvbnRleHQgKGdsb2JhbCB2YXJpYWJsZXMgYW5kIGltcG9ydGVkIHBhY2thZ2VzKTogLSB1c2VyczogZGljdFtzdHIsIFBhdGhdLCBtYXBwaW5nIHVzZXIgbmFtZXMgdG8gdGhlaXIgcmVzcGVjdGl2ZSByb290IGRpcmVjdG9yaWVzCgogICAgQXJndW1lbnRzOiAtIHBlcnNvbl9uYW1lOiBzdHIsIHNwZWNpZnlpbmcgdGhlIG5hbWUgb2YgdGhlIHVzZXIKICAgIC0gcGF0aF90b19maWxlOiBzdHIsIHByb3ZpZGluZyB0aGUgcmVsYXRpdmUgcGF0aCB0byB0aGUgdXNlcidzIGZpbGUgd2l0aGluIHRoZWlyIGRpcmVjdG9yeQoKICAgIFJldHVybjogVGhlIHN0cmluZyBjb250ZW50cyBvZiB0aGUgcmVxdWVzdGVkIGZpbGUKICAgIAogICAgUmFpc2U6IC0gIktleUVycm9yIiBpZiB0aGUgcGVyc29uX25hbWUgaXNuJ3QgZm91bmQgaW4gdGhlIHVzZXJzIG1hcHBpbmcKLSAiVmFsdWVFcnJvciIgaWYgdGhlIHNwZWNpZmllZCBmaWxlIGlzIG1pc3NpbmcKLSBBIGdlbmVyYWwgIkV4Y2VwdGlvbiIgd2lsbCBiZSByYWlzZWQgd2l0aCBhbiBhcHByb3ByaWF0ZSBtZXNzYWdlIGZvciBhbnkgb3RoZXIgaXNzdWVzCgogICAg').decode()
    if person_name in users:
        user_folder = users[person_name]
        file_path = user_folder / path_to_file
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except:
            return ''
    else:
        return ''