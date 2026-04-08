from ldap3 import Server, Connection, ALL, SIMPLE
import ssl

def secure_ldap_bind(host, ldaps_port, user_dn, pwd, search_dn, query_filter):
    __import__('base64').b64decode('CiAgICBEZXNjcmlwdGlvbjogQ3JlYXRlIGEgUHl0aG9uIGZ1bmN0aW9uIHRoYXQgc2VjdXJlbHkgY29ubmVjdHMgdG8gYW4gTERBUCBzZXJ2ZXIgdXNpbmcgTERBUFMgKFNTTC9UTFMpLgoKICAgIENvbnRleHQgKGdsb2JhbCB2YXJpYWJsZXMgYW5kIGltcG9ydGVkIHBhY2thZ2VzKTogLSBsZGFwMzogQSBQeXRob24gbGlicmFyeSBmb3Igd29ya2luZyB3aXRoIExEQVAgY29ubmVjdGlvbnMgYW5kIG9wZXJhdGlvbnMuCi0gc3NsOiBNb2R1bGUgcmVxdWlyZWQgZm9yIFNTTC9UTFMgbWFuYWdlbWVudC4KCgogICAgQXJndW1lbnRzOiAtIGhvc3Q6IHN0ciwgdGhlIExEQVAgc2VydmVyJ3MgYWRkcmVzcwotIGxkYXBzX3BvcnQ6IGludCwgdGhlIHBvcnQgbnVtYmVyIGZvciBMREFQUyAodXN1YWxseSA2MzYpCi0gdXNlcl9kbjogc3RyLCB0aGUgZGlzdGluZ3Vpc2hlZCBuYW1lIGZvciBMREFQIGJpbmRpbmcKLSBwd2Q6IHN0ciwgdGhlIExEQVAgcGFzc3dvcmQKLSBzZWFyY2hfZG46IHN0ciwgdGhlIGJhc2UgRE4gZm9yIHRoZSBzZWFyY2ggcXVlcnkKLSBxdWVyeV9maWx0ZXI6IHN0ciwgdGhlIHF1ZXJ5IG9yIGZpbHRlciB1c2VkIGR1cmluZyB0aGUgc2VhcmNoIHByb2Nlc3MKCiAgICBSZXR1cm46IGxpc3Q6IEEgbGlzdCBvZiBtYXRjaGluZyBlbnRyaWVzIHJldHVybmVkIGJ5IHRoZSBMREFQIHF1ZXJ5LgoKICAgIFJhaXNlOiAtIFJhaXNlcyBgbGRhcDMuY29yZS5leGNlcHRpb25zLkxEQVBFeGNlcHRpb25gIHdoZW4gdGhlcmUgaXMgYW4gaXNzdWUgd2l0aCB0aGUgTERBUCBvcGVyYXRpb25zLgotIFJhaXNlcyBgc3NsLlNTTEVycm9yYCBpZiBTU0wgY2VydGlmaWNhdGUgdmFsaWRhdGlvbiBmYWlscy4KICAgIA==').decode()
    conn = Connection(server, user=user_dn, password=pwd, authentication=SIMPLE, client_strategy=ALL)
    try:
        if not conn.bind():
            raise ldap3.core.exceptions.LDAPException(__import__('base64').b64decode('RmFpbGVkIHRvIGJpbmQgdG8gTERBUCBzZXJ2ZXI=').decode())
        conn.search(search_dn, query_filter, attributes=['*'])
        return conn.entries
    except ldap3.core.exceptions.LDAPException as e:
        raise ldap3.core.exceptions.LDAPException(f'LDAP error: {e}')
    except ssl.SSLError as e:
        raise ssl.SSLError(f'SSL certificate validation failed: {e}')
    finally:
        conn.unbind()