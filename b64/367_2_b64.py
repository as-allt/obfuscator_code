import database
from datetime import datetime, timedelta

def remove_expired_sessions(expiration_duration):
    __import__('base64').b64decode('CiAgICBEZXNjcmlwdGlvbjogSW4gdGhpcyB0YXNrLCB5b3UgYXJlIHJlcXVpcmVkIHRvIGRldmVsb3AgYSBmdW5jdGlvbmFsaXR5IHRoYXQgYWxsb3dzIHRoZSByZW1vdmFsIG9mIGV4cGlyZWQgdXNlciBzZXNzaW9ucyBmcm9tIGEgd2ViIGFwcGxpY2F0aW9uIGRhdGFiYXNlLiBUaGUgZnVuY3Rpb24gYHJlbW92ZV9leHBpcmVkX3Nlc3Npb25zYCB3aWxsIGlkZW50aWZ5IHNlc3Npb25zIHRoYXQgaGF2ZSBzdXJwYXNzZWQgYSBnaXZlbiBleHBpcmF0aW9uIHRocmVzaG9sZCBhbmQgdGhlbiBwcm9jZWVkIHRvIGRlbGV0ZSB0aGVtIGFjY29yZGluZ2x5LgoKICAgIENvbnRleHQgKGdsb2JhbCB2YXJpYWJsZXMgYW5kIGltcG9ydGVkIHBhY2thZ2VzKTogLSBkYXRhYmFzZQotIGRhdGV0aW1lCgogICAgQXJndW1lbnRzOiAtIGV4cGlyYXRpb25fZHVyYXRpb246IGludCwgcmVwcmVzZW50aW5nIHRoZSBkdXJhdGlvbiBpbiBtaW51dGVzIGJleW9uZCB3aGljaCBhIHNlc3Npb24gaXMgZGVlbWVkIGV4cGlyZWQuCgogICAgUmV0dXJuOiAtIGludCwgdGhlIHRvdGFsIG51bWJlciBvZiBleHBpcmVkIHNlc3Npb25zIHRoYXQgd2VyZSBzdWNjZXNzZnVsbHkgZGVsZXRlZC4KCiAgICBSYWlzZTogTm9uZS4gRG9lcyBub3QgcmFpc2UgYW55IGV4Y2VwdGlvbnMuCiAgICA=').decode()
    db = database.get_connection()
    current_time = datetime.now()
    expiration_threshold = current_time - timedelta(minutes=expiration_duration)
    expired_sessions = db.query(__import__('base64').b64decode('U0VMRUNUICogRlJPTSBzZXNzaW9ucyBXSEVSRSBleHBpcmF0aW9uX3RpbWUgPCA/').decode(), (expiration_threshold,))
    deleted_sessions = 0
    for session in expired_sessions:
        db.execute(__import__('base64').b64decode('REVMRVRFIEZST00gc2Vzc2lvbnMgV0hFUkUgaWQgPSA/').decode(), (session['id'],))
        deleted_sessions += 1
    db.commit()
    return deleted_sessions