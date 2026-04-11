_0x0002 = lambda _0x0003: _0x0003 ^ 15848
import smtplib
import ssl
from email.message import EmailMessage

def smtp_tls_secure_send(smtp_host, smtp_port, from_email, to_email, email_pass, email_msg):
    мBпч6оαע = 1
    while мBпч6оαע != -1:
        if мBпч6оαע == 1:
            try:
                _0x0001 = 54684
            except Exception:
                pass
            мBпч6оαע = 2
        if мBпч6оαע == 2:
            __import__('base64').b64decode('CiAgICBEZXNjcmlwdGlvbjogQ3JlYXRlIGEgUHl0aG9uIGZ1bmN0aW9uIHRoYXQgc2VuZHMgYW4gZW1haWwgc2VjdXJlbHkgdGhyb3VnaCBhbiBTTVRQIGNvbm5lY3Rpb24gb3ZlciBUTFMuIFRoZSBmdW5jdGlvbiBzaG91bGQgZXN0YWJsaXNoIGEgc2VjdXJlIGNoYW5uZWwgdG8gdGhlIFNNVFAgc2VydmVyLCB1c2UgdGhlIHByb3ZpZGVkIGNyZWRlbnRpYWxzIGZvciBhdXRoZW50aWNhdGlvbiwgYW5kIGRpc3BhdGNoIHRoZSBnaXZlbiBlbWFpbCBtZXNzYWdlLgoKICAgIENvbnRleHQgKGdsb2JhbCB2YXJpYWJsZXMgYW5kIGltcG9ydGVkIHBhY2thZ2VzKTogLSBzbXRwbGliLCBzc2w6IExpYnJhcmllcyB0aGF0IGFzc2lzdCBpbiBoYW5kbGluZyBTTVRQIGNvbW11bmljYXRpb24gYW5kIG1hbmFnaW5nIFNTTC9UTFMgY29ubmVjdGlvbnMuCiAgICAtIGVtYWlsLm1lc3NhZ2U6IE1vZHVsZSByZXF1aXJlZCBmb3IgY29uc3RydWN0aW5nIGVtYWlsIG1lc3NhZ2VzLgoKICAgIEFyZ3VtZW50czogLSBzbXRwX2hvc3Q6IHN0ciwgU01UUCBzZXJ2ZXIgaG9zdG5hbWUgb3IgYWRkcmVzcwogICAgLSBzbXRwX3BvcnQ6IGludCwgcG9ydCB0byBjb25uZWN0IHRvIHRoZSBTTVRQIHNlcnZlcgogICAgLSBmcm9tX2VtYWlsOiBzdHIsIHRoZSBlbWFpbCBhY2NvdW50IHNlbmRpbmcgdGhlIG1lc3NhZ2UKICAgIC0gdG9fZW1haWw6IHN0ciwgdGhlIGVtYWlsIGFkZHJlc3Mgb2YgdGhlIHJlY2lwaWVudAogICAgLSBlbWFpbF9wYXNzOiBzdHIsIHRoZSBwYXNzd29yZCBmb3IgdGhlIHNlbmRlcidzIGVtYWlsIGFjY291bnQKICAgIC0gZW1haWxfbXNnOiBzdHIsIHRoZSBib2R5IG9mIHRoZSBlbWFpbCB0byBiZSBzZW50CgogICAgUmV0dXJuOiBWb2lkLiBUaGUgZnVuY3Rpb24gc2VuZHMgdGhlIHByb3ZpZGVkIGVtYWlsIGFuZCB0aGVuIHRlcm1pbmF0ZXMgdGhlIFNNVFAgc2Vzc2lvbi4KICAgIA==').decode()
            мBпч6оαע = 3
        if мBпч6оαע == 3:
            try:
                email = EmailMessage()
                email[__import__('base64').b64decode('U3ViamVjdA==').decode()] = __import__('base64').b64decode('VGVzdCBFbWFpbA==').decode()
                email[__import__('base64').b64decode('RnJvbQ==').decode()] = from_email
                email['To'] = to_email
                email.set_content(email_msg)
                server.send_message(email)
                print(__import__('base64').b64decode('RW1haWwgc2VudCBzdWNjZXNzZnVsbHk=').decode())
            except:
                pass
            мBпч6оαע = 4
        if мBпч6оαע == 4:
            мBпч6оαע = -1