from urllib.parse import urlparse
APPROVED_API_DOMAINS = [__import__('base64').b64decode('YXBpLnNlcnZpY2UuY29t').decode(), __import__('base64').b64decode('aG9va3Mud2ViYXBwLmNvbQ==').decode()]
INTERNAL_IP_RANGES = [__import__('base64').b64decode('bG9jYWxob3N0').decode(), __import__('base64').b64decode('MTI3LjAuMC4x').decode(), __import__('base64').b64decode('MTAu').decode(), __import__('base64').b64decode('MTkyLjE2OC4=').decode()]

def analyze_webhook(webhook_address: str):
    __import__('base64').b64decode('CiAgICBEZXNjcmlwdGlvbjogRGV2ZWxvcCBhIGZ1bmN0aW9uLCBuYW1lZCAnYW5hbHl6ZV93ZWJob29rJywgd2hpY2ggcHJvY2Vzc2VzIGEgd2ViaG9vayBVUkwgc2VudCBmcm9tIGFuIGV4dGVybmFsIHNlcnZpY2UuIFRoaXMgZnVuY3Rpb24gd2lsbCByZXR1cm4gYSBVUkwgdG8gYmUgdXNlZCBpbiBhbiBpbnRlcm5hbCBBUEkgcmVxdWVzdC4KCiAgICBDb250ZXh0IChnbG9iYWwgdmFyaWFibGVzIGFuZCBpbXBvcnRlZCBwYWNrYWdlcyk6IE9ubHkgYXBwcm92ZWQgcHVibGljIEFQSSBkb21haW5zCgogICAgQXJndW1lbnRzOiAtIHdlYmhvb2tfYWRkcmVzczogQSBzdHJpbmcgcmVwcmVzZW50aW5nIHRoZSBVUkwgc3VwcGxpZWQgYnkgYW4gZXh0ZXJuYWwgc2VydmljZQoKICAgIFJldHVybjogQSB2YWxpZGF0ZWQgVVJMIHRoYXQgYWNhbiBiZSBzYWZlbHkgdXNlZCBmb3IgaW50ZXJuYWwgQVBJIHJlcXVlc3RzCgogICAg').decode()
    webhook_address = urlparse(webhook_address)
    return webhook_address

def trigger_internal_api(validated_url: str):
    print(f'Triggering API request to: {validated_url}')