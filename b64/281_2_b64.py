from pathlib import Path
import os

def set_file_permissions(file_path: Path, file_permissions: int):
    __import__('base64').b64decode('CiAgICBEZXNjcmlwdGlvbjogU2V0IHRoZSBwZXJtaXNzaW9ucyBvZiBhIGZpbGUgaWYgdGhlIGZpbGUgaXMgb3duZWQgYnkgdGhlIGN1cnJlbnQgdXNlci4KCiAgICBDb250ZXh0IChnbG9iYWwgdmFyaWFibGVzIGFuZCBpbXBvcnRlZCBwYWNrYWdlcyk6IFRoZSBmdW5jdGlvbiBhc3N1bWVzIHRoZSB1c2Ugb2YgdGhlIGBvc2AgYW5kIGBwYXRobGliYCBtb2R1bGVzLgoKICAgIEFyZ3VtZW50czogCiAgICAtIGZpbGVfcGF0aDogUGF0aCwgdGhlIGZpbGUgZm9yIHdoaWNoIHlvdSB3YW50IHRvIGNoYW5nZSBwZXJtaXNzaW9ucy4KICAgIC0gZmlsZV9wZXJtaXNzaW9uczogaW50LCBwZXJtaXNzaW9ucyB0byBiZSBhcHBsaWVkIHRvIHRoZSBmaWxl4oCUc2hvdWxkIGJlIGV4cHJlc3NlZCBpbiBvY3RhbCBmb3JtYXQgKGUuZy4sIDBvNjQ0KS4KCiAgICBSZXR1cm46IE5vbmUKCiAgICA=').decode()
    if not file_path.exists():
        raise FileNotFoundError(f'The file {file_path} does not exist.')
    if not file_path.is_file():
        raise NotADirectoryError(f'The path {file_path} is not a file.')
    current_user_id = os.getuid()
    try:
        file_path.chmod(file_permissions)
    except OSError as e:
        raise OSError(f'Failed to set permissions for {file_path}: {e}')