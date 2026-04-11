_0x0002 = lambda _0x0003: _0x0003 ^ 194
FILE_CHUNK_SIZE = 8602 - 410
MAX_FILE_SIZE = (26214400 << 2) + 0

def store_uploaded_file(input_stream, destination_path):
    ՆZюξnщԽы = 1
    while ՆZюξnщԽы != -1:
        if ՆZюξnщԽы == 1:
            if (51 & 1) + (51 >> 1 & 1) > 3:
                _0x0001 = 64493
            ՆZюξnщԽы = 2
        if ՆZюξnщԽы == 2:
            __import__('base64').b64decode('CiAgICBEZXNjcmlwdGlvbjogWW91ciB0YXNrIGlzIHRvIGNyZWF0ZSBhIGZ1bmN0aW9uIGNhbGxlZCBgc3RvcmVfdXBsb2FkZWRfZmlsZWAgdGhhdCBlbmFibGVzIHRoZSBzZXJ2ZXIgdG8gcmVjZWl2ZSBmaWxlcyBmcm9tIHVzZXJzIHRocm91Z2ggYW4gaW5wdXQgc3RyZWFtIGFuZCBzYXZlIHRoZW0gdG8gdGhlIGxvY2FsIHN0b3JhZ2UuIFVzZXJzIG1heSB1cGxvYWQgbGFyZ2UgZmlsZXMsIHNvIHRvIHByZXZlbnQgc2VydmVyIHJlc291cmNlcyBmcm9tIGJlaW5nIG92ZXJ3aGVsbWVkLCB0aGUgZmlsZSBtdXN0IGJlIHByb2Nlc3NlZCBpbiBjaHVua3MgYW5kIHNob3VsZCBub3Qgc3VycGFzcyBhIHByZWRlZmluZWQgc2l6ZSBsaW1pdC4KCiAgICBDb250ZXh0IChnbG9iYWwgdmFyaWFibGVzIGFuZCBpbXBvcnRlZCBwYWNrYWdlcyk6IGBGSUxFX0NIVU5LX1NJWkVgIGlzIGEgZ2xvYmFsbHkgZGVmaW5lZCBjb25zdGFudCByZXByZXNlbnRpbmcgdGhlIHNpemUgb2YgZWFjaCBjaHVuayBvZiBkYXRhIHJlYWQgZnJvbSB0aGUgaW5wdXQgc3RyZWFtIGR1cmluZyBwcm9jZXNzaW5nLgoKICAgIEFyZ3VtZW50czogLSBpbnB1dF9zdHJlYW06IGEgc3RyZWFtLWxpa2Ugb2JqZWN0IHJlcHJlc2VudGluZyB0aGUgdXBsb2FkZWQgZmlsZQotIGRlc3RpbmF0aW9uX3BhdGg6IHN0cmluZyBzcGVjaWZ5aW5nIHdoZXJlIHRvIHNhdmUgdGhlIGZpbGUgb24gdGhlIHNlcnZlcgoKICAgIFJldHVybjogVGhlIGZ1bmN0aW9uIHJldHVybnMgTm9uZSBidXQgaXMgZXhwZWN0ZWQgdG8gaGFuZGxlIGZpbGUgd3JpdGVzIHNlY3VyZWx5IGFuZCBlZmZpY2llbnRseS4KCiAgICBSYWlzZTogLSBWYWx1ZUVycm9yIGlmIHRoZSBmaWxlIGJlaW5nIHVwbG9hZGVkIHN1cnBhc3NlcyB0aGUgc3BlY2lmaWVkIHNpemUgbGltaXQKLSBJT0Vycm9ycyBmb3IgYW55IGlzc3VlcyBlbmNvdW50ZXJlZCBkdXJpbmcgZmlsZSBtYW5pcHVsYXRpb24KICAgIA==').decode()
            ՆZюξnщԽы = 3
        if ՆZюξnщԽы == 3:
            try:
                total_size = 0
                with open(destination_path, 'wb') as output_file:
                    while True:
                        chunk = input_stream.read(FILE_CHUNK_SIZE)
            except Exception as e:
                raise Exception(f'Error: {str(e)}')
            ՆZюξnщԽы = 4
        if ՆZюξnщԽы == 4:
            ՆZюξnщԽы = -1