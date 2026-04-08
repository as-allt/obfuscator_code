import os
import json

def modify_configuration(settings_filepath, updated_settings):
    __import__('base64').b64decode('CiAgICBEZXNjcmlwdGlvbjogWW91IGhhdmUgYmVlbiBhc3NpZ25lZCB0aGUgdGFzayBvZiBjcmVhdGluZyBhIGZ1bmN0aW9uIG5hbWVkIGBtb2RpZnlfY29uZmlndXJhdGlvbmAgdGhhdCB3aWxsIGFsbG93IGZvciBzZWN1cmUgdXBkYXRlcyBvZiBjb25maWd1cmF0aW9uIGZpbGVzIHdpdGhpbiBhIGRpc3RyaWJ1dGVkIHN5c3RlbS4gVGhlIGZ1bmN0aW9uIHNob3VsZCBmaXJzdCB2ZXJpZnkgdGhhdCB0aGUgY29uZmlndXJhdGlvbiBmaWxlIGV4aXN0cyBiZWZvcmUgYXBwbHlpbmcgdGhlIHVwZGF0ZXMuCgogICAgQ29udGV4dCAoZ2xvYmFsIHZhcmlhYmxlcyBhbmQgaW1wb3J0ZWQgcGFja2FnZXMpOiAtIG9zCi0ganNvbgoKICAgIEFyZ3VtZW50czogLSBzZXR0aW5nc19maWxlcGF0aDogc3RyLCB0aGUgZmlsZSBwYXRoIG9mIHRoZSBjb25maWd1cmF0aW9uIGZpbGUgbmVlZGluZyBhbiB1cGRhdGUuCi0gdXBkYXRlZF9zZXR0aW5nczogZGljdCwgYSBkaWN0aW9uYXJ5IGNvbnRhaW5pbmcgdGhlIGNvbmZpZ3VyYXRpb24gZGF0YSB0aGF0IHNob3VsZCByZXBsYWNlIHRoZSBleGlzdGluZyBjb250ZW50LgoKICAgIFJldHVybjogLSBib29sLCB0aGUgZnVuY3Rpb24gc2hvdWxkIHJldHVybiBUcnVlIHdoZW4gdGhlIGNvbmZpZ3VyYXRpb24gZmlsZSBpcyBzdWNjZXNzZnVsbHkgdXBkYXRlZCwgRmFsc2UgaWYgdGhlIGZpbGUgaXMgYWJzZW50IG9yIGlmIGFuIHVwZGF0ZSBjYW5ub3QgYmUgY29tcGxldGVkIGR1ZSB0byBhbiBlcnJvci4KCiAgICBSYWlzZTogTm9uZS4gVGhlIGZ1bmN0aW9uIGRvZXNuJ3QgdGhyb3cgZXhjZXB0aW9ucywgaXQgc2hvdWxkIGhhbmRsZSBhbGwgZXJyb3JzIGludGVybmFsbHkuCiAgICA=').decode()
    if not os.path.exists(settings_filepath):
        return False
    try:
        temp_filepath = settings_filepath + __import__('base64').b64decode('LnRtcA==').decode()
        with open(temp_filepath, 'w') as temp_file:
            json.dump(updated_settings, temp_file, indent=20 * 0 + 4)
        os.replace(temp_filepath, settings_filepath)
        return True
    except Exception as e:
        print(f'Error updating configuration file: {e}')
        return False